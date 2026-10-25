
import json
import threading
from datetime import datetime

import paho.mqtt.client as mqtt
import streamlit as st


# ==================================================
# ZENVIA CONFIGURATION
# ==================================================

BROKER = "broker.hivemq.com"
PORT = 1883

COMMAND_TOPIC = "zenvia/demo/gesture-73821"
TELEMETRY_TOPIC = "zenvia/demo/telemetry-73821"

SAFE_DISTANCE_CM = 50
MAX_EVENTS = 100

TEMP_WARNING = 75.0
VIBRATION_WARNING = 6.0


# ==================================================
# PAGE SETTINGS
# ==================================================

st.set_page_config(
    page_title="Zenvia | Industrial Monitoring",
    page_icon="🏭",
    layout="wide",
)

st.title("🏭 Zenvia Industrial Monitoring")
st.caption(
    "Industrial safety | Gesture control | Production tracking "
    "| Predictive maintenance simulation"
)


# ==================================================
# SESSION STATE
# ==================================================

if "production_count" not in st.session_state:
    st.session_state.production_count = 0

if "events" not in st.session_state:
    st.session_state.events = []

if "temperature" not in st.session_state:
    st.session_state.temperature = 38.0

if "vibration" not in st.session_state:
    st.session_state.vibration = 1.2

if "maintenance_scenario" not in st.session_state:
    st.session_state.maintenance_scenario = "Normal Operation"

if "last_snapshot" not in st.session_state:
    st.session_state.last_snapshot = None


def add_event(event_type, message):
    """Add a timestamped dashboard event."""
    event = {
        "Time": datetime.now().astimezone().strftime(
            "%d %b %Y, %I:%M:%S %p"
        ),
        "Type": event_type,
        "Event": message,
    }

    st.session_state.events.insert(0, event)
    del st.session_state.events[MAX_EVENTS:]


# ==================================================
# MQTT MONITOR
# Keep the existing broker and topics
# ==================================================

@st.cache_resource
def create_mqtt_monitor():
    state = {
        "connected": False,
        "last_command": "No command received",
        "last_command_time": None,
        "telemetry": None,
        "last_telemetry_time": None,
        "error": None,
        "events": [],
    }

    lock = threading.Lock()

    def record_event(event_type, message, timestamp):
        state["events"].insert(
            0,
            {
                "Time": timestamp.strftime(
                    "%d %b %Y, %I:%M:%S %p"
                ),
                "Type": event_type,
                "Event": message,
            },
        )
        del state["events"][MAX_EVENTS:]

    def on_connect(
        client, userdata, flags, reason_code, properties
    ):
        with lock:
            state["connected"] = (reason_code == 0)

            if reason_code == 0:
                state["error"] = None
                record_event(
                    "CONNECTION",
                    "Connected to MQTT broker",
                    datetime.now().astimezone(),
                )
            else:
                state["error"] = (
                    f"MQTT connection failed: {reason_code}"
                )

        if reason_code == 0:
            client.subscribe(COMMAND_TOPIC)
            client.subscribe(TELEMETRY_TOPIC)

    def on_disconnect(
        client, userdata, disconnect_flags,
        reason_code, properties
    ):
        with lock:
            state["connected"] = False

            if reason_code != 0:
                state["error"] = (
                    f"MQTT disconnected: {reason_code}"
                )

            record_event(
                "CONNECTION",
                f"MQTT disconnected (code {reason_code})",
                datetime.now().astimezone(),
            )

    def on_message(client, userdata, message):
        received_at = datetime.now().astimezone()

        try:
            payload = message.payload.decode(
                "utf-8"
            ).strip()

            with lock:
                if message.topic == COMMAND_TOPIC:
                    command = payload.upper()

                    state["last_command"] = command
                    state["last_command_time"] = received_at

                    record_event(
                        "COMMAND",
                        f"Gesture command received: {command}",
                        received_at,
                    )

                elif message.topic == TELEMETRY_TOPIC:
                    data = json.loads(payload)

                    if not isinstance(data, dict):
                        return

                    previous = state["telemetry"]

                    state["telemetry"] = data
                    state["last_telemetry_time"] = received_at

                    if previous is None:
                        record_event(
                            "TELEMETRY",
                            "First ESP32 telemetry received",
                            received_at,
                        )
                    else:
                        if (
                            previous.get("machine")
                            != data.get("machine")
                        ):
                            record_event(
                                "MACHINE",
                                "Machine status changed to "
                                + str(data.get("machine", "UNKNOWN")),
                                received_at,
                            )

                        if (
                            previous.get("emergency_lock")
                            != data.get("emergency_lock")
                        ):
                            record_event(
                                "SAFETY",
                                "Emergency lock changed to "
                                + str(data.get("emergency_lock")),
                                received_at,
                            )

                        try:
                            old_distance = float(
                                previous.get("distance_cm")
                            )
                            new_distance = float(
                                data.get("distance_cm")
                            )
                            threshold = float(
                                data.get(
                                    "safe_distance_cm",
                                    SAFE_DISTANCE_CM,
                                )
                            )

                            if (
                                old_distance > threshold
                                and new_distance <= threshold
                            ):
                                record_event(
                                    "SAFETY",
                                    "Distance entered unsafe zone",
                                    received_at,
                                )
                        except (TypeError, ValueError):
                            pass

        except (UnicodeDecodeError, json.JSONDecodeError):
            with lock:
                state["error"] = (
                    "Received an invalid MQTT message."
                )
                record_event(
                    "ERROR",
                    "Invalid MQTT message received",
                    received_at,
                )

    client = mqtt.Client(
        callback_api_version=mqtt.CallbackAPIVersion.VERSION2,
        client_id="zenvia_dashboard_monitor",
        protocol=mqtt.MQTTv311,
    )

    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message

    try:
        client.connect(BROKER, PORT, keepalive=60)
        client.loop_start()
    except Exception as exc:
        state["error"] = str(exc)

    return client, state, lock


client, monitor, monitor_lock = create_mqtt_monitor()


# ==================================================
# PREDICTIVE MAINTENANCE SIMULATION
# ==================================================

st.header("🔧 Predictive Maintenance Simulation")

st.info(
    "Demonstration mode: temperature and vibration are simulated. "
    "These readings do not come from physical sensors."
)

scenario = st.selectbox(
    "Choose a machine condition",
    [
        "Normal Operation",
        "Overheating",
        "Excessive Vibration",
        "Combined Fault",
    ],
    key="maintenance_scenario",
)

if st.button("▶ Run Fault Simulation", type="primary"):
    if scenario == "Normal Operation":
        temperature = 38.0
        vibration = 1.2
        message = (
            "Normal operation simulated; "
            "health readings returned to normal"
        )

    elif scenario == "Overheating":
        temperature = 82.0
        vibration = 1.5
        message = "Overheating fault scenario simulated"

    elif scenario == "Excessive Vibration":
        temperature = 42.0
        vibration = 7.2
        message = "Excessive vibration scenario simulated"

    else:
        temperature = 88.0
        vibration = 7.8
        message = "Combined overheating and vibration scenario simulated"

    st.session_state.temperature = temperature
    st.session_state.vibration = vibration

    add_event("MAINTENANCE", message)
    st.rerun()


# ==================================================
# LIVE MONITORING
# ==================================================

@st.fragment(run_every=2)
def live_monitoring():

    with monitor_lock:
        connected = monitor["connected"]
        last_command = monitor["last_command"]
        command_time = monitor["last_command_time"]

        telemetry = (
            monitor["telemetry"].copy()
            if monitor["telemetry"] is not None
            else None
        )

        telemetry_time = monitor["last_telemetry_time"]
        error = monitor["error"]
        mqtt_events = list(monitor["events"])

    # Merge MQTT events into dashboard event history
    known_events = {
        (event["Time"], event["Type"], event["Event"])
        for event in st.session_state.events
    }

    for event in reversed(mqtt_events):
        key = (
            event["Time"],
            event["Type"],
            event["Event"],
        )

        if key not in known_events:
            st.session_state.events.insert(0, event.copy())
            known_events.add(key)

    del st.session_state.events[MAX_EVENTS:]

    if connected:
        st.success("🟢 Connected to MQTT broker")
    else:
        st.error("🔴 Not connected to MQTT broker")

    if error:
        st.caption(f"Connection/message detail: {error}")

    # Read telemetry
    machine_status = "WAITING"
    emergency_lock = None
    distance = None
    threshold = SAFE_DISTANCE_CM

    if telemetry is not None:
        machine_status = str(
            telemetry.get("machine", "UNKNOWN")
        ).upper()

        emergency_lock = telemetry.get("emergency_lock")

        try:
            distance = float(telemetry.get("distance_cm"))
        except (TypeError, ValueError):
            distance = None

        try:
            threshold = float(
                telemetry.get(
                    "safe_distance_cm",
                    SAFE_DISTANCE_CM,
                )
            )
        except (TypeError, ValueError):
            threshold = SAFE_DISTANCE_CM

    # --------------------------------------------------
    # MACHINE OVERVIEW
    # --------------------------------------------------

    st.divider()
    st.subheader("📊 Live Machine Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Machine Status", machine_status)

    with col2:
        st.metric(
            "Measured Distance",
            f"{distance:.1f} cm" if distance is not None
            else "No reading",
        )

    with col3:
        lock_status = (
            "ACTIVE" if emergency_lock is True
            else "INACTIVE" if emergency_lock is False
            else "UNKNOWN"
        )
        st.metric("Emergency Lock", lock_status)

    with col4:
        st.metric(
            "Production Count",
            st.session_state.production_count,
        )

    # --------------------------------------------------
    # MACHINE HEALTH
    # --------------------------------------------------

    st.divider()
    st.subheader("🩺 Machine Health")

    health1, health2, health3 = st.columns(3)

    with health1:
        if distance is None:
            st.warning("📏 Proximity: UNAVAILABLE")
        elif distance <= threshold:
            st.error("🔴 Proximity: UNSAFE")
        else:
            st.success("🟢 Proximity: SAFE")

    with health2:
        if emergency_lock is True:
            st.error("🚨 Emergency system: LOCKED")
        elif emergency_lock is False:
            st.success("🛡️ Emergency system: READY")
        else:
            st.warning("Emergency state unavailable")

    with health3:
        if machine_status == "RUNNING":
            st.success("⚙️ Machine: RUNNING")
        elif machine_status == "STOPPED":
            st.warning("⚙️ Machine: STOPPED")
        else:
            st.info("Machine status unavailable")

    st.caption(
        "The following temperature and vibration values are "
        "simulated for demonstration purposes only."
    )

    temperature = st.session_state.temperature
    vibration = st.session_state.vibration

    temp_col, vibration_col = st.columns(2)

    with temp_col:
        st.metric(
            "🌡️ Simulated Temperature",
            f"{temperature:.1f} °C",
        )

        if temperature >= TEMP_WARNING:
            st.error("High-temperature warning")
        else:
            st.success("Temperature within demo threshold")

    with vibration_col:
        st.metric(
            "📳 Simulated Vibration",
            f"{vibration:.1f} mm/s",
        )

        if vibration >= VIBRATION_WARNING:
            st.error("High-vibration warning")
        else:
            st.success("Vibration within demo threshold")

    # --------------------------------------------------
    # HEALTH ASSESSMENT
    # --------------------------------------------------

    st.subheader("🔍 Maintenance Assessment")

    temperature_high = temperature >= TEMP_WARNING
    vibration_high = vibration >= VIBRATION_WARNING

    if temperature_high and vibration_high:
        st.error(
            "🔴 CRITICAL DEMO SCENARIO: High temperature and "
            "high vibration detected together. Inspect the "
            "simulated machine before continuing."
        )
        st.write(
            "**Suggested action:** Stop the demonstration and "
            "inspect the simulated temperature and vibration causes."
        )

    elif temperature_high:
        st.warning(
            "🟠 HIGH TEMPERATURE: The simulated temperature "
            "exceeds the configured warning threshold."
        )
        st.write(
            "**Suggested action:** Inspect simulated cooling "
            "and temperature conditions."
        )

    elif vibration_high:
        st.warning(
            "🟠 HIGH VIBRATION: The simulated vibration "
            "exceeds the configured warning threshold."
        )
        st.write(
            "**Suggested action:** Investigate possible simulated "
            "imbalance, looseness or mechanical wear."
        )

    else:
        st.success(
            "🟢 SIMULATED HEALTH NORMAL: No temperature or "
            "vibration warning is active."
        )

    st.caption(
        "This is threshold-based fault demonstration, not an AI "
        "failure prediction model. Thresholds are illustrative "
        "and are not validated for a specific machine."
    )

    # --------------------------------------------------
    # PRODUCTION TRACKING
    # --------------------------------------------------

    st.divider()
    st.subheader("📦 Production Tracking")

    st.caption(
        "Demo counter only. Record an item manually after a "
        "simulated production cycle."
    )

    prod1, prod2 = st.columns(2)

    with prod1:
        if st.button("➕ Record Completed Item"):
            st.session_state.production_count += 1

            add_event(
                "PRODUCTION",
                "Completed item recorded. Total: "
                f"{st.session_state.production_count}",
            )
            st.rerun()

    with prod2:
        if st.button("↩️ Reset Production Count"):
            st.session_state.production_count = 0

            add_event(
                "PRODUCTION",
                "Production counter reset to zero",
            )
            st.rerun()

    # --------------------------------------------------
    # GESTURE AND TELEMETRY DETAILS
    # --------------------------------------------------

    st.divider()
    st.subheader("✋ Gesture & Sensor Details")

    detail1, detail2 = st.columns(2)

    with detail1:
        st.write("**Last gesture command:**", last_command)

        if command_time:
            st.caption(
                "Received: "
                + command_time.strftime(
                    "%d %b %Y, %I:%M:%S %p"
                )
            )

    with detail2:
        st.write("**Safety threshold:**", f"{threshold:.1f} cm")

        if telemetry_time:
            st.caption(
                "Last ESP32 telemetry: "
                + telemetry_time.strftime(
                    "%d %b %Y, %I:%M:%S %p"
                )
            )
        else:
            st.caption("Waiting for ESP32 telemetry")

    # --------------------------------------------------
    # SAFETY ALERTS
    # --------------------------------------------------

    st.divider()
    st.subheader("🚨 Safety Alerts")

    alerts = []

    if telemetry is None:
        alerts.append("Waiting for ESP32 telemetry.")

    else:
        if emergency_lock is True:
            alerts.append("Emergency lock is ACTIVE.")

        if distance is None:
            alerts.append("Distance reading unavailable.")

        elif distance <= threshold:
            alerts.append(
                f"Unsafe proximity: {distance:.1f} cm. "
                f"Required distance is greater than {threshold:.1f} cm."
            )

        if machine_status == "STOPPED" and not alerts:
            alerts.append(
                "Machine is stopped. Check commands and safety conditions."
            )

    if temperature_high:
        alerts.append(
            "SIMULATED temperature warning: "
            f"{temperature:.1f} °C."
        )

    if vibration_high:
        alerts.append(
            "SIMULATED vibration warning: "
            f"{vibration:.1f} mm/s."
        )

    if alerts:
        for alert in alerts:
            st.warning("⚠️ " + alert)
    else:
        st.success(
            "No active alerts based on available readings."
        )

    # --------------------------------------------------
    # EVENT HISTORY
    # --------------------------------------------------

    st.divider()
    st.subheader("🕒 Event History")

    if st.session_state.events:
        st.dataframe(
            st.session_state.events,
            use_container_width=True,
            hide_index=True,
        )

        if st.button("🗑️ Clear Displayed Event History"):
            st.session_state.events = []
            st.rerun()

    else:
        st.info(
            "Events will appear as commands, machine changes, "
            "production actions and simulations occur."
        )

    # --------------------------------------------------
    # CONNECTION DETAILS
    # --------------------------------------------------

    with st.expander("🔧 MQTT Connection Details"):
        st.write("Broker:", f"{BROKER}:{PORT}")
        st.write("Command topic:", COMMAND_TOPIC)
        st.write("Telemetry topic:", TELEMETRY_TOPIC)

        st.caption(
            "This demonstration uses a public MQTT broker. "
            "Do not use it for real machine safety or industrial control."
        )


live_monitoring()
