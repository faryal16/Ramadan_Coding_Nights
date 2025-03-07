# FastAPI Side Hustles & Money Quotes API

A simple FastAPI application that provides random side hustle ideas and money-related quotes.

## Installation


Create and activate a virtual environment:


python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
Install dependencies:


pip install fastapi uvicorn
Running the API
Run the FastAPI server using:

uvicorn main:app --reload
The API will be available at http://127.0.0.1:8000.

API Endpoints
Get a Random Side Hustle
Endpoint: GET /side_hustles
Query Parameter: apiKey (string) - Required
Example Request:
arduino

http://127.0.0.1:8000/side_hustles?apiKey=123456789
Response:
json

{
  "side_hustle": "Freelancing - Start offering your skills online!"
}
Get a Random Money Quote
Endpoint: GET /money_quotes
Query Parameter: apiKey (string) - Required
Example Request:
arduino

http://127.0.0.1:8000/money_quotes?apiKey=123456789
Response:
json

{
  "money_quotes": "Money grows on the tree of persistence. – Japanese Proverb"
}
API Key
The API requires an apiKey query parameter.
Use 123456789 as the valid API key.
If an invalid key is provided, the response will return:
json

{
  "error": "Invalid Api Key"
}
License
This project is open-source.

vbnet


Let me know if you need any modifications! 🚀



