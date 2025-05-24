import os
import streamlit as st
from models.langchain_rag import run_rag_pipeline
from utils.file_handler import process_uploaded_file, process_arxiv_url

# Paths for documents and vector index
documents_directory = "data/uploads"
vector_store_path = "data/index/faiss_index"

# Ensure directories exist
os.makedirs(documents_directory, exist_ok=True)
os.makedirs(os.path.dirname(vector_store_path), exist_ok=True)

def summarize_document_page():
    """
    Streamlit page for the Summarize Document feature.
    """
    # File Upload Section
    uploaded_file = st.file_uploader("Upload a file (PDF, CSV)", type=["pdf", "csv"])
    arxiv_url = st.text_input("Enter an ArXiv URL (e.g., https://arxiv.org/abs/1234.56789)")
    
    if not uploaded_file and not arxiv_url:
        st.info("Please upload a file or provide an ArXiv URL to start.")
        return

    # Process the uploaded file or ArXiv URL
    try:
        if uploaded_file:
            file_path = os.path.join(documents_directory, uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.read())
            extracted_text = process_uploaded_file(file_path)
        elif arxiv_url:
            st.info("Processing the ArXiv URL...")
            extracted_text = process_arxiv_url(arxiv_url)

        # Ensure extracted text is valid
        if not extracted_text.strip():
            st.error("No text could be extracted from the provided file or URL.")
            return

        # Process the extracted text with LangChain RAG pipeline
        st.info("Processing the document...")
        qa_chain = run_rag_pipeline(documents_directory, vector_store_path)
        chunks = qa_chain.retriever.vectorstore.docstore._dict
        all_content = " ".join(chunk.page_content for chunk in chunks.values())

        # Split content into smaller chunks for summarization
        chunk_size = 1000
        small_chunks = [
            all_content[i:i + chunk_size]
            for i in range(0, len(all_content), chunk_size)
        ]

        # Summarize each chunk
        summaries = []
        for small_chunk in small_chunks:
            prompt = f"Summarize the following text concisely:\n\n{small_chunk}"
            summary = qa_chain.run(prompt)
            summaries.append(summary)

        # Combine summaries into a final summary
        final_summary = " ".join(summaries)
        st.subheader("Document Summary")
        st.write(final_summary)

    except Exception as e:
        st.error(f"Error summarizing the document: {e}")
