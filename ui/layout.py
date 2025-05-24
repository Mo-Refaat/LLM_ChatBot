import streamlit as st

def initialize_ui():
    """
    Initializes the Streamlit app UI with a layout similar to ChatGPT.
    """
    st.set_page_config(
        page_title="Multimodal Chatbot",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.sidebar.title("Multimodal Chatbot")
    st.sidebar.info(
        """
        Select a feature from the sidebar to get started.
        """
    )
    st.sidebar.image("static/logo.png", use_container_width=True)
