# Wordsmith-AI              This ![Wordsmith](https://github.com/Cruz455/Wordsmith-AI/assets/117976019/6fecf7e9-cd05-45f7-a2e3-82949834b592)
repository contains a Content Generator API that generates content based on a given format, topic, emotion, and length using OpenAI's GPT-3.5-turbo model.

## Features

- Generates content based on user-specified format, topic, emotion, and length
- Utilizes OpenAI's powerful GPT-3.5-turbo model for content generation
- Provides a user-friendly Gradio interface for easy interaction
- Supports API integration for programmatic content generation

## Requirements

- Python 3.6 or above
- Required libraries:
  - `openai`
  - `flask`
  - `gradio`

## Installation

1. Clone the repository:
git clone https://github.com/Cruz455/Wordsmith-AI.git

2. Navigate to the project directory:
cd your-repository

3. Create a virtual environment (optional but recommended):
python -m venv venv

4. Activate the virtual environment:
- For Windows:
  ```
  venv\Scripts\activate
  ```
- For macOS and Linux:
  ```
  source venv/bin/activate
  ```

5. Install the required libraries:
pip install -r requirements.txt

## Usage

1. Run the content generator:
python content_generator.py

2. Access the Gradio interface in your web browser at `http://localhost:7860`.

3. Enter the desired format, topic, emotion, and length in the provided input fields.

4. Click the "Generate Content" button to generate content.

5. The generated content will be displayed in the output text area.

## API Endpoint

- **URL:** `/generate`
- **Method:** `POST`
- **Request Body:**
- `format` (string): The format of the content to be generated (e.g., "LinkedIn post").
- `topic` (string): The topic of the content (e.g., "Generative AI").
- `emotion` (string, optional): The desired emotion of the content (e.g., "excited"). Default is "excited".
- `length` (integer, optional): The desired length of the generated content in tokens. Default is 100.
- **Response:**
- `text` (string): The generated content based on the provided parameters.

Note: Make sure to replace the OpenAI API key in the code with your own valid API key.
