#include <Arduino.h>
#include <Wire.h>
#include <U8g2lib.h>
#include <DHT.h>
#include "config.h"

#define DHTTYPE DHT22

DHT dht(PIN_DHT, DHTTYPE);
U8G2_SSD1306_128X64_NONAME_1_HW_I2C oled(U8G2_R0, U8X8_PIN_NONE);

float lastTempC = NAN;
float lastHumidity = NAN;
bool motionDetected = false;

unsigned long lastDhtReadMs = 0;
unsigned long lastDisplayMs = 0;
unsigned long lastSerialMs = 0;

void applyOutputs(bool motion) {
  digitalWrite(PIN_RELAY, motion ? HIGH : LOW);
  digitalWrite(PIN_BUZZER, motion ? HIGH : LOW);
  digitalWrite(PIN_LED_RED, motion ? HIGH : LOW);
  digitalWrite(PIN_LED_GREEN, motion ? LOW : HIGH);
}

void readDhtIfDue() {
  const unsigned long now = millis();
  if (now - lastDhtReadMs < DHT_READ_INTERVAL_MS) return;
  lastDhtReadMs = now;

  float t = dht.readTemperature();
  float h = dht.readHumidity();

  if (!isnan(t)) lastTempC = t;
  if (!isnan(h)) lastHumidity = h;
}

void drawDisplay() {
  char line1[24];
  char line2[24];
  char line3[24];

  snprintf(line1, sizeof(line1), "Motion: %s", motionDetected ? "DETECTED" : "NONE");

  if (isnan(lastTempC)) {
    snprintf(line2, sizeof(line2), "Temp: --.- C");
  } else {
    snprintf(line2, sizeof(line2), "Temp: %.1f C", lastTempC);
  }

  if (isnan(lastHumidity)) {
    snprintf(line3, sizeof(line3), "Hum : --.- %%");
  } else {
    snprintf(line3, sizeof(line3), "Hum : %.1f %%", lastHumidity);
  }

  oled.firstPage();
  do {
    oled.setFont(u8g2_font_6x12_tf);
    oled.drawStr(0, 14, "Room Human Detection");
    oled.drawHLine(0, 18, 128);
    oled.drawStr(0, 34, line1);
    oled.drawStr(0, 48, line2);
    oled.drawStr(0, 62, line3);
  } while (oled.nextPage());
}

void printStatus() {
  Serial.print("Motion: ");
  Serial.print(motionDetected ? "DETECTED" : "NONE");
  Serial.print(" | Temp: ");
  if (isnan(lastTempC)) Serial.print("--.-");
  else Serial.print(lastTempC, 1);
  Serial.print(" C | Humidity: ");
  if (isnan(lastHumidity)) Serial.print("--.-");
  else Serial.print(lastHumidity, 1);
  Serial.println(" %");
}

void setup() {
  Serial.begin(SERIAL_BAUDRATE);

  pinMode(PIN_PIR, INPUT);
  pinMode(PIN_RELAY, OUTPUT);
  pinMode(PIN_BUZZER, OUTPUT);
  pinMode(PIN_LED_GREEN, OUTPUT);
  pinMode(PIN_LED_RED, OUTPUT);

  applyOutputs(false);

  dht.begin();

  Wire.begin(PIN_I2C_SDA, PIN_I2C_SCL);
  oled.setI2CAddress(OLED_I2C_ADDRESS << 1);
  oled.begin();

  drawDisplay();
  printStatus();
}

void loop() {
  const unsigned long now = millis();

  bool currentMotion = (digitalRead(PIN_PIR) == HIGH);
  if (currentMotion != motionDetected) {
    motionDetected = currentMotion;
    applyOutputs(motionDetected);
    printStatus();
  }

  readDhtIfDue();

  if (now - lastDisplayMs >= DISPLAY_INTERVAL_MS) {
    lastDisplayMs = now;
    drawDisplay();
  }

  if (now - lastSerialMs >= SERIAL_INTERVAL_MS) {
    lastSerialMs = now;
    printStatus();
  }
}
