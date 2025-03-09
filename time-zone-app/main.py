import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

# 🎨 Custom Styling
st.markdown(
    """
    <style>
        .big-font { font-size:24px !important; font-weight:bold; }
        .emoji { font-size:30px; }
        .stButton button { background-color: #4CAF50; color: white; font-size: 18px; }
    </style>
    """,
    unsafe_allow_html=True,
)

# 🌍 List of Available Time Zones
TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata",
]

# 🕰️ App Title
st.title("🌎 Time Zone Converter ⏳")

# 📌 Multi-select dropdown for choosing time zones
selected_timezone = st.multiselect(
    "🌟 Select Timezones", TIME_ZONES, default=["UTC", "Asia/Karachi"]
)

# ⏲️ Display current time for selected time zones
st.subheader("🕒 Current Time in Selected Timezones")
for tz in selected_timezone:
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.write(f"🌍 **{tz}**: 🕰️ `{current_time}`")

# 🔄 Time Conversion Section
st.subheader("🔄 Convert Time Between Timezones")
current_time = st.time_input("⏰ Select Time", value=datetime.now().time())
from_tz = st.selectbox("📍 From Timezone", TIME_ZONES, index=0)
to_tz = st.selectbox("📍 To Timezone", TIME_ZONES, index=1)

# 🚀 Convert Button
if st.button("🔄 Convert Time"):
    dt = datetime.combine(datetime.today(), current_time, tzinfo=ZoneInfo(from_tz))
    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I:%M:%S %p")
    st.success(f"✅ Converted Time in {to_tz}: ⏰ `{converted_time}`")
