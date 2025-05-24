import os
import streamlit as st
from models.langchain_rag import run_rag_pipeline
from models.memory import ChatMemory
from ui.chat_ui import render_chat_ui
from utils.file_manager import process_uploaded_file, process_arxiv_url
from audio.stt import transcribe_audio_to_text
from audio.tts import convert_text_to_audio

# Paths for documents and vector index
documents_directory = "data/uploads"
vector_store_path = "data/index/faiss_index"

# Initialize or retrieve chat memory from session state
if "chat_memory" not in st.session_state:
    st.session_state["chat_memory"] = ChatMemory()

chat_memory = st.session_state["chat_memory"]

def ask_questions_page():
    """
    Streamlit page for the Ask Questions feature with audio support.
    """
    # File Upload Section or ArXiv URL
    uploaded_file = st.file_uploader("Upload a file (PDF, CSV) or provide an ArXiv URL", type=["pdf", "csv"])
    arxiv_url = st.text_input("Enter an ArXiv URL (e.g., https://arxiv.org/abs/1234.56789)")
    qa_chain = None

    try:
        extracted_text = ""
        if uploaded_file:
            st.info("Processing the uploaded file...")
            extracted_text = process_uploaded_file(uploaded_file)
        elif arxiv_url:
            st.info("Processing the ArXiv URL...")
            extracted_text = process_arxiv_url(arxiv_url)
        else:
            st.info("Please upload a file or provide an ArXiv URL to start.")

        if extracted_text:
            st.success("File processed successfully!")
            qa_chain = run_rag_pipeline(documents_directory, vector_store_path)

            # Voice Input Section
            if st.button("Start Recording"):
                st.info("Recording... Speak now!")
                question = transcribe_audio_to_text()
                if question:
                    st.success(f"Recognized Question: {question}")
                    try:
                        # Prepend context from chat memory
                        context = chat_memory.get_context()
                        full_query = f"{context}\nUser: {question}\nBot:"
                        st.info("Fetching the answer...")
                        answer = qa_chain.run(full_query)

                        if not answer.strip():
                            answer = "I could not find an answer to your question. Please try again."

                        # Save the question and answer in memory
                        chat_memory.add_message(question, answer.strip("Bot: ").strip())

                        # Display the answer with "Listen to Answer" option
                        st.subheader("Answer")
                        st.write(answer)
                        
                        if st.button("Listen to the Answer"):
                            audio_stream = convert_text_to_audio(answer)
                            if audio_stream:
                                st.audio(audio_stream, format="audio/mp3")  
                            else:
                                st.error("Failed to generate audio response.")
                        
                    except Exception as e:
                        st.error(f"Error fetching the answer: {e}")
                else:
                    st.warning("Could not understand your audio input. Please try again.")

            # Text Input Section
            question = st.text_input("Enter your question", key="user_input")
            if st.button("Ask", key="ask_button"):
                try:
                    # Prepend context from chat memory
                    context = chat_memory.get_context()
                    full_query = f"{context}\nUser: {question}\nBot:"
                    st.info("Fetching the answer...")
                    answer = qa_chain.run(full_query)

                    if not answer.strip():
                        answer = "I could not find an answer to your question. Please try again."

                    # Save the question and answer in memory
                    chat_memory.add_message(question, answer.strip("Bot: ").strip())

                    # Display the answer with "Listen to Answer" option
                    st.subheader("Answer")
                    st.write(answer)

                    if st.button("Listen to the Answer"):
                        audio_stream = convert_text_to_audio(answer)
                        if audio_stream:
                            st.audio(audio_stream, format="audio/mp3")  
                        else:
                            st.error("Failed to generate audio response.")
                except Exception as e:
                    st.error(f"Error fetching the answer: {e}")

            # Render Chat History
            render_chat_ui(chat_memory)
    except Exception as e:
        st.error(f"Error: {e}")
