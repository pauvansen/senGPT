# SenGPT Chat Application

## Overview

SenGPT is a Flask-based web application that uses the OpenAI GPT-3.5-turbo model to provide responses to user questions. The responses are cached for efficiency, using both in-memory and SQLite-based caching mechanisms. The application interface is a simple chat-like interface where users can ask questions, and SenGPT responds in German.

## Features

- Flask backend for handling HTTP requests.
- OpenAI GPT-3.5-turbo model for generating responses.
- In-memory and SQLite caching to improve response time and reduce redundant API calls.
- Simple web interface for interacting with the chat application.

## Setup and Installation

### Prerequisites

- Python 3.7+
- Flask
- OpenAI API key

### Installation Steps

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/sengpt.git
    cd sengpt
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the OpenAI API key:**

    Replace `"OPENAI_API_KEY"` in the `setup_model` method with your actual OpenAI API key.

5. **Run the Flask application:**

    ```sh
    python app.py
    ```

    The application will be available at `http://127.0.0.1:5000`.

## Code Structure

### `SenGPTCache` Class

This class encapsulates the logic for setting up and using the OpenAI GPT-3.5-turbo model with caching.

- **setup_model()**: Configures the OpenAI model.
- **setup_in_memory_cache()**: Sets up in-memory caching.
- **setup_sqlite_cache()**: Sets up SQLite caching.
- **setup_prompt_template(template_string)**: Sets up the prompt template.
- **predict(prompt)**: Generates a response using the configured model and cache.

### Flask Application

The Flask application defines two routes:

- `/`: Serves the main HTML page.
- `/ask`: Handles POST requests to receive a question and return a response from SenGPT.

### HTML and JavaScript

The frontend is a simple HTML page with embedded JavaScript to handle user interactions.

- **HTML**: Defines the chat interface layout.
- **CSS**: Styles the chat interface.
- **JavaScript**: Handles user input, sends questions to the backend, and displays responses.

## Usage

1. Open a web browser and navigate to `http://127.0.0.1:5000`.
2. Enter a question in the input box and click "Send".
3. SenGPT will respond in German, and the conversation will be displayed in the chat interface.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [OpenAI](https://openai.com/)
- [LangChain](https://www.langchain.com/)

---

Feel free to customize this README file further based on your specific needs and any additional features you might add to the application.
