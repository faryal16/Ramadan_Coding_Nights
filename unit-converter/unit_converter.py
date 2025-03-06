# 🚀 Import Libraries
import streamlit as st

# 📌 Store Conversion History
if "history" not in st.session_state:
    st.session_state.history = []

# 🎯 Define Functions
def convert_units(value, unit_from, unit_to):
    conversions = {
        "meters_kilometers": 0.001,  # 1 meter = 0.001 kilometers
        "kilometers_meters": 1000,   # 1 kilometer = 1000 meters
        "grams_kilograms": 0.001,    # 1 gram = 0.001 kilograms
        "kilograms_grams": 1000,     # 1 kilogram = 1000 grams
    }
    
    key = f"{unit_from}_{unit_to}"  # Generate a unique key for the conversion
    
    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    elif unit_from == unit_to:
        return value
    else:
        return "❌ Conversion not supported"

# 🎨 UI Setup
st.title("🔢 Unit Converter")

value = st.number_input("📝 Enter the value to convert:", min_value=1.0, step=1.0)
unit_from = st.selectbox("📌 Convert from:", ["meters", "kilometers", "grams", "kilograms"])
unit_to = st.selectbox("🎯 Convert to:", ["meters", "kilometers", "grams", "kilograms"])

if st.button("🔄 Convert"):
    result = convert_units(value, unit_from, unit_to)
    
    if isinstance(result, (int, float)):  # Only store valid conversions
        st.session_state.history.append(f"{value} {unit_from} → {result} {unit_to}")
    
    st.write(f"✅ Converted Value: {result}")

# 📊 Summary Option
if st.checkbox("📋 Show Summary"):
    st.write("""
    - Supports conversions between meters, kilometers, grams, and kilograms.
    - Converts using predefined conversion factors.
    - Prevents unsupported conversions and same-unit selections.
    """)

# 🕒 Show Conversion History
if st.checkbox("📜 Show Conversion History"):
    if st.session_state.history:
        st.write("### 🔄 Previous Conversions:")
        for item in st.session_state.history[-5:]:  # Show last 5 conversions
            st.write(f"- {item}")
    else:
        st.write("🚫 No conversions yet.")
