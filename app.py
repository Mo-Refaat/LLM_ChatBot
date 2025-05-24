import streamlit as st
from ui.layout import initialize_ui
from features.ask_questions import ask_questions_page
from features.summarize_document import summarize_document_page
from features.image_captioning import image_captioning_page
from features.visual_question_answering import visual_question_answering_page
from features.image_text_qa import image_text_qa_page

import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="torch")

# Initialize UI
initialize_ui()

# Sidebar for feature selection
feature = st.sidebar.selectbox("Choose a feature", [
    "Ask Questions",
    "Summarize Document",
    "Image Captioning",
    "Visual Question Answering",
    "Image Text QA",
])

# Route to selected feature
if feature == "Ask Questions":
    ask_questions_page()
    
elif feature == "Summarize Document":
    summarize_document_page()

elif feature == "Image Captioning":
    documents_directory = "data/uploads" 
    image_captioning_page(documents_directory)

elif feature == "Visual Question Answering":
    visual_question_answering_page()

elif feature == "Image Text QA":
    documents_directory = "data/uploads"  
    vector_store_path = "data/index/faiss_index"  
    image_text_qa_page(documents_directory, vector_store_path)
