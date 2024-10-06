## Baltic AI Hakathon
### Challange 7:  LVRTC Adaptive AI Solutions for Personalized Learning of Regulations and Guidelines
This Python code in `app.py` file creates a Streamlit web app designed for extracting text from PDFs, summarizing the content, generating true/false quizzes, answering user questions about the text, and providing text-to-speech functionality. Here's a more detailed breakdown of the specification:

### 1. **PDF Text Extraction**
   - **Library**: `PyMuPDF` (`fitz`).
   - **Function**: `extract_text_from_pdf(pdf_file)`
     - This function takes a PDF file as input, opens it using `fitz.open()`, and iterates through each page to extract the text using the `page.get_text()` method. 
     - It concatenates the extracted text from all pages and returns the complete text.

### 2. **Text Summarization**
   - **API Service**: Groq API.
   - **Function**: `summarize_text(text)`
     - Uses the Groq API to generate a summary of the extracted PDF text.
     - Sends a chat-like request to the Groq API using the "llama-3.1-8b-instant" language model. The request includes two messages: one defining the assistant's role ("You are a helpful assistant.") and another containing the user's prompt to summarize the provided text.
     - The response is returned as the summary, extracted from `summary_response.choices[0].message.content`.

### 3. **True/False Quiz Generation**
   - **Core Functionality**: Automatically generates true/false questions from the extracted text.
   - **Functions**:
     - `generate_true_false_questions(context)`
       - Takes the extracted text (context), splits it into sentences, and iterates through them to create quiz questions.
       - Calls the helper function `create_true_false_question(sentence)` to generate individual questions.
     - `create_true_false_question(sentence)`
       - Assumes the original sentence is true.
       - Constructs a false version of the sentence by replacing verbs like "is" with "is not" and "are" with "are not".
       - Randomly selects either the true or modified false sentence as the quiz question and returns it along with a boolean answer (True for correct statements, False for incorrect).
   - **Quiz Logic**:
     - The app allows users to answer true/false questions via `st.radio()` buttons. After submitting their answers, the correct answers are counted, and a score is presented.

---

### ⚠️ **Important Notice!**

The quiz feature is not fully developed yet; it is currently just a rough concept that demonstrates how it might look visually. In future iterations, the logic will be refined using AI generation techniques to ensure accurate answers and to create more personalized and knowledge-deepening test questions.

---


### 4. **Question & Answering Based on PDF Content**
   - **API Service**: Groq API.
   - **Function**: `ask_question(context, question)`
     - Users can input a custom question about the PDF content.
     - The function sends a request to the Groq API, where it provides the full PDF text (context) and the user's question.
     - It returns the answer extracted from `answer_response.choices[0].message.content`.

### 5. **Text-to-Speech (TTS)**
   - **Library**: `pyttsx3`.
   - **Function**: `text_to_speech_pyttsx3(text)`
     - Converts a given text into speech using the `pyttsx3` TTS engine.
     - Saves the audio output as an MP3 file ("output.mp3").
     - Loads the MP3 file, encodes it in Base64, and creates an HTML audio player to allow the user to listen to the audio within the Streamlit app.
     - The audio player is returned in the form of an HTML string with embedded Base64-encoded audio.

### 6. **Streamlit UI Components**
   - **Image Display**:
     - The app starts by loading and displaying an image (`AI Pic 5.jpg`) using `st.image()`. The image must be placed in the same directory or referenced with the correct path.
   - **File Uploader**:
     - The user uploads a PDF file through `st.file_uploader()`, which only accepts PDF files.
   - **Text Display**:
     - After the user uploads a PDF, the app extracts and displays the first 500 characters of the text for review.
   - **Buttons**:
     - "Summarize Text" Button: When clicked, it triggers the `summarize_text()` function to summarize the PDF text.
     - "Take Test" Button: This generates true/false quiz questions from the text using `generate_true_false_questions()`.
     - "Submit Answers" Button: After answering the quiz, users can click this button to check their answers and receive feedback on the number of correct responses.
   - **Custom Q&A Input**:
     - A text input field (`st.text_input()`) allows users to ask custom questions about the PDF content, triggering the `ask_question()` function for an answer.
   - **TTS Button**:
     - A button to trigger text-to-speech generation for the provided answer. If clicked, it plays the audio within the app using the HTML audio player returned by `text_to_speech_pyttsx3()`.

### 7. **Session State Management**
   - The app uses Streamlit’s `st.session_state` to manage the quiz state, including:
     - Storing generated quiz questions.
     - Keeping track of user answers.
     - Counting the number of correct answers.

### 8. **Error Handling**
   - The app includes basic exception handling for interactions with the Groq API. If an error occurs during the summarization or Q&A requests, it catches the exception and displays an error message instead of crashing the app.

### Key Libraries and Technologies:
   - **Streamlit**: For building the interactive UI.
   - **PyMuPDF (fitz)**: For extracting text from PDFs.
   - **Groq API**: For summarization and Q&A (based on large language models).
   - **pyttsx3**: For converting text to speech (offline TTS).
   - **PIL (Image)**: For loading and displaying images in the app.
   - **Random**: For randomizing the true/false quiz answers.

This specification outlines how each component in the app functions and interacts to provide a complete workflow for users to extract, analyze, and interact with PDF content.



**Reference:**

This website development code was initially based on the tutorial from Pitsillides91's project "Using FB Llama models on PDF," available on GitHub [Pitsillides91 GitHub repository](https://github.com/Pitsillides91/llms_2024/blob/main/4.Metas_Llama/Using%20FB%20llama%20models%20on%20PDF.ipynb). The functionality, including PDF text extraction, text summarization, and the use of the LLaMA model, diolog addiotion,  audio file and quiz building, was further modified, adapted or added to meet our specific requirements and to expand the website's capabilities.


---

In addition to the development of the core functionality, a higher-quality design prototype has been created using **Figma**, with a more detailed and polished layout for the website. The design prototype outlines a visually appealing and user-friendly interface, laying the groundwork for future development of an improved and more refined version of the site.

You can explore the design through the following links:
- **Slideshow Overview**: [Figma Slideshow](https://www.figma.com/proto/xLZ0zFWKJBNoXvBEaa0yFR/Perceiva-design-prototype?node-id=20-70&node-type=canvas&t=XrVpkyUySNbBwaIk-1&scaling=scale-down&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=20%3A70)
- **Design Overview**: [Figma Design Overview](https://www.figma.com/design/xLZ0zFWKJBNoXvBEaa0yFR/Perceiva-design-prototype?node-id=0-1&t=6lhsLbvjnHB3qbF1-1)

The plan is to implement this enhanced version in future iterations, ensuring a higher-quality, well-designed user experience.

---




---

### **Color Palette**

The design of the website incorporates the following color scheme to ensure a modern and cohesive aesthetic:

- **Primary Color**: `#7071E8` - A bold, elegant **blue** used for primary elements and accents.
- **Secondary Color**: `#C683D7` - A soft **lavender** shade, adding a calming contrast to the design.
- **Accent Color**: `#ED9ED6` - A vibrant **pink** used to highlight key features and interactive elements.
- **Background Color**: `#FFC7C7` - A warm **peach** hue that enhances readability and visual appeal.

This color palette ensures a visually pleasing and harmonious user experience across the website.

---
