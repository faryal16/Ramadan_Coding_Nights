from fastapi import FastAPI
import random

app = FastAPI()

# Sample list of random programs
programs = [
    {"name": "To-Do App", "description": "A simple task manager."},
    {"name": "Weather App", "description": "Fetches real-time weather data."},
    {"name": "Quiz Game", "description": "A fun multiple-choice quiz."},
    {"name": "Password Generator", "description": "Generates strong passwords."},
    {"name": "Unit Converter", "description": "Converts between different units."}
]

@app.get("/program")
def get_random_program():
    return random.choice(programs)