<<<<<<< HEAD
# Multimodal LLM Chatbot

A professional, extensible Streamlit-based chatbot platform for multimodal AI interactions. This project enables users to interact with documents, images, and audio using advanced NLP and vision models, supporting document Q&A, summarization, image captioning, visual question answering, and audio features.

---

## Features

- **Ask Questions**: Upload PDFs/CSVs or provide ArXiv URLs, then ask questions via text or voice. Answers are generated using a Retrieval-Augmented Generation (RAG) pipeline.
- **Summarize Document**: Summarize uploaded documents or ArXiv papers using state-of-the-art language models.
- **Image Captioning**: Generate captions for uploaded images.
- **Visual Question Answering (VQA)**: Ask questions about images and receive intelligent answers.
- **Image Text QA**: Extract text from images and ask questions about the extracted content.
- **Audio Support**: Transcribe spoken questions and listen to generated answers.

---

## Directory Structure

```
.
├── app.py
├── requirements.txt
├── thinking.md
├── audio/
│   ├── stt.py
│   └── tts.py
├── config/
│   └── settings.py
├── data/
│   ├── index/
│   └── uploads/
├── features/
│   ├── ask_questions.py
│   ├── image_captioning.py
│   ├── image_text_qa.py
│   ├── summarize_document.py
│   └── visual_question_answering.py
├── models/
│   ├── image_captioning.py
│   ├── langchain_rag.py
│   ├── memory.py
│   ├── multimodal_vqa.py
│   └── ocr_text_extraction.py
├── preprocessors/
│   ├── arxiv_processor.py
│   ├── csv_processor.py
│   └── pdf_processor.py
├── static/
│   └── logo.png
├── ui/
│   ├── chat_ui.py
│   └── layout.py
├── utils/
│   ├── file_handler.py
│   └── file_manager.py
├── vector_store/
│   ├── index.faiss
│   └── index.pkl
```

---

## Getting Started

### 1. Clone the Repository

```powershell
git clone https://github.com/Mo-Refaat/LLM_ChatBot.git
cd llm_chatbot_project
```

### 2. Create and Activate a Virtual Environment

```powershell
python -m venv venv
.\venv\Scripts\Activate
```

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory and add your HuggingFace API token:

```
HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token
```

### 5. Prepare Data Directories

Ensure the following directories exist (they will be created automatically if missing):
- `data/uploads/` — for uploaded files
- `data/index/` — for vector store indices

### 6. Run the Application

```powershell
streamlit run app.py
```

---

## Usage

- Select a feature from the sidebar (e.g., Ask Questions, Summarize Document, Image Captioning, etc.).
- Follow the on-screen instructions to upload files, images, or use audio input.
- For document-based features, upload a PDF/CSV or provide an ArXiv URL.
- For image-based features, upload an image (JPG/PNG).
- For audio features, use your microphone to ask questions or listen to answers.

---

## Core Technologies

- **Streamlit**: Interactive web UI
- **LangChain**: RAG pipeline for document Q&A
- **HuggingFace Transformers**: Language and vision models
- **FAISS**: Vector store for efficient retrieval
- **SpeechRecognition & TTS**: Audio input/output
- **PyPDFLoader**: PDF document parsing

---

## File Overview

- `app.py`: Main entry point, handles routing and UI initialization.
- `features/`: Contains Streamlit page logic for each feature.
- `models/langchain_rag.py`: Implements the RAG pipeline and vector store logic.
- `audio/`: Speech-to-text and text-to-speech utilities.
- `config/settings.py`: Loads configuration and API tokens.
- `ui/layout.py`: UI layout and sidebar setup.
- `utils/`: File handling and utility functions.
- `preprocessors/`: Document and data preprocessing modules.

---

## Customization

- **Add New Features**: Create a new file in `features/` and add it to the sidebar in `app.py`.
- **Change Models**: Update model names in `models/langchain_rag.py` or relevant feature files.
- **UI Customization**: Modify `ui/layout.py` for branding and layout changes.

---

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements and new features.

---

## License

This project is licensed under the MIT License.

---

## Contact

- **Email**: [Mohamed Refaat](mailto:morefaat356@gmail.com)

---

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [HuggingFace](https://huggingface.co/)
- [LangChain](https://python.langchain.com/)
- [FAISS](https://faiss.ai/)
=======
# LLM_ChatBot
A professional, extensible Streamlit-based chatbot platform for multimodal AI interactions. This project enables users to interact with documents, images, and audio using advanced NLP and vision models, supporting document Q&amp;A, summarization, image captioning, visual question answering, and audio features.
>>>>>>> c2df89f71062775f76da4c317c5a8664894c735a
