import requests

# IBM Watson API request setup
url = "secret"

body = {
    "parameters": {
        "decoding_method": "greedy",
        "max_new_tokens": 200,
        "repetition_penalty": 1
    },
    "model_id": "meta-llama/llama-3-70b-instruct",
    "project_id": "4763a576-7903-490c-975e-e539c573cff1",
    "moderations": {
        "hap": {
            "input": {
                "enabled": True,
                "threshold": 0.5,
                "mask": {
                    "remove_entity_value": True
                }
            },
            "output": {
                "enabled": True,
                "threshold": 0.5,
                "mask": {
                    "remove_entity_value": True
                }
            }
        }
    },
    "input": "What is the sigma?"
}

# Replace this with your actual Bearer token
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer secret"

# Make the API request
response = requests.post(
    url,
    headers=headers,
    json=body
)

if response.status_code != 200:
    raise Exception("Non-200 response: " + str(response.text))

data = response.json()
print(data["results"][0]["generated_text"])




import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

pdf_path = "pdf_path"
pdf_text = extract_text_from_pdf(pdf_path)
pdf_text[0:1000]





import os
from groq import Groq

# Initialize the Groq client (replace with your actual API key)
client = Groq(api_key='secret')

# Function to summarize text
def summarize_text(text):
    try:
        summary_response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": f"Summarize the following text: {text}"
                }
            ],
            model="llama-3.1-8b-instant",
        )
        return summary_response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

# Assuming you have already extracted the text from the PDF
pdf_text = extract_text_from_pdf

# Summarize the PDF text
summary = summarize_text(pdf_text)
print("Summary:")
print(summary)
