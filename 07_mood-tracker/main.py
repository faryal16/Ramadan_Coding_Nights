import streamlit as st
import pandas as pd
import datetime
import csv
import os

# File location
MOOD_FILE = "mood_log.csv"

# Ensure CSV file exists
if not os.path.exists(MOOD_FILE) or os.stat(MOOD_FILE).st_size == 0:
    with open(MOOD_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Mood"])  # Only two columns

# Load mood data
def load_mood_data():
    try:
        df = pd.read_csv(MOOD_FILE, usecols=[0, 1], names=["Date", "Mood"], header=0)
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        return df
    except Exception as e:
        st.error(f"Error loading mood data: {e}")
        return pd.DataFrame(columns=["Date", "Mood"])

# Save mood data
def save_mood_data(date, mood):
    with open(MOOD_FILE, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, mood])

# 🎨 UI
st.title("Mood Tracker 😊")
st.write("---")

# Name Input
user_name = st.text_input("😎 What's your good Name?", placeholder="Enter your name")

# 📅 Today's Date
today = datetime.date.today()

# 🎭 Mood Selection
mood_options = {
    "😊 Happy": "Happy",
    "😢 Sad": "Sad",
    "😡 Angry": "Angry",
    "😐 Neutral": "Neutral",
    "😴 Sleepy": "Sleepy",
    "🤩 Excited": "Excited",
    "😔 Tired": "Tired",
    "🤯 Stressed": "Stressed"
}
mood = st.selectbox("Select your mood", list(mood_options.keys()))

# 🌟 Mood-Based Messages
mood_messages = {
    "Happy": "🌞 Keep spreading joy! Happiness is contagious. 😃",
    "Sad": "💙 It's okay to feel sad. Take a deep breath, talk to a friend, or do something that makes you happy. 😊",
    "Angry": "🔥 Take a moment to breathe deeply. Anger is temporary, but your actions matter. Stay calm. 💆‍♂️",
    "Neutral": "🤔 Feeling neutral? Try something new today! A small adventure can bring excitement. 🚀",
    "Sleepy": "😴 Get some rest! Your body and mind deserve a good recharge. 💤",
    "Excited": "🎉 Woohoo! Keep that energy up and make the most of today! 🚀",
    "Tired": "😔 Take it easy today. A short break, some fresh air, or a quick nap can help. ☕",
    "Stressed": "💆 Deep breaths! Prioritize tasks, take a break, and remind yourself that you got this! 💪"
}

# 📝 Log Mood
if st.button("Log Mood"):
    save_mood_data(today, mood_options[mood])
    st.success(f" {user_name} Your mood has been logged successfully!")
    
    # Show motivational message **after** logging mood
    st.info(mood_messages[mood_options[mood]])

st.write("---")
# 📊 Load and Display Mood Data
data = load_mood_data()

if data.empty:
    st.warning("⚠️ No mood data available. Log your first mood entry!")
else:
    # 📈 Mood Trends Chart
    st.subheader("📈 Mood Trends")
    mood_counts = data["Mood"].value_counts()
    if not mood_counts.empty:
        st.bar_chart(mood_counts)

    # 📅 Mood History Table
    st.subheader("📅 Mood History")
    st.dataframe(data.sort_values(by="Date", ascending=False))

# ❤️ Footer
st.write("---")
st.markdown('<h3 style="text-align:center;">Built with ❤️ by Code With Fairy</h3>', unsafe_allow_html=True)
