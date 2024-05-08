# Content Generator

This is a content generator that uses OpenAI's GPT-3.5-turbo model to generate content based on a given format, topic, emotion, and length.

## Installation

1. Clone the repository:
git clone https://github.com/Cruz455/Wordsmith-AI.git

2. Navigate to the project directory:
cd your-repository

3. Install the required dependencies:
pip install -r requirements.txt

## Usage

1. Run the `content_generator.py` file:
python content_generator.py

2. The Gradio interface will be launched, and you will see input fields for format, topic, emotion, and length.

3. Enter the desired values in the input fields and click the "Generate Content" button.

4. The generated content will be displayed in the output text area.

## API

## API Endpoint

The Content Generator also provides an API endpoint for generating content programmatically.

- **Endpoint:** `/generate`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "format": "LinkedIn post",
    "topic": "Generative AI",
    "emotion": "excited",
    "length": 100
  }


Note: Make sure to replace the OpenAI API key in the code with your own valid API key.
