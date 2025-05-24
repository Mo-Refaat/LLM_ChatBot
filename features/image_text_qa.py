import os
import streamlit as st
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import HuggingFaceHub
from models.ocr_text_extraction import extract_text_from_image
from config.settings import HUGGINGFACEHUB_API_TOKEN

def image_text_qa_page(documents_directory, vector_store_path):
    """
    Handles Image Text Extraction and QA.
    """
    st.header("Image Text QA Feature")

    # File Upload Section
    uploaded_image = st.file_uploader("Upload an image for OCR + QA", type=["jpg", "png"])
    if uploaded_image:
        # Save the uploaded image
        file_path = os.path.join(documents_directory, uploaded_image.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_image.read())

        # Display the uploaded image
        st.image(file_path, caption="Uploaded Image", use_container_width=True)

        # Extract text using OCR
        st.info("Extracting text from the image...")
        try:
            extracted_text = extract_text_from_image(file_path)
            st.subheader("Extracted Text")
            st.write(extracted_text)

            # Check if extracted text is valid
            if not extracted_text.strip():
                st.error("No text found in the image.")
                return

            # Set up LangChain QA pipeline
            embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
            text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
            chunks = text_splitter.split_text(extracted_text)

            # Convert chunks into LangChain document objects
            docs = [{"page_content": chunk} for chunk in chunks]

            # Create vector store
            vector_store = FAISS.from_documents(
                documents=docs,
                embedding=embeddings
            )

            # Define the QA chain
            qa_chain = RetrievalQA.from_chain_type(
                llm=HuggingFaceHub(
                    repo_id="google/flan-t5-large",
                    huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN,
                    model_kwargs={"temperature": 0.3, "max_new_tokens": 100}
                ),
                retriever=vector_store.as_retriever()
            )

            # Ask a question
            question = st.text_input("Enter your question about the extracted text")
            if st.button("Ask"):
                answer = qa_chain.run(question)
                st.subheader("Answer")
                st.write(answer)

        except Exception as e:
            st.error(f"Error processing the image: {e}")
    else:
        st.info("Please upload an image to start.")
