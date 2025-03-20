import streamlit as st
import requests

def get_random_joke(category):
    """Fetch a random joke from the Internet's best joke database! (Probably...)"""
    try:
        # Knock, knock! Who's there? A GET request!
        url = f"https://official-joke-api.appspot.com/jokes/{category}/random"
        response = requests.get(url)
        if response.status_code == 200:
            joke_data = response.json()[0] 
            return f"😂 {joke_data['setup']} \n\n👉 {joke_data['punchline']}"
        else:
            return "😢 Oops! Looks like the joke machine is on a coffee break. Try again later!"

    except:
        return "💻 Why did the programmer quit his job? \n👉 Because he didn't get arrays!!"
    
def main():
    st.title("🤣 Random Joke Generator 😂")
    st.write("Click the button below to unleash some serious laughter (or at least a pity chuckle).")

    # Joke category selection
    categories = ["general", "programming", "knock-knock"]
    category = st.selectbox("Choose a joke category:", categories)

    
    if st.button("🤣 Make Me Laugh!"):
        joke = get_random_joke(category)
        st.success(joke)
    
if __name__ == "__main__":
    main()
