import requests

# IBM Watson API request setup
url = "https://us-south.ml.cloud.ibm.com/ml/v1/text/generation?version=2023-05-29"

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
    "Authorization": "Bearer eyJraWQiOiIyMDI0MTAwMjA4NDIiLCJhbGciOiJSUzI1NiJ9.eyJpYW1faWQiOiJzcGpwOGlOWXFxLTU3MTRkYThkLTIwZjQtNDk5Ni05NzEwLTIwNGFjZmVjMGNlNCIsImlkIjoic3BqcDhpTllxcS01NzE0ZGE4ZC0yMGY0LTQ5OTYtOTcxMC0yMDRhY2ZlYzBjZTQiLCJyZWFsbWlkIjoic3BqcDhpTllxcSIsImp0aSI6ImM4YzJmNjJjLTZjNjUtNDg3OC1hZjU0LTkzYTE0YTE3OGE0MiIsImlkZW50aWZpZXIiOiI1NzE0ZGE4ZC0yMGY0LTQ5OTYtOTcxMC0yMDRhY2ZlYzBjZTQiLCJnaXZlbl9uYW1lIjoibm90c2V0IiwiZmFtaWx5X25hbWUiOiJub3RzZXQiLCJuYW1lIjoic3R1ZGVudF9jenVvYWYiLCJlbWFpbCI6InN0dWRlbnRfY3p1b2FmQHRlY2h6b25lLmlibS5jb20iLCJzdWIiOiJzdHVkZW50X2N6dW9hZiIsImF1dGhuIjp7InN1YiI6InN0dWRlbnRfY3p1b2FmIiwiaWFtX2lkIjoic3BqcDhpTllxcS01NzE0ZGE4ZC0yMGY0LTQ5OTYtOTcxMC0yMDRhY2ZlYzBjZTQiLCJuYW1lIjoic3R1ZGVudF9jenVvYWYiLCJnaXZlbl9uYW1lIjoibm90c2V0IiwiZmFtaWx5X25hbWUiOiJub3RzZXQiLCJlbWFpbCI6InN0dWRlbnRfY3p1b2FmQHRlY2h6b25lLmlibS5jb20ifSwiYWNjb3VudCI6eyJ2YWxpZCI6dHJ1ZSwiYnNzIjoiOWY4Zjk1ZWVlNDcxNDQ3M2E4N2ZhMzE5ZDk2NDA2M2MiLCJpbXNfdXNlcl9pZCI6IjEyNzc5MjI5IiwiZnJvemVuIjp0cnVlLCJpc19lbnRlcnByaXNlX2FjY291bnQiOmZhbHNlLCJlbnRlcnByaXNlX2lkIjoiZWU1NzVjNTc3ODc2NGQ0MDkxNTVhYTM1NzgwZWM4ZDEiLCJpbXMiOiIyNjM2NzI3In0sImlhdCI6MTcyODE0MjIwOCwiZXhwIjoxNzI4MTQ1ODA4LCJpc3MiOiJodHRwczovL2lhbS5jbG91ZC5pYm0uY29tL2lkZW50aXR5IiwiZ3JhbnRfdHlwZSI6InVybjppYm06cGFyYW1zOm9hdXRoOmdyYW50LXR5cGU6YXBpa2V5Iiwic2NvcGUiOiJpYm0gb3BlbmlkIiwiY2xpZW50X2lkIjoiZGVmYXVsdCIsImFjciI6MSwiYW1yIjpbInB3ZCJdfQ.RmD3tr2ZL5vKLHRYRMDD0rnQVQWQQPV3YhiEg73Q_KBlQdWuGANCwN6OH5QrEfeBtn1_VcMqPEKaYLvqD0SvxeQYOOLyiUa6H4rsQZkpQ7YlaFtE6Zid2BT4cktfYKzJIa32etQ_RI_6naZ5GLqHSds4EAfQV2Q2eF15kccyosxykM-mEXHOZviC2YRDUScvmCW0X8RNRvBhueGWoeWlIfMo0n5QzViyX9E2kYvJ86wxlKy1viTishqlaCsk4RKzWD4L73gS9JkN5xga2uY2hZdUsxNG_7xMJfp26FCV8P6IQX8DUHwm3i19HuQfbsGOZkxuO-sbw0JP3kvX6FD11A"
}

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

pdf_path = r"C:\Users\ediit\OneDrive\Dators\Viss\Boring_fire_safety.pdf"
pdf_text = extract_text_from_pdf(pdf_path)
pdf_text[0:1000]





import os
from groq import Groq

# Initialize the Groq client (replace with your actual API key)
client = Groq(api_key='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')

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
