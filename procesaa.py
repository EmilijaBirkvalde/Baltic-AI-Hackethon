import streamlit as st
import fitz  # PyMuPDF
from groq import Groq
from PIL import Image
import pyttsx3
import base64
import os

# Initialize the Groq client with your actual API key
client = Groq(api_key='secret')

# Initialize pyttsx3 for text-to-speech
engine = pyttsx3.init()

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_file):
    doc = fitz.open(pdf_file)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Function to summarize text using Groq API
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

# Function to ask a question based on the context using Groq API
def ask_question(context, question):
    try:
        answer_response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant."
                },
                {
                    "role": "user",
                    "content": f"Context: {context} Question: {question}"
                }
            ],
            model="llama-3.1-8b-instant",
        )
        return answer_response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

# Function to convert text to speech using pyttsx3 (offline)
def text_to_speech_pyttsx3(text):
    engine.save_to_file(text, "output.mp3")
    engine.runAndWait()

    with open("output.mp3", "rb") as audio_file:
        audio_bytes = audio_file.read()
        audio_base64 = base64.b64encode(audio_bytes).decode('utf-8')
        audio_html = f'<audio controls><source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3"></audio>'
        return audio_html

# Streamlit UI
st.title("PDF Summarizer and Question Answering")
image = Image.open('AI Pic 5.jpg')  # Make sure the image file is in the same directory or provide the full path
st.image(image, use_column_width='always')

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    pdf_text = extract_text_from_pdf(uploaded_file)

    st.subheader("Text Extracted from PDF:")
    st.write(pdf_text[:500])  # Display a snippet of the text for review

    summary_button = st.button("Summarize Text")
    if summary_button:
        summary = summarize_text(pdf_text)
        st.subheader("Summary:")
        st.write(summary)

    question = st.text_input("Ask a question about the PDF:")
    if question:
        answer = ask_question(pdf_text, question)
        st.subheader("Answer:")
        st.write(answer)

        # Convert the answer to speech using pyttsx3 and display the audio player
        if st.button("Hear the Answer"):
            audio_html = text_to_speech_pyttsx3(answer)
            st.markdown(audio_html, unsafe_allow_html=True)
