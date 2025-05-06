# 🤖 Greeting Agent for Asharib Ali

A friendly AI chatbot powered by Chainlit that greets users and shares information about **Asharib Ali**.  
Built with ❤️ using Python, Chainlit, and Gemini API.

---

## ✨ Features

- 👋 Greets you with *"Salam from Asharib Ali"*
- 👋 Says goodbye with *"Allah Hafiz from Asharib Ali"*
- 📄 Fetches detailed profile info from [asharib.xyz](https://www.asharib.xyz)
- 🔐 GitHub OAuth login
- 🚫 Politely denies unrelated queries

---

## ⚙️ Tech Stack

- 🐍 Python
- 🔗 [Chainlit](https://docs.chainlit.io/)
- 🌐 Gemini API (Google AI)
- 🔐 GitHub OAuth
- 🧰 Custom Tool: `get_asharib_data`

---

## 🛠️ Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/faryal16/Ramadan_Coding_Nights/tree/main/17_advance-agent.git
   cd greeting-agent
## Create a .env file with your Gemini API key:

```bash
GEMINI_API_KEY=your_gemini_api_key
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run the app

```bash

chainlit run your_main_file.py
```
## 👤 About the Agent
The agent is trained to:

✅ Greet users
✅ Share Asharib Ali's profile info
✅ Say goodbye
❌ Avoid answering off-topic questions


