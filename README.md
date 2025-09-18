#  Document-based Question Answering System (GenAI)

##  Objective

This project allows users to upload documents (PDFs or Word files) and ask questions based on the content. It uses **LangChain, OpenAI GPT-4, and ChromaDB** to provide intelligent, context-aware answers.

---

##  Tech Stack

* Python
* Streamlit (for UI)
* LangChain (for LLM orchestration)
* OpenAI GPT-4 (for answer generation)
* ChromaDB (for vector storage & search)

---

##  Features

*  Upload PDF or DOCX files
*  Document chunking + vector embeddings
*  Context-aware answer generation using GPT-4
*  Simple and professional UI

---

##  Installation & Usage

### 1. Clone or Download the Project

```bash
git clone https://github.com/your-username/doc-qa-app.git
cd doc-qa-app
```

Or just download the ZIP and extract it.

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Set up API Key

Create a file named **`.env`** in the project folder and add your OpenAI API key:

```
OPENAI_API_KEY=sk-your-api-key
```

---

### 4. Run the App

```bash
streamlit run app.py
```

Then open the local URL (shown in terminal) in your browser.

---

##  Use Case

This tool is useful in:

*  Legal firms (for analyzing contracts & case files)
*  Educational platforms (for summarizing study material)
*  Knowledge management (for company documents & reports)

---

##  Author

Developed by **Maryam Hamza**

---


