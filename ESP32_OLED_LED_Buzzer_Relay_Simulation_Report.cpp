#include <Arduino.h>
#include <WiFi.h>
#include <WebServer.h>
#include <Wire.h>
#include <U8g2lib.h>
#include <time.h>
#include <vector>
#include "config.h"

struct FamilyMember {
  uint16_t id;
  String name;
  bool inside;
};

enum class FlowState {
  IDLE,
  PENDING_OWNER_DECISION,
  WAITING_SECURITY_KEY
};

WebServer server(80);
U8G2_SSD1306_128X64_NONAME_F_HW_I2C oled(U8G2_R0, U8X8_PIN_NONE);

// Core runtime state
std::vector<FamilyMember> familyMembers;
std::vector<String> eventLog;

uint16_t nextFamilyId = 1;
uint32_t nextUnknownVisitorId = 1;
uint32_t nextEventId = 1;

FlowState flowState = FlowState::IDLE;
uint32_t pendingUnknownId = 0;
String pendingUnknownLabel = "";
unsigned long pendingDecisionStartMs = 0;
unsigned long ownerDecisionTimeoutMs = OWNER_DECISION_TIMEOUT_MS_DEFAULT;

String demoSecurityKey = "2468";
uint8_t keyFailures = 0;
uint8_t unauthorizedStreak = 0;

// Lock and indicators
bool lockUnlocked = false;
unsigned long lockUnlockUntilMs = 0;

bool alarmActive = false;
bool alarmSilenced = false;

unsigned long chirpUntilMs = 0;
unsigned long testBuzzerUntilMs = 0;

// OLED banner override
String oledBannerTitle = "";
String oledBannerDetail = "";
unsigned long oledBannerUntilMs = 0;
unsigned long lastOledDrawMs = 0;

// Physical output shadow (for API sync)
bool outRed = false;
bool outGreen = false;
bool outRelay = false;
bool outBuzzer = false;

// Buttons previous state (INPUT_PULLUP: HIGH idle, LOW pressed)
uint8_t prevExit = HIGH;
uint8_t prevYes = HIGH;
uint8_t prevNo = HIGH;

String lastEvent = "System booted.";

static const char INDEX_HTML[] PROGMEM = R"HTML(
<!doctype html>
<html>
<head>
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>ESP32 Smart Door Security</title>
  <style>
    :root { color-scheme: light dark; }
    body { font-family: Arial, sans-serif; margin: 12px; max-width: 1100px; }
    h2, h3 { margin: 10px 0 6px; }
    .grid { display: grid; grid-template-columns: repeat(auto-fit,minmax(250px,1fr)); gap: 10px; }
    .card { border: 1px solid #8885; border-radius: 10px; padding: 10px; }
    .row { display: flex; gap: 6px; flex-wrap: wrap; align-items: center; margin: 6px 0; }
    input, button, select { padding: 8px; border-radius: 8px; border: 1px solid #8888; }
    button { cursor: pointer; }
    .ok { color: #0a8; font-weight: 700; }
    .warn { color: #c80; font-weight: 700; }
    .err { color: #d33; font-weight: 700; }
    #logs { max-height: 300px; overflow: auto; white-space: pre-wrap; background: #0001; padding: 8px; border-radius: 8px; }
    table { width: 100%; border-collapse: collapse; }
    td,th { border-bottom: 1px solid #8884; padding: 6px; text-align: left; }
    .badge { font-size: 12px; padding: 3px 7px; border-radius: 12px; border: 1px solid #8888; }
  </style>
</head>
<body>
  <h2>Smart Door Security Simulator (ESP32)</h2>
  <div class="card">
    <div><b>Note:</b> <span class="warn">SIMULATED CAMERA</span> events are software-triggered from this dashboard.</div>
    <div class="row">
      <label><input type="checkbox" id="speechOpt"> Browser speech on simulated camera events</label>
      <label><input type="checkbox" id="notifyOpt"> Browser notifications on simulated camera events</label>
    </div>
  </div>

  <div class="grid">
    <div class="card">
      <h3>System Status</h3>
      <div id="status"></div>
    </div>
    <div class="card">
      <h3>Owner Decision Panel</h3>
      <div class="row">
        <button onclick="act('ownerYes')">Owner YES</button>
        <button onclick="act('ownerNo')">Owner NO</button>
      </div>
      <div class="row">
        <input id="securityKeyInput" placeholder="Security key (fallback)">
        <button onclick="submitKey()">Submit Key</button>
      </div>
      <small>Fallback key used only after owner timeout. Max failures: 3</small>
    </div>
    <div class="card">
      <h3>Alarm / Buzzer</h3>
      <div class="row">
        <button onclick="act('silenceAlarm')">Silence Alarm</button>
        <button onclick="act('resetAlarm')">Reset Alarm</button>
      </div>
      <div class="row">
        <button onclick="act('testBuzzer')">Test Buzzer</button>
      </div>
    </div>
  </div>

  <div class="grid">
    <div class="card">
      <h3>First-run Family Registration</h3>
      <div class="row">
        <input id="newMemberName" placeholder="Family member name">
        <button onclick="registerFamily()">Register Member</button>
      </div>
      <small>Creates per-member ID with inside/outside tracking.</small>
    </div>
    <div class="card">
      <h3>Simulated Camera Detection</h3>
      <div class="row">
        <input id="unknownName" placeholder="Unknown label (optional)">
        <button onclick="simulateUnknown()">SIMULATED CAMERA: Unknown Visitor</button>
      </div>
      <small>Owner YES/NO required, then timeout fallback to security key.</small>
    </div>
    <div class="card">
      <h3>Security Settings (Demo)</h3>
      <div class="row">
        <input id="demoKey" placeholder="New demo key">
        <button onclick="setDemoKey()">Set Demo Key</button>
      </div>
      <div class="row">
        <input id="decisionTimeoutMs" type="number" min="3000" step="1000" placeholder="Decision timeout ms">
        <button onclick="setTimeoutMs()">Set Timeout</button>
      </div>
    </div>
  </div>

  <div class="card">
    <h3>Family Members</h3>
    <table>
      <thead><tr><th>ID</th><th>Name</th><th>Location</th><th>Action</th></tr></thead>
      <tbody id="familyBody"></tbody>
    </table>
  </div>

  <div class="card">
    <h3>Event Log</h3>
    <div id="logs"></div>
  </div>

<script>
let lastEventSeen = "";

function esc(s){ return (s ?? '').toString(); }

async function act(cmd, extra={}) {
  const p = new URLSearchParams({cmd, ...extra});
  const r = await fetch('/api/action', {method:'POST', headers:{'Content-Type':'application/x-www-form-urlencoded'}, body:p.toString()});
  const j = await r.json();
  if(!j.ok) alert(j.message || 'Action failed');
  await poll();
}

async function registerFamily() {
  const name = document.getElementById('newMemberName').value.trim();
  if(!name) return alert('Enter member name');
  await act('registerFamily', {name});
  document.getElementById('newMemberName').value = '';
}
async function simulateUnknown() {
  const name = document.getElementById('unknownName').value.trim();
  await act('simulateUnknown', {name});
}
async function submitKey() {
  const key = document.getElementById('securityKeyInput').value;
  await act('submitKey', {key});
}
async function setDemoKey() {
  const key = document.getElementById('demoKey').value.trim();
  if(!key) return alert('Enter new key');
  await act('setDemoKey', {key});
}
async function setTimeoutMs() {
  const ms = document.getElementById('decisionTimeoutMs').value;
  await act('setTimeoutMs', {ms});
}
async function simulateFamily(id) { await act('simulateFamily', {id: String(id)}); }

function notifyIfSupported(msg){
  if(!document.getElementById('notifyOpt').checked) return;
  if(!('Notification' in window)) return;
  if(Notification.permission === 'granted'){
    new Notification('Smart Door (Simulated Camera)', { body: msg });
  } else if (Notification.permission !== 'denied') {
    Notification.requestPermission();
  }
}
function speakIfSupported(msg){
  if(!document.getElementById('speechOpt').checked) return;
  if(!('speechSynthesis' in window)) return;
  const ut = new SpeechSynthesisUtterance(msg);
  speechSynthesis.speak(ut);
}

function flowLabel(f){
  switch(f){
    case 'IDLE': return 'Idle';
    case 'PENDING_OWNER_DECISION': return 'Waiting owner YES/NO';
    case 'WAITING_SECURITY_KEY': return 'Waiting security key';
    default: return f;
  }
}

async function poll() {
  const r = await fetch('/api/state');
  const s = await r.json();

  const status = `
    <div><b>Time:</b> ${esc(s.time)}</div>
    <div><b>IP:</b> ${esc(s.ip)} (${s.wifiConnected ? '<span class="ok">WiFi OK</span>' : '<span class="warn">WiFi offline</span>'})</div>
    <div><b>Flow:</b> ${flowLabel(s.flow)}</div>
    <div><b>Door Lock:</b> ${s.lockUnlocked ? '<span class="ok">UNLOCKED</span>' : '<span class="err">LOCKED</span>'}</div>
    <div><b>Pending Unknown ID:</b> ${s.pendingUnknownId || '-'}</div>
    <div><b>Timeout Remaining:</b> ${s.pendingRemainingMs} ms</div>
    <div><b>Unauthorized Streak:</b> ${s.unauthorizedStreak}</div>
    <div><b>Alarm:</b> ${s.alarmActive ? (s.alarmSilenced ? '<span class="warn">ACTIVE (silenced)</span>' : '<span class="err">ACTIVE</span>') : '<span class="ok">OFF</span>'}</div>
    <div><b>GPIO Sync:</b>
      <span class="badge">Relay:${s.relay?1:0}</span>
      <span class="badge">Red:${s.ledRed?1:0}</span>
      <span class="badge">Green:${s.ledGreen?1:0}</span>
      <span class="badge">Buzzer:${s.buzzer?1:0}</span>
    </div>
    <div><b>First Run Registration:</b> ${s.firstRun ? '<span class="warn">Required</span>' : '<span class="ok">Completed</span>'}</div>
  `;
  document.getElementById('status').innerHTML = status;

  const fb = document.getElementById('familyBody');
  fb.innerHTML = '';
  for(const m of s.family){
    const tr = document.createElement('tr');
    tr.innerHTML = `<td>FM${String(m.id).padStart(3,'0')}</td><td>${esc(m.name)}</td><td>${m.inside ? 'Inside' : 'Outside'}</td>
      <td><button onclick="simulateFamily(${m.id})">Simulate Scan</button></td>`;
    fb.appendChild(tr);
  }

  document.getElementById('logs').textContent = (s.logs || []).join('\n');

  if (s.lastEvent && s.lastEvent !== lastEventSeen) {
    lastEventSeen = s.lastEvent;
    if (s.lastEvent.includes('SIMULATED CAMERA')) {
      const shortMsg = 'Simulated camera detected visitor. Check owner decision panel.';
      notifyIfSupported(shortMsg);
      speakIfSupported(shortMsg);
    }
  }
}

setInterval(poll, 1000);
poll();
</script>
</body>
</html>
)HTML";

bool timeReached(unsigned long nowMs, unsigned long targetMs) {
  return (long)(nowMs - targetMs) >= 0;
}

String flowToString(FlowState f) {
  switch (f) {
    case FlowState::IDLE: return "IDLE";
    case FlowState::PENDING_OWNER_DECISION: return "PENDING_OWNER_DECISION";
    case FlowState::WAITING_SECURITY_KEY: return "WAITING_SECURITY_KEY";
    default: return "IDLE";
  }
}

String jsonEscape(const String& in) {
  String out;
  out.reserve(in.length() + 8);
  for (size_t i = 0; i < in.length(); i++) {
    char c = in[i];
    switch (c) {
      case '\"': out += "\\\""; break;
      case '\\': out += "\\\\"; break;
      case '\n': out += "\\n"; break;
      case '\r': break;
      case '\t': out += "\\t"; break;
      default: out += c; break;
    }
  }
  return out;
}

String timestampNow() {
  struct tm timeinfo;
  if (getLocalTime(&timeinfo, 10)) {
    char buf[28];
    strftime(buf, sizeof(buf), "%Y-%m-%d %H:%M:%S", &timeinfo);
    return String(buf);
  }
  return "UPTIME+" + String(millis() / 1000) + "s";
}

String makeEventId() {
  char buf[16];
  snprintf(buf, sizeof(buf), "EVT%06lu", (unsigned long)nextEventId++);
  return String(buf);
}

void pushLog(const String& msg) {
  String line = makeEventId() + " | " + timestampNow() + " | " + msg;
  eventLog.push_back(line);
  if (eventLog.size() > MAX_LOG_ENTRIES) {
    eventLog.erase(eventLog.begin());
  }
  lastEvent = line;
  Serial.println(line);
}

void chirpAck() {
  chirpUntilMs = millis() + ACK_CHIRP_MS;
}

void setOledBanner(const String& title, const String& detail, unsigned long ms) {
  oledBannerTitle = title;
  oledBannerDetail = detail;
  oledBannerUntilMs = millis() + ms;
}

FamilyMember* findMemberById(uint16_t id) {
  for (size_t i = 0; i < familyMembers.size(); i++) {
    if (familyMembers[i].id == id) return &familyMembers[i];
  }
  return nullptr;
}

FamilyMember* firstInsideMember() {
  for (size_t i = 0; i < familyMembers.size(); i++) {
    if (familyMembers[i].inside) return &familyMembers[i];
  }
  return nullptr;
}

void clearPendingUnknown() {
  pendingUnknownId = 0;
  pendingUnknownLabel = "";
  pendingDecisionStartMs = 0;
  keyFailures = 0;
  if (flowState != FlowState::IDLE) {
    flowState = FlowState::IDLE;
  }
}

void triggerAlarmIfNeeded() {
  if (unauthorizedStreak >= UNAUTHORIZED_STREAK_ALARM_THRESHOLD) {
    if (!alarmActive) {
      alarmActive = true;
      alarmSilenced = false;
      pushLog("ALARM activated due to repeated unauthorized attempts.");
    }
  }
}

void markUnauthorized(const String& reason) {
  unauthorizedStreak++;
  pushLog("Unauthorized: " + reason + " (streak=" + String(unauthorizedStreak) + ")");
  setOledBanner("ACCESS DENIED", "Unauthorized attempt", OLED_BANNER_MS);
  clearPendingUnknown();
  triggerAlarmIfNeeded();
}

void unlockDoor(const String& reason) {
  lockUnlocked = true;
  lockUnlockUntilMs = millis() + LOCK_OPEN_MS_DEFAULT;
  unauthorizedStreak = 0;
  clearPendingUnknown();
  chirpAck();
  setOledBanner("ACCESS APPROVED", "Door unlocked", OLED_BANNER_MS);
  pushLog("Door UNLOCKED: " + reason);
}

void lockDoorNow(const String& reason) {
  if (lockUnlocked) {
    lockUnlocked = false;
    pushLog("Door LOCKED: " + reason);
  }
}

void ownerApprove() {
  if (flowState != FlowState::PENDING_OWNER_DECISION) {
    pushLog("Owner YES ignored: no pending visitor.");
    return;
  }
  String uv = "UV" + String(pendingUnknownId);
  unlockDoor("Owner approved visitor " + uv + ".");
}

void ownerDeny() {
  if (flowState != FlowState::PENDING_OWNER_DECISION) {
    pushLog("Owner NO ignored: no pending visitor.");
    return;
  }
  String uv = "UV" + String(pendingUnknownId);
  markUnauthorized("Owner denied visitor " + uv + ".");
}

void beginUnknownVisitor(const String& label) {
  if (flowState != FlowState::IDLE) {
    pushLog("New unknown visitor ignored: workflow already active.");
    return;
  }
  pendingUnknownId = nextUnknownVisitorId++;
  pendingUnknownLabel = label.length() ? label : "Unknown";
  pendingDecisionStartMs = millis();
  flowState = FlowState::PENDING_OWNER_DECISION;
  chirpAck();

  String uv = "UV" + String(pendingUnknownId);
  setOledBanner("UNKNOWN VISITOR", uv, OLED_BANNER_MS);
  pushLog("SIMULATED CAMERA: Unknown visitor detected " + uv + " label=\"" + pendingUnknownLabel + "\".");
}

void submitSecurityKey(const String& key) {
  if (flowState != FlowState::WAITING_SECURITY_KEY) {
    pushLog("Security key ignored: no fallback session active.");
    return;
  }

  String uv = "UV" + String(pendingUnknownId);
  if (key == demoSecurityKey) {
    unlockDoor("Fallback security key accepted for " + uv + ".");
    return;
  }

  keyFailures++;
  chirpAck();
  pushLog("Fallback key failed for " + uv + " (" + String(keyFailures) + "/" + String(SECURITY_KEY_MAX_FAILURES) + ").");
  if (keyFailures >= SECURITY_KEY_MAX_FAILURES) {
    markUnauthorized("Security key failed max attempts for " + uv + ".");
  }
}

void handlePhysicalButtons() {
  uint8_t e = digitalRead(PIN_BTN_EXIT);
  uint8_t y = digitalRead(PIN_BTN_YES);
  uint8_t n = digitalRead(PIN_BTN_NO);

  if (e == LOW && prevExit == HIGH) {
    FamilyMember* m = firstInsideMember();
    if (m != nullptr) {
      m->inside = false;
      unlockDoor("Exit button: " + m->name + " marked Outside.");
    } else {
      unlockDoor("Exit button pressed.");
    }
  }
  if (y == LOW && prevYes == HIGH) {
    ownerApprove();
  }
  if (n == LOW && prevNo == HIGH) {
    ownerDeny();
  }

  prevExit = e;
  prevYes = y;
  prevNo = n;
}

void drawCentered(uint8_t y, const String& text) {
  int16_t w = oled.getStrWidth(text.c_str());
  int16_t x = (128 - w) / 2;
  if (x < 0) x = 0;
  oled.drawStr(x, y, text.c_str());
}

void updateOled() {
  unsigned long now = millis();
  if (!timeReached(now, lastOledDrawMs + OLED_REFRESH_MS)) return;
  lastOledDrawMs = now;

  String l1, l2, l3;

  if (alarmActive) {
    l1 = "SECURITY ALARM";
    l2 = alarmSilenced ? "ACTIVE (SILENCED)" : "ACTIVE - SOUNDING";
  } else if (!timeReached(now, oledBannerUntilMs)) {
    l1 = oledBannerTitle;
    l2 = oledBannerDetail;
  } else if (flowState == FlowState::PENDING_OWNER_DECISION) {
    l1 = "UNKNOWN VISITOR";
    l2 = "OWNER DECISION";
    l3 = "PENDING";
  } else if (flowState == FlowState::WAITING_SECURITY_KEY) {
    l1 = "ACCESS DENIED";
    l2 = "OWNER TIMEOUT";
    l3 = "ENTER SECURITY KEY";
  } else if (lockUnlocked) {
    l1 = "ACCESS APPROVED";
    l2 = "DOOR UNLOCKED";
  } else {
    l1 = "DOOR LOCKED";
    l2 = "SYSTEM READY";
  }

  oled.clearBuffer();
  oled.setFont(u8g2_font_6x12_tf);
  drawCentered(16, l1);
  if (l2.length()) drawCentered(34, l2);
  if (l3.length()) drawCentered(50, l3);

  oled.setFont(u8g2_font_5x7_tf);
  String footer = "Flow:" + flowToString(flowState);
  oled.drawStr(0, 63, footer.c_str());

  oled.sendBuffer();
}

void updateStateMachine() {
  unsigned long now = millis();

  handlePhysicalButtons();

  if (lockUnlocked && timeReached(now, lockUnlockUntilMs)) {
    lockDoorNow("Auto re-lock timeout.");
  }

  if (flowState == FlowState::PENDING_OWNER_DECISION) {
    if (timeReached(now, pendingDecisionStartMs + ownerDecisionTimeoutMs)) {
      flowState = FlowState::WAITING_SECURITY_KEY;
      keyFailures = 0;
      String uv = "UV" + String(pendingUnknownId);
      pushLog("Owner timeout for " + uv + ". Enter fallback security key.");
    }
  }

  // LED logic
  if (alarmActive) {
    outRed = ((now / 150) % 2) == 0;
    outGreen = false;
  } else if (flowState == FlowState::PENDING_OWNER_DECISION) {
    outRed = true;
    outGreen = ((now / 500) % 2) == 0;
  } else if (flowState == FlowState::WAITING_SECURITY_KEY) {
    outRed = ((now / 400) % 2) == 0;
    outGreen = false;
  } else if (lockUnlocked) {
    outRed = false;
    outGreen = true;
  } else {
    outRed = true;
    outGreen = false;
  }

  // Relay logic (active HIGH module)
  outRelay = lockUnlocked;

  // Buzzer logic
  bool alarmBuzz = alarmActive && !alarmSilenced && (((now / 250) % 2) == 0);
  bool testBuzz = (!timeReached(now, testBuzzerUntilMs)) && (((now / 120) % 2) == 0);
  bool chirpBuzz = (!timeReached(now, chirpUntilMs)) && (((now / 80) % 2) == 0);

  if (alarmBuzz) outBuzzer = true;
  else if (testBuzz) outBuzzer = true;
  else if (chirpBuzz) outBuzzer = true;
  else outBuzzer = false;

  digitalWrite(PIN_LED_RED, outRed ? HIGH : LOW);
  digitalWrite(PIN_LED_GREEN, outGreen ? HIGH : LOW);
  digitalWrite(PIN_RELAY_LOCK, outRelay ? HIGH : LOW);
  digitalWrite(PIN_BUZZER, outBuzzer ? HIGH : LOW);

  updateOled();
}

String makeStateJson() {
  String json = "{";
  json += "\"time\":\"" + jsonEscape(timestampNow()) + "\",";
  json += "\"ip\":\"" + WiFi.localIP().toString() + "\",";
  json += "\"wifiConnected\":" + String((WiFi.status() == WL_CONNECTED) ? "true" : "false") + ",";
  json += "\"firstRun\":" + String(familyMembers.empty() ? "true" : "false") + ",";
  json += "\"flow\":\"" + flowToString(flowState) + "\",";
  json += "\"lockUnlocked\":" + String(lockUnlocked ? "true" : "false") + ",";
  json += "\"relay\":" + String(outRelay ? "true" : "false") + ",";
  json += "\"ledRed\":" + String(outRed ? "true" : "false") + ",";
  json += "\"ledGreen\":" + String(outGreen ? "true" : "false") + ",";
  json += "\"buzzer\":" + String(outBuzzer ? "true" : "false") + ",";
  json += "\"alarmActive\":" + String(alarmActive ? "true" : "false") + ",";
  json += "\"alarmSilenced\":" + String(alarmSilenced ? "true" : "false") + ",";
  json += "\"unauthorizedStreak\":" + String(unauthorizedStreak) + ",";
  json += "\"pendingUnknownId\":" + String(pendingUnknownId) + ",";
  unsigned long rem = 0;
  if (flowState == FlowState::PENDING_OWNER_DECISION) {
    unsigned long now = millis();
    unsigned long endAt = pendingDecisionStartMs + ownerDecisionTimeoutMs;
    rem = timeReached(now, endAt) ? 0 : (endAt - now);
  }
  json += "\"pendingRemainingMs\":" + String(rem) + ",";
  json += "\"securityKeyFailures\":" + String(keyFailures) + ",";
  json += "\"securityKeyMaxFailures\":" + String(SECURITY_KEY_MAX_FAILURES) + ",";
  json += "\"decisionTimeoutMs\":" + String(ownerDecisionTimeoutMs) + ",";
  json += "\"demoSecurityKey\":\"" + jsonEscape(demoSecurityKey) + "\",";
  json += "\"lastEvent\":\"" + jsonEscape(lastEvent) + "\",";

  json += "\"family\":[";
  for (size_t i = 0; i < familyMembers.size(); i++) {
    if (i) json += ",";
    json += "{";
    json += "\"id\":" + String(familyMembers[i].id) + ",";
    json += "\"name\":\"" + jsonEscape(familyMembers[i].name) + "\",";
    json += "\"inside\":" + String(familyMembers[i].inside ? "true" : "false");
    json += "}";
  }
  json += "],";

  json += "\"logs\":[";
  for (size_t i = 0; i < eventLog.size(); i++) {
    if (i) json += ",";
    json += "\"" + jsonEscape(eventLog[i]) + "\"";
  }
  json += "]";

  json += "}";
  return json;
}

void sendActionResult(bool ok, const String& message) {
  String out = "{\"ok\":";
  out += ok ? "true" : "false";
  out += ",\"message\":\"" + jsonEscape(message) + "\"}";
  server.send(ok ? 200 : 400, "application/json", out);
}

void handleActionApi() {
  String cmd = server.arg("cmd");
  if (cmd.length() == 0) {
    sendActionResult(true, "Action endpoint ready.");
    return;
  }

  if (cmd == "registerFamily") {
    String name = server.arg("name");
    name.trim();
    if (name.length() == 0) return sendActionResult(false, "Name required.");
    if (familyMembers.size() >= MAX_FAMILY_MEMBERS) return sendActionResult(false, "Family member limit reached.");
    FamilyMember m;
    m.id = nextFamilyId++;
    m.name = name;
    m.inside = false;
    familyMembers.push_back(m);
    pushLog("SIMULATED CAMERA: Family registered FM" + String(m.id) + " \"" + m.name + "\" (Outside).");
    chirpAck();
    return sendActionResult(true, "Member registered.");
  }

  if (cmd == "simulateFamily") {
    uint16_t id = (uint16_t) server.arg("id").toInt();
    FamilyMember* m = findMemberById(id);
    if (!m) return sendActionResult(false, "Member not found.");

    setOledBanner("REGISTERED MEMBER VERIFIED", "FM" + String(m->id) + " " + m->name, OLED_BANNER_MS);
    if (m->inside) {
      m->inside = false;
      unlockDoor("Known member " + m->name + " (FM" + String(m->id) + ") exited.");
    } else {
      m->inside = true;
      unlockDoor("Known member " + m->name + " (FM" + String(m->id) + ") entered.");
    }
    return sendActionResult(true, "Family simulation processed.");
  }

  if (cmd == "simulateUnknown") {
    String name = server.arg("name");
    name.trim();
    beginUnknownVisitor(name);
    return sendActionResult(true, "Unknown visitor simulation sent.");
  }

  if (cmd == "ownerYes") {
    ownerApprove();
    return sendActionResult(true, "Owner YES processed.");
  }

  if (cmd == "ownerNo") {
    ownerDeny();
    return sendActionResult(true, "Owner NO processed.");
  }

  if (cmd == "submitKey") {
    String key = server.arg("key");
    submitSecurityKey(key);
    return sendActionResult(true, "Security key processed.");
  }

  if (cmd == "silenceAlarm") {
    alarmSilenced = true;
    pushLog("Alarm silenced.");
    return sendActionResult(true, "Alarm silenced.");
  }

  if (cmd == "resetAlarm") {
    alarmActive = false;
    alarmSilenced = false;
    unauthorizedStreak = 0;
    pushLog("Alarm reset.");
    return sendActionResult(true, "Alarm reset.");
  }

  if (cmd == "testBuzzer") {
    testBuzzerUntilMs = millis() + TEST_BUZZER_MS_DEFAULT;
    pushLog("Buzzer test started.");
    return sendActionResult(true, "Buzzer test started.");
  }

  if (cmd == "setDemoKey") {
    String key = server.arg("key");
    key.trim();
    if (key.length() < 1 || key.length() > 16) return sendActionResult(false, "Key length 1..16 required.");
    demoSecurityKey = key;
    pushLog("Demo security key updated.");
    return sendActionResult(true, "Demo key updated.");
  }

  if (cmd == "setTimeoutMs") {
    long ms = server.arg("ms").toInt();
    if (ms < 3000 || ms > 120000) return sendActionResult(false, "Timeout must be 3000..120000 ms.");
    ownerDecisionTimeoutMs = (unsigned long)ms;
    pushLog("Owner decision timeout updated to " + String(ownerDecisionTimeoutMs) + " ms.");
    return sendActionResult(true, "Timeout updated.");
  }

  if (cmd == "clearLog") {
    eventLog.clear();
    pushLog("Log cleared.");
    return sendActionResult(true, "Log cleared.");
  }

  sendActionResult(false, "Unknown command.");
}

void setupRoutes() {
  server.on("/", HTTP_GET, []() {
    server.send_P(200, "text/html", INDEX_HTML);
  });

  server.on("/api/state", HTTP_GET, []() {
    server.send(200, "application/json", makeStateJson());
  });

  server.on("/api/action", HTTP_ANY, handleActionApi);

  server.onNotFound([]() {
    server.send(404, "application/json", "{\"ok\":false,\"message\":\"Not found\"}");
  });
}

void setupPins() {
  pinMode(PIN_LED_RED, OUTPUT);
  pinMode(PIN_LED_GREEN, OUTPUT);
  pinMode(PIN_BUZZER, OUTPUT);
  pinMode(PIN_RELAY_LOCK, OUTPUT);

  pinMode(PIN_BTN_EXIT, INPUT_PULLUP);
  pinMode(PIN_BTN_YES, INPUT_PULLUP);
  pinMode(PIN_BTN_NO, INPUT_PULLUP);

  digitalWrite(PIN_LED_RED, LOW);
  digitalWrite(PIN_LED_GREEN, LOW);
  digitalWrite(PIN_BUZZER, LOW);
  digitalWrite(PIN_RELAY_LOCK, LOW);
}

void setupOled() {
  Wire.begin(PIN_I2C_SDA, PIN_I2C_SCL);
  oled.setI2CAddress((uint8_t)(OLED_I2C_ADDR << 1));
  oled.begin();
  oled.clearBuffer();
  oled.setFont(u8g2_font_6x12_tf);
  drawCentered(24, "SMART DOOR");
  drawCentered(42, "BOOTING...");
  oled.sendBuffer();
}

void connectWiFi() {
  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID, WIFI_PASS);
  pushLog("Connecting WiFi...");

  unsigned long start = millis();
  while (WiFi.status() != WL_CONNECTED && !timeReached(millis(), start + 12000)) {
    delay(150);
  }

  if (WiFi.status() == WL_CONNECTED) {
    pushLog("WiFi connected. IP: " + WiFi.localIP().toString());
  } else {
    pushLog("WiFi not connected (running standalone).");
  }
}

void setupTimeSync() {
  configTime(0, 0, "pool.ntp.org", "time.nist.gov");
}

void setup() {
  Serial.begin(115200);
  setupPins();
  setupOled();
  pushLog("Boot sequence started.");
  connectWiFi();
  setupTimeSync();
  setupRoutes();
  server.begin();
  pushLog("HTTP dashboard started on port 80.");
}

void loop() {
  server.handleClient();
  updateStateMachine();
}
