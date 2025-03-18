import requests
import streamlit as st
import random
import pandas as pd

# Initialize session state for search history
if 'history' not in st.session_state:
    st.session_state.history = []

# Function to get weather data
def get_weather(city):
    api_key = "ef25b7653a1c0d03e4e316aa9c0d954c"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data['cod'] != 200:
            st.error(f"Error: {data['message']}")
            return None
    except requests.exceptions.RequestException as err:
        st.error(f"❌Error fetching data: {err}")
        return None
    
    # Extract relevant weather information
    weather_info = {
        "City": city,
        "Description": data['weather'][0]['description'].title(),
        "Temperature": round(data['main']['temp'] - 273.15, 2),  # Convert Kelvin to Celsius
        "Humidity": data['main']['humidity'],
        "Pressure": data['main']['pressure']
    }
    
    # Append to history
    st.session_state.history.append(weather_info)
    return weather_info

# UI Setup
col1, col2 = st.columns([1, 1])

with col1:
    st.title("🌍 Real-Time Weather App")
    st.write("Get up-to-date weather details for any city around the world! 📊")

with col2:
    st.image(
        "https://media.istockphoto.com/id/2186489699/photo/tropical-storm-in-u-s.jpg?s=612x612&w=0&k=20&c=GcZERMrDlE7BP0HRf7RtCJfAFTZoIjwyE5Uv5Na9PLs=",
        use_container_width=True,
    )
st.write("---")

# Get user input
city = st.text_input("Enter City Name 📍")
if st.button("📊 Get Weather"):
    if city.strip():
        weather_data = get_weather(city)
        if weather_data:
            st.subheader(f"🌆 Weather in {city} ☀️")
            st.write(f"**🌬️ Condition:** {weather_data['Description']}")
            st.write(f"**🌡️ Temperature:** {weather_data['Temperature']}°C")
            st.write(f"**💧 Humidity:** {weather_data['Humidity']}%")
            st.write(f"**💨 Pressure:** {weather_data['Pressure']} hPa")

           

            # Random success message
            messages = [
                "Stay prepared for the day! 🚀",
                "Looks like a great day ahead! 🌈",
                "Don't forget your umbrella ☔ if needed!",
                "Enjoy the sunshine! 🌞",
                "Keep an eye on changing weather conditions! 🔄"
            ]
            st.success(random.choice(messages))

             # Bar chart visualization
            df = pd.DataFrame({
                "Metric": ["Temperature (°C)", "Humidity (%)", "Pressure (hPa)"],
                "Value": [weather_data['Temperature'], weather_data['Humidity'], weather_data['Pressure']]
            })
            st.bar_chart(df.set_index("Metric"))
    else:
        st.error("Please enter a valid city name! ⚠️")

# Display search history
if st.session_state.history:
    st.write("---")
    st.subheader("📜 Search History")
    history_df = pd.DataFrame(st.session_state.history)
    st.table(history_df)


