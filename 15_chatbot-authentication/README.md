# Gemini Chatbot with Chainlit

This code implements a simple chatbot using Google's Gemini AI model and the Chainlit framework for the web UI.  It allows users to interact with the Gemini model through a chat interface.

## Key Features:

*   **Environment Variable Loading:** Loads API keys and other configurations from a `.env` file.
*   **Gemini Integration:**  Connects to the Google Gemini AI model for generating responses. Specifically uses `gemini-2.0-flash` for faster responses.
*   **Chainlit UI:** Uses Chainlit to create a user-friendly chat interface in the browser.
*   **Chat History:** Maintains chat history to provide context for the Gemini model.
*   **OAuth Callback (GitHub):** Includes an OAuth callback function (currently only prints debugging information), presumably for future implementation to support user authentication via GitHub.
*   **Asynchronous Handling:** Uses `async` and `await` for non-blocking operations.

## How it Works:

1.  **Initialization:** Loads API keys, configures Gemini, and initializes the Chainlit application.
2.  **Chat Start:** When a user starts a new chat session, an empty chat history is created, and a welcome message is displayed.
3.  **Message Handling:** When a user sends a message:
    *   The message is added to the chat history.
    *   The chat history is formatted for the Gemini model.
    *   The Gemini model generates a response based on the history.
    *   The response is added to the chat history.
    *   The response is displayed to the user in the Chainlit UI.
4. **OAuth Authentication**: When a user authenticates with Github. The callback function handles the authentication.

## Requirements:

*   Python 3.6+
*   `chainlit`
*   `google-generativeai`
*   `python-dotenv`

## Setup

1.  **Install dependencies:**
    ```bash
    pip install chainlit google-generativeai python-dotenv
    ```

2.  **Create a `.env` file:**
    ```
    GEMINI_API_KEY=YOUR_GEMINI_API_KEY
    ```
    Replace `YOUR_GEMINI_API_KEY` with your actual Gemini API key.

3.  **Run the Chainlit app:**
    ```bash
    chainlit run main.py  
    ```

## Important Notes:

*   The OAuth callback function is a placeholder and needs further implementation to fully support GitHub authentication.
*   Error handling could be improved to gracefully handle cases where the Gemini API fails.


