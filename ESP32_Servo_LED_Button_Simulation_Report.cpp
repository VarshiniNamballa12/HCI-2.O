#include <Arduino.h>
#include <WiFi.h>
#include <WebServer.h>
#include <ESP32Servo.h>
#include "config.h"

enum class ParcelState {
  CLOSED_LOCKED,
  WAITING_OWNER,
  APPROVED_OPEN,
  REJECTED_CLOSED
};

WebServer server(80);
Servo lockServo;

ParcelState g_state = ParcelState::CLOSED_LOCKED;
bool g_redLedOn = false;
bool g_greenLedOn = false;
bool g_redBlinkPhase = true;
unsigned long g_lastBlinkToggleMs = 0;
bool g_btnPrev = HIGH;
bool g_servoReady = false;

const char PAGE_HTML[] PROGMEM = R"rawliteral(
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>SMART PARCEL BOX</title>
  <style>
    :root{--bg:#0f172a;--card:#111827;--text:#e5e7eb;--muted:#9ca3af;--ok:#22c55e;--bad:#ef4444;--accent:#38bdf8;}
    *{box-sizing:border-box;font-family:Arial,sans-serif}
    body{margin:0;background:var(--bg);color:var(--text)}
    .wrap{max-width:980px;margin:0 auto;padding:16px}
    h1{text-align:center;margin:8px 0 18px 0;color:var(--accent)}
    .grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px}
    .card{background:var(--card);border-radius:12px;padding:14px;box-shadow:0 4px 18px rgba(0,0,0,.25)}
    .card h2{margin:0 0 12px 0;font-size:1.05rem}
    .btns{display:flex;gap:8px;flex-wrap:wrap}
    button{border:none;border-radius:10px;padding:10px 14px;color:white;font-weight:700;cursor:pointer}
    .open{background:#0ea5e9}.close{background:#64748b}.yes{background:var(--ok)}.no{background:var(--bad)}
    button:active{transform:translateY(1px)}
    .kv{display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid #1f2937}
    .dot{display:inline-block;width:10px;height:10px;border-radius:999px;margin-right:6px}
    .on{background:#22c55e}.off{background:#6b7280}.redon{background:#ef4444}
    #result{margin-top:10px;color:#fbbf24;min-height:1.2em}
    .small{color:var(--muted);font-size:.9rem}
  </style>
</head>
<body>
  <div class="wrap">
    <h1>SMART PARCEL BOX</h1>
    <div class="grid">
      <div class="card">
        <h2>DELIVERY PERSON</h2>
        <div class="btns">
          <button class="open" onclick="sendCmd('OPEN')">OPEN</button>
          <button class="close" onclick="sendCmd('CLOSE')">CLOSE</button>
        </div>
      </div>
      <div class="card">
        <h2>OWNER</h2>
        <div class="btns">
          <button class="yes" onclick="sendCmd('YES')">YES</button>
          <button class="no" onclick="sendCmd('NO')">NO</button>
        </div>
      </div>
      <div class="card" style="grid-column:1/-1">
        <h2>SHARED STATUS</h2>
        <div class="kv"><span>State</span><strong id="state">-</strong></div>
        <div class="kv"><span>Request State</span><strong id="request">-</strong></div>
        <div class="kv"><span>Box State</span><strong id="box">-</strong></div>
        <div class="kv"><span>Red Light</span><strong id="red">-</strong></div>
        <div class="kv"><span>Green Light</span><strong id="green">-</strong></div>
        <div class="kv"><span>Device IP</span><strong id="ip">-</strong></div>
        <div id="result"></div>
        <div class="small">Auto-refresh from /api/status every 1s</div>
      </div>
    </div>
  </div>
<script>
async function sendCmd(cmd){
  try{
    const res = await fetch('/api/command', {
      method:'POST',
      headers:{'Content-Type':'application/x-www-form-urlencoded'},
      body:'cmd='+encodeURIComponent(cmd)
    });
    const js = await res.json();
    render(js);
    document.getElementById('result').textContent = js.message || (js.success ? 'OK' : 'Command failed');
  }catch(e){
    document.getElementById('result').textContent = 'Network error while sending command';
  }
}
async function refreshStatus(){
  try{
    const res = await fetch('/api/status');
    const js = await res.json();
    render(js);
  }catch(e){}
}
function render(s){
  if(!s) return;
  document.getElementById('state').textContent = s.state || '-';
  document.getElementById('request').textContent = s.request_state || '-';
  document.getElementById('box').textContent = s.box_state || '-';
  document.getElementById('red').textContent = (s.red_light || '-') + (s.red_mode ? (' (' + s.red_mode + ')') : '');
  document.getElementById('green').textContent = s.green_light || '-';
  document.getElementById('ip').textContent = s.ip || '-';
}
setInterval(refreshStatus, 1000);
refreshStatus();
</script>
</body>
</html>
)rawliteral";

static const char* stateToString(ParcelState s) {
  switch (s) {
    case ParcelState::CLOSED_LOCKED:   return "CLOSED_LOCKED";
    case ParcelState::WAITING_OWNER:   return "WAITING_OWNER";
    case ParcelState::APPROVED_OPEN:   return "APPROVED_OPEN";
    case ParcelState::REJECTED_CLOSED: return "REJECTED_CLOSED";
    default:                           return "UNKNOWN";
  }
}

static bool isPendingRequest() {
  return g_state == ParcelState::WAITING_OWNER;
}

static bool isBoxOpen() {
  return g_state == ParcelState::APPROVED_OPEN;
}

static String jsonEscape(const String& in) {
  String out;
  out.reserve(in.length() + 8);
  for (size_t i = 0; i < in.length(); i++) {
    const char c = in[i];
    if (c == '\\' || c == '"') out += '\\';
    out += c;
  }
  return out;
}

static void setServoLocked(bool locked) {
  if (!g_servoReady) return;
  lockServo.write(locked ? SERVO_LOCK_ANGLE : SERVO_UNLOCK_ANGLE);
}

static void updateLeds() {
  const unsigned long now = millis();

  switch (g_state) {
    case ParcelState::CLOSED_LOCKED:
    case ParcelState::REJECTED_CLOSED:
      g_redLedOn = true;
      g_greenLedOn = false;
      break;

    case ParcelState::WAITING_OWNER:
      if (now - g_lastBlinkToggleMs >= RED_BLINK_INTERVAL_MS) {
        g_lastBlinkToggleMs = now;
        g_redBlinkPhase = !g_redBlinkPhase;
      }
      g_redLedOn = g_redBlinkPhase;
      g_greenLedOn = false;
      break;

    case ParcelState::APPROVED_OPEN:
      g_redLedOn = false;
      g_greenLedOn = true;
      break;
  }

  digitalWrite(PIN_LED_RED, g_redLedOn ? HIGH : LOW);
  digitalWrite(PIN_LED_GREEN, g_greenLedOn ? HIGH : LOW);
}

static void applyStateOutputs() {
  if (g_state == ParcelState::APPROVED_OPEN) {
    setServoLocked(false);
  } else {
    setServoLocked(true);
  }
  updateLeds();
}

static void transitionTo(ParcelState next, const String& reason) {
  if (g_state == next) return;
  Serial.printf("[STATE] %s -> %s | %s\n", stateToString(g_state), stateToString(next), reason.c_str());
  g_state = next;
  g_redBlinkPhase = true;
  g_lastBlinkToggleMs = millis();
  applyStateOutputs();
}

static void appendStatusFields(String& json) {
  updateLeds();
  json += "\"state\":\"";
  json += stateToString(g_state);
  json += "\",\"request_state\":\"";
  json += (isPendingRequest() ? "PENDING" : "NONE");
  json += "\",\"box_state\":\"";
  json += (isBoxOpen() ? "OPEN" : "CLOSED");
  json += "\",\"red_light\":\"";
  json += (g_redLedOn ? "ON" : "OFF");
  json += "\",\"red_mode\":\"";
  if (g_state == ParcelState::WAITING_OWNER) json += "BLINK";
  else if (g_redLedOn) json += "SOLID";
  else json += "OFF";
  json += "\",\"green_light\":\"";
  json += (g_greenLedOn ? "ON" : "OFF");
  json += "\",\"ip\":\"";
  json += WiFi.localIP().toString();
  json += "\"";
}

static void sendStatusJson() {
  String json = "{";
  appendStatusFields(json);
  json += "}";
  server.send(200, "application/json", json);
}

static void sendCommandJson(int code, bool success, const String& cmd, const String& message) {
  String json = "{";
  json += "\"success\":";
  json += (success ? "true" : "false");
  json += ",\"command\":\"";
  json += jsonEscape(cmd);
  json += "\",\"message\":\"";
  json += jsonEscape(message);
  json += "\",";
  appendStatusFields(json);
  json += "}";

  server.send(code, "application/json", json);
}

static String normalizedCommand() {
  String cmd = server.arg("cmd"); // query or form field
  if (cmd.length() == 0) {
    cmd = server.arg("command");   // tolerate alternate field name
  }
  if (cmd.length() == 0 && server.args() > 0) {
    cmd = server.arg(0);           // fallback: first provided argument
  }
  if (cmd.length() == 0 && server.hasArg("plain")) {
    cmd = server.arg("plain");     // raw body (e.g. "OPEN")
  }
  cmd.trim();
  cmd.toUpperCase();
  return cmd;
}

static void handleCommand() {
  const String cmd = normalizedCommand();
  Serial.printf("[CMD] Received: %s\n", cmd.c_str());

  if (cmd.length() == 0) {
    sendCommandJson(400, false, "", "Missing command. Use OPEN, CLOSE, YES, NO");
    return;
  }

  if (cmd == "OPEN") {
    if (isPendingRequest()) {
      sendCommandJson(409, false, cmd, "OPEN rejected: request already pending");
      return;
    }
    if (isBoxOpen()) {
      sendCommandJson(409, false, cmd, "OPEN rejected: box already open");
      return;
    }
    transitionTo(ParcelState::WAITING_OWNER, "Delivery OPEN request");
    sendCommandJson(200, true, cmd, "OPEN accepted: waiting owner decision");
    return;
  }

  if (cmd == "YES") {
    if (!isPendingRequest()) {
      sendCommandJson(409, false, cmd, "YES rejected: no pending request");
      return;
    }
    transitionTo(ParcelState::APPROVED_OPEN, "Owner approved");
    sendCommandJson(200, true, cmd, "YES accepted: box unlocked/open");
    return;
  }

  if (cmd == "NO") {
    if (!isPendingRequest()) {
      sendCommandJson(409, false, cmd, "NO rejected: no pending request");
      return;
    }
    transitionTo(ParcelState::REJECTED_CLOSED, "Owner rejected");
    sendCommandJson(200, true, cmd, "NO accepted: box stays closed");
    return;
  }

  if (cmd == "CLOSE") {
    if (!isBoxOpen()) {
      sendCommandJson(409, false, cmd, "CLOSE rejected: box already closed");
      return;
    }
    transitionTo(ParcelState::CLOSED_LOCKED, "Close command");
    sendCommandJson(200, true, cmd, "CLOSE accepted: box locked");
    return;
  }

  sendCommandJson(400, false, cmd, "Unknown command. Use OPEN, CLOSE, YES, NO");
}

static void handleRoot() {
  server.send_P(200, "text/html", PAGE_HTML);
}

static void handleNotFound() {
  server.send(404, "application/json", "{\"success\":false,\"message\":\"Not found\"}");
}

static void setupWiFi() {
  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID, WIFI_PASS);

  Serial.printf("[WIFI] Connecting to %s", WIFI_SSID);
  const unsigned long start = millis();
  while (WiFi.status() != WL_CONNECTED && (millis() - start) < WIFI_CONNECT_TIMEOUT_MS) {
    delay(250);
    Serial.print(".");
  }
  Serial.println();

  if (WiFi.status() == WL_CONNECTED) {
    Serial.printf("[WIFI] Connected. IP: %s\n", WiFi.localIP().toString().c_str());
  } else {
    Serial.println("[WIFI] Connection timeout. Web server may be unreachable.");
  }
}

static void setupServer() {
  server.on("/", HTTP_GET, handleRoot);
  server.on("/api/status", HTTP_GET, sendStatusJson);
  server.on("/api/command", HTTP_POST, handleCommand);
  server.on("/api/command", HTTP_GET, handleCommand); // handy for manual browser tests
  server.onNotFound(handleNotFound);
  server.begin();
  Serial.println("[HTTP] Server started on port 80");
}

static void handleDoorButton() {
  const bool btn = digitalRead(PIN_DOOR_BUTTON);
  if (btn == LOW && g_btnPrev == HIGH) {
    Serial.println("[BTN] Door button pressed");
    if (isBoxOpen()) {
      transitionTo(ParcelState::CLOSED_LOCKED, "Door button pressed while open");
      Serial.println("[BTN] Auto-closed and locked");
    } else {
      Serial.println("[BTN] Ignored (box not open)");
    }
  }
  g_btnPrev = btn;
}

void setup() {
  Serial.begin(115200);
  delay(200);

  pinMode(PIN_LED_RED, OUTPUT);
  pinMode(PIN_LED_GREEN, OUTPUT);
  pinMode(PIN_DOOR_BUTTON, INPUT_PULLUP);

  ESP32PWM::allocateTimer(0);
  lockServo.setPeriodHertz(50);
  lockServo.attach(PIN_SERVO_SIG, SERVO_MIN_US, SERVO_MAX_US);
  g_servoReady = lockServo.attached();

  Serial.printf("[SERVO] %s on pin %d\n", g_servoReady ? "Attached" : "Not attached", PIN_SERVO_SIG);

  transitionTo(ParcelState::CLOSED_LOCKED, "Boot");
  setupWiFi();
  setupServer();
}

void loop() {
  server.handleClient();
  handleDoorButton();
  updateLeds();
}
