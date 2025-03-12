import streamlit as st
import random
import time
import requests

st.title("💰 Money Making Machine 💰")

# Function to generate random money
def generate_money():
    return random.randint(1, 1000)

# Function to fetch side hustle ideas
def fetch_side_hustle():
    try:
        response = requests.get('https://ramadancodingnights-simple-api.streamlit.app/side_hustles')
        if response.status_code == 200:
            hustles = response.json()
            return hustles["side_hustle"]
        else:
            return "💼 Start freelancing today!"
    except:
        return "⚠️ Something went wrong!"

# Function to fetch money-making quotes
def fetch_money_quote():
    try:
        response = requests.get('https://ramadancodingnights-simple-api.streamlit.app/money_quotes')
        if response.status_code == 200:
            money_quotes = response.json()
            return money_quotes['money_quotes']
        else:
            return "💵 Money is the root of all evil!"
    except:
        return "⚠️ Something went wrong!"

# Function to fetch motivational quotes
def fetch_quotes():
    try:
        response = requests.get("https://ramadancodingnights-simple-api.streamlit.app/motivations")
        if response.status_code == 200:
            quote = response.json()
            return quote["quote_of_the_day"]
        else:
            return "🌟 Motivation is what gets you started!"
    except:
        return "⚠️ Something went wrong!"

# Create a two-row, two-column layout with spacing
st.markdown("<br>", unsafe_allow_html=True)  # Add margin

# First row: Cash Generator & Side Hustles
col1, col2 = st.columns(2, gap="large")

with col1:
    with st.container():
        st.subheader("🎰 Instant Cash Generator 🎰")
        if st.button("💵 Generate Money 💵"):
            st.write("💰 Counting your money... 🤑")
            time.sleep(1)
            amount = generate_money()
            st.success(f"🎉 You made **${amount}**! 💸💸")

with col2:
    with st.container():
        st.subheader("💡 Side Hustles Ideas 💡")
        if st.button("🚀 Generate Hustles 🚀"):
            idea = fetch_side_hustle()
            st.success(f"📢 **{idea}**")

# Add spacing between rows
st.markdown("<br>", unsafe_allow_html=True)

# Second row: Money Motivation & Motivational Quotes
col3, col4 = st.columns(2, gap="large")

with col3:
    with st.container():
        st.subheader("📜 Money-Making Motivation 💰")
        if st.button("✨ Get Inspired ✨"):  
            quote = fetch_money_quote()
            st.info(f"📢 **{quote}** 💵")

with col4:
    with st.container():
        st.subheader("🚀 Motivational Quotes 🌟")
        if st.button("🔥 Get Motivated 🔥"):  
            quote = fetch_quotes()
            st.info(f"💡 **{quote}** 💪🔥")
