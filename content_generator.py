import openai
from flask import Flask, request, jsonify
import gradio as gr

app = Flask(__name__)

# Create an OpenAI client using your API key
from openai import OpenAI
client = OpenAI(api_key='your-openai-api-key')

def generate_content(format, topic, emotion="excited", length=100):
    prompt = f"{emotion.capitalize()} insights on {topic}! 🚀 {format}."
    response = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt}
        ],
        model="gpt-3.5-turbo",  # Make sure this model is available in your OpenAI subscription
        max_tokens=length
    )
    # Print response for debugging
    print(response)
    # Safely extract message content from the response
    message_content = response.choices[0].message.content if hasattr(response.choices[0].message, 'content') else "No content returned."
    return message_content

@app.route('/generate', methods=['POST'])
def generate_api():
    data = request.get_json()
    format = data['format']
    topic = data['topic']
    emotion = data.get('emotion', 'excited')
    length = data.get('length', 100)
    result = generate_content(format, topic, emotion, length)
    return jsonify({"text": result})

def gradio_interface():
    with gr.Blocks() as demo:
        with gr.Row():
            format_input = gr.Textbox(label="Format (e.g., LinkedIn post)")
            topic_input = gr.Textbox(label="Topic (e.g., Generative AI)")
        with gr.Row():
            emotion_input = gr.Textbox(label="Emotion (optional)", placeholder="Excited (optional)")
            length_input = gr.Slider(minimum=50, maximum=300, label="Length (optional)", value=100)
        output_text = gr.Textbox(label="Generated Content", lines=10)
        generate_button = gr.Button("Generate Content")
        generate_button.click(
            fn=generate_content, 
            inputs=[format_input, topic_input, emotion_input, length_input], 
            outputs=output_text
        )
    demo.launch(share=True)  # Set 'share=True' to create a public link

if __name__ == "__main__":
    gradio_interface()
