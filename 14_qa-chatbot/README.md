# Gemini-Powered Chatbot with Chainlit

This repository contains a simple chatbot application built using Chainlit, Google's Gemini API, and Python. It leverages the power of the Gemini language model to provide intelligent and interactive responses to user queries.

## Features

*   **Chainlit Integration:** Uses Chainlit to create a user-friendly chatbot interface.
*   **Gemini API:** Leverages the Google Gemini API (specifically `gemini-2.0-flash` model) for generating responses.
*   **Environment Variable Handling:** Uses `.env` files to securely store and manage API keys.
*   **Simple Conversation Flow:** Greets the user and responds to messages using the Gemini model.

## Prerequisites

Before running this application, you will need to:

1.  **Obtain a Google Gemini API Key:**  You can get an API key from the Google AI Studio: [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey).
2.  **Install Python:** Ensure you have Python 3.7 or higher installed.
3.  **Install the required Python packages:**

    ```bash
    pip install chainlit google-generativeai python-dotenv
    ```

## Setup

1.  **Clone the Repository:**

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Create a `.env` file:**  In the root directory of the project, create a file named `.env`.

3.  **Add your Gemini API key to the `.env` file:**

    ```
    GEMINI_API_KEY=YOUR_GEMINI_API_KEY
    ```

    Replace `YOUR_GEMINI_API_KEY` with the actual API key you obtained from Google AI Studio.

4.  **Run the Chainlit Application:**

    ```bash
    chainlit run main.py
    ```

    This command will start the Chainlit server, and you can access the chatbot interface in your web browser (usually at `http://localhost:8000`).

## Code Explanation

*   **`main.py`:** This is the main script that defines the chatbot logic.

    *   **Imports:** Imports necessary libraries like `os`, `chainlit`, `google.generativeai`, and `dotenv`.
    *   **Environment Variable Loading:** Loads the Gemini API key from the `.env` file using `load_dotenv()` and `os.getenv()`.
    *   **Gemini API Configuration:** Configures the Gemini API with the loaded API key using `genai.configure(api_key=gemini_api_key)`.
    *   **Model Initialization:** Initializes the `gemini-2.0-flash` model using `genai.GenerativeModel(model_name="gemini-2.0-flash")`.
    *   **`@cl.on_chat_start`:**  This decorator defines the function `handle_chat_start` that is executed when a new chat session begins. It sends a welcome message to the user.
    *   **`@cl.on_message`:** This decorator defines the function `handle_message` that is executed when a new message is received from the user.
        *   It extracts the message content.
        *   Uses the Gemini model to generate a response.
        *   Sends the response back to the user using `cl.Message(content=response_text).send()`.  It also handles cases where the response might not have a `text` attribute, preventing errors.

## Troubleshooting

*   **API Key Issues:**  Double-check that your API key is valid and correctly stored in the `.env` file.
*   **Installation Errors:**  Ensure you have installed all the required packages using `pip install`.  Check the console output for any error messages during installation.
*   **Chainlit Not Running:** If Chainlit fails to start, verify that port 8000 is available or try specifying a different port with `chainlit run main.py --port <port_number>`.
*   **Response Issues:** If the chatbot is not responding, check the console output for any errors from the Gemini API.

## Future Enhancements

*   **Memory Management:** Implement a mechanism to store conversation history to provide more context-aware responses.
*   **Error Handling:** Add more robust error handling to gracefully handle API errors or invalid user input.
*   **Customization:**  Allow users to customize the chatbot's personality or behavior through configuration options.
*   **More Complex Prompts:** Experiment with more sophisticated prompting techniques to improve the quality of responses.
*   **Integration with Other Tools:** Integrate the chatbot with other tools or services, such as databases or external APIs.

## Contributing

Contributions are welcome!  Feel free to submit pull requests with bug fixes, improvements, or new features.  Please follow these guidelines:

*   Write clear and concise commit messages.
*   Test your changes thoroughly.
*   Provide documentation for any new features.



