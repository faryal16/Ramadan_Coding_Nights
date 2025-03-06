import streamlit as st
import random
import string

def generate_password(length, use_digits, _use_special):
    characters = string.ascii_letters
    
    if use_digits:
        characters += string.digits
    if _use_special:
        characters += string.punctuation
    
    return ''.join(random.choice(characters) for _ in range(length))

# UI setup
st.title("🔒 Password Generater")

length = st.slider("Password length", min_value=6 , max_value=12, value=8)

use_digits = st.checkbox("Include Digits")
use_special = st.checkbox("Include Special characters")

if st.button("🔑 Create Password"):
    password = generate_password(length, use_digits, use_special)
    st.write(f"Generated Password:  :blue[{password}]")
    st.success("🎉Password successfully generated!")
    st.balloons()
    
st.write("____________")
st.write("Build with ❤ by [Code with Fairy](https://github.com/faryal16)")
    
    

