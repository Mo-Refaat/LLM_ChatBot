import streamlit as st

def render_chat_header():
    """
    Renders the consistent header for the chatbot app.
    """
    st.title("Multimodal Chatbot")
    st.write("An AI-powered chatbot integrating NLP and Computer Vision features.")

def render_chat_ui(chat_memory):
    """
    Renders the chat interface with conversation history.
    Args:
        chat_memory: Instance of ChatMemory containing the chat history.
    """
    st.subheader("Conversation History")
    history = chat_memory.get_history()
    if history:
        for entry in history:
            st.markdown(f"**You:** {entry['user']}")
            st.markdown(f"**Bot:** {entry['bot']}")
    else:
        st.write("No conversation history yet.")

    # Clear chat history button
    if st.button("Clear Chat History"):
        chat_memory.clear_history()
        st.session_state["chat_memory"] = chat_memory  # Reset the session state
        st.success("Chat history cleared!")
