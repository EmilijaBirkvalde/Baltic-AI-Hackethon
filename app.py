import streamlit as st
import fitz  # PyMuPDF
from groq import Groq
from PIL import Image
import pyttsx3
import base64
import random
import spacy

# Load the spaCy English model for NLP tasks
nlp = spacy.load("en_core_web_sm")

# Initialize the Groq client with your actual API key
client = Groq(api_key='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')

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

# Function to generate true or false questions based on the context
def generate_true_false_questions(context):
    questions = []
    sentences = context.split('.')  # Split text into sentences to derive statements
    for sentence in sentences:
        if sentence.strip():
            statement, answer = create_true_false_question(sentence)
            questions.append((statement, answer))
    return questions[:10]  # Limit to 10 questions

# Function to create a true or false question
def create_true_false_question(sentence):
    # Assume the statement is true for simplicity
    true_statement = sentence.strip()
    # Create a false statement by negating the first part of the sentence
    false_statement = true_statement.replace("is", "is not").replace("are", "are not")
    
    # Randomly choose true or false answer for the question
    if random.choice([True, False]):
        return true_statement, True  # Return true statement
    else:
        return false_statement, False  # Return false statement

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
st.title("Empowering Your Workflow")
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

    # Quiz Generation
    if st.button("Take Test"):
        true_false_questions = generate_true_false_questions(pdf_text)
        st.session_state.true_false_questions = true_false_questions  # Store questions in session state
        st.session_state.user_answers = []  # To store user answers
        st.session_state.correct_answers = 0  # To track correct answers
        st.success("Questions generated!")

    # Display the quiz
    if 'true_false_questions' in st.session_state:
        st.subheader("True/False Quiz Questions:")
        for i, (statement, answer) in enumerate(st.session_state.true_false_questions):
            user_answer = st.radio(f"{i+1}. {statement}", ("True", "False"), key=f'question_{i}')
            st.session_state.user_answers.append(user_answer == "True")  # Store boolean answer

        if st.button("Submit Answers"):
            for i, (statement, answer) in enumerate(st.session_state.true_false_questions):
                if st.session_state.user_answers[i] == answer:
                    st.session_state.correct_answers += 1

            # Provide overall feedback
            total_questions = len(st.session_state.true_false_questions)
            feedback = f"You answered {st.session_state.correct_answers} out of {total_questions} questions correctly."
            st.success(feedback)

    question = st.text_input("Ask a question about the PDF:")
    if question:
        answer = ask_question(pdf_text, question)
        st.subheader("Answer:")
        st.write(answer)

        # Convert the answer to speech using pyttsx3 and display the audio player
        if st.button("Hear the Answer"):
            audio_html = text_to_speech_pyttsx3(answer)
            st.markdown(audio_html, unsafe_allow_html=True)
