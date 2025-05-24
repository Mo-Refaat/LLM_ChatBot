import os
import requests
import streamlit as st
from config.settings import HUGGINGFACEHUB_API_TOKEN

def visual_question_answering_page():
    """
    Streamlit page for Visual Question Answering (VQA).
    """
    st.title("Visual Question Answering")
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png"])
    question = st.text_input("Ask a question about the image")

    if st.button("Submit"):
        if not uploaded_image or not question:
            st.error("Please upload an image and enter a question.")
            return

        try:
            # Save the uploaded image
            image_path = os.path.join("data/uploads", uploaded_image.name)
            with open(image_path, "wb") as f:
                f.write(uploaded_image.read())

            # Display the image
            st.image(image_path, caption="Uploaded Image", use_container_width=True)

            # Read the image in binary format
            with open(image_path, "rb") as image_file:
                image_binary = image_file.read()

            # Send the image and question to the VQA model
            api_url = "https://api-inference.huggingface.co/models/Salesforce/blip-vqa-base"
            headers = {"Authorization": f"Bearer {HUGGINGFACEHUB_API_TOKEN}"}
            files = {"image": ("image.jpg", image_binary, "application/octet-stream")}
            data = {"question": question}

            response = requests.post(api_url, headers=headers, files=files, data=data)

            if response.status_code == 200:
                result = response.json().get("generated_text", "No answer found.")
                st.subheader("Answer")
                st.write(result)
            else:
                st.error(f"VQA API request failed: {response.status_code}, {response.text}")

        except Exception as e:
            st.error(f"Error processing the VQA: {e}")
