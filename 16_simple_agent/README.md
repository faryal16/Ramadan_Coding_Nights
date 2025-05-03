# Greeting Agent

This is a simple AI-powered **Greeting Agent** that uses a Gemini-compatible API through an OpenAI-like interface. It responds to user greetings with friendly, predefined messages.

## 💡 What This Script Does

- Loads an API key from a `.env` file
- Connects to Gemini's API using an OpenAI-compatible wrapper
- Sets up a chat model (`gemini-2.0-flash`)
- Creates an agent with fixed greeting instructions
- Takes user input from the terminal
- Returns a greeting based on user input

## 🧠 Agent Behavior

The agent responds based on input:

- **"hi"** → `Salam from Asharib Ali`
- **"bye"** → `Allah Hafiz from Asharib Ali`
- **Anything else** → `Asharib is here just for greeting, I can't answer anything else, sorry.`

## ▶️ Example

```bash
$ python greet_agent.py
Please enter your question: hi
Salam from Asharib Ali
```

## 📝 Requirements
Python 3.7+

.env file with:

```bash
GEMINI_API_KEY=your_api_key_here
```

## Required Python packages:

```bash
python-dotenv

agents (custom or external package)
```



Let me know if you’d like to include instructions for installing dependencies or creating the `.env` file.








