# 📚 PaperTrail AI — Research Paper Explorer

PaperTrail AI is a Python-based web application that helps users explore technical research papers through PDF text extraction, keyword search, page-level results, and relevance-based ranking.

Built with **Python, Streamlit, and PyMuPDF**, the application provides a simple interface for uploading multiple research papers, searching their contents, identifying relevant passages, and downloading search reports.

## 🚀 Live Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://papertrail-ai-pxaixmabi25jrmhlvyszw4.streamlit.app/)

Try PaperTrail AI: [Open the live application](https://papertrail-ai-pxaixmabi25jrmhlvyszw4.streamlit.app/)

Upload research PDFs, search their contents, explore page-level results, filter and rank matching papers, and download search reports.

## ✨ Features

- **Multiple PDF Uploads:** Upload multiple research papers through the web interface.
- **PDF Text Extraction:** Extract readable text from uploaded PDF documents using PyMuPDF.
- **Research Library:** View uploaded paper filenames, page counts, and extracted character counts.
- **Library Dashboard:** View summary metrics for the uploaded documents.
- **Keyword Search:** Search for words or phrases across uploaded research papers.
- **Case-Insensitive Matching:** Find matches regardless of capitalization.
- **Page-Level Results:** Display the page number and matching text for each result.
- **Paper Selection:** Search all uploaded papers or select specific documents.
- **Relevance-Based Ranking:** Rank papers by the number of matching lines, with higher counts appearing first.
- **Minimum-Match Filtering:** Show only papers that meet a specified minimum number of matching lines.
- **Search Metrics:** Display the total matching lines and number of papers returned.
- **Downloadable Reports:** Export search results as a plain-text report containing the query, document names, page numbers, and matching passages.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Streamlit | Interactive web interface |
| PyMuPDF | PDF reading and text extraction |
| Git and GitHub | Version control and project hosting |

## 📁 Project Structure

```text
PaperTrail-AI/
├── app.py              # Main Streamlit web application
├── main.py             # Command-line search prototype, if retained
├── README.md           # Project documentation
├── .gitignore          # Excludes local and unnecessary files
├── requirements.txt    # Python dependencies, if added
├── papers/             # Optional local testing documents
└── .venv/               # Local Python virtual environment
```

The `.venv/` directory is created locally and should not be committed to GitHub. The `main.py` and `requirements.txt` files should be included only if they exist in the repository.

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or a compatible newer Python version
- Git
- A web browser

### 1. Clone the repository

Replace `YOUR_USERNAME` with your GitHub username after creating the repository.

```bash
git clone https://github.com/YOUR_USERNAME/PaperTrail-AI.git
cd PaperTrail-AI
```

### 2. Create a virtual environment

**Windows — PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS or Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install the dependencies

If a `requirements.txt` file is available:

```bash
python -m pip install -r requirements.txt
```

Alternatively, install the required packages directly:

```bash
python -m pip install streamlit pymupdf
```

### 4. Run the application

From the project root, execute:

```bash
python -m streamlit run app.py
```

Streamlit will provide a local URL, usually:

```text
http://localhost:8501
```

Open that URL in your browser to access PaperTrail AI.

## 🚀 How to Use

1. Launch the application.
2. Upload one or more research paper PDFs.
3. Explore the research library and dashboard statistics.
4. Select which papers to search, or keep all papers selected.
5. Enter a keyword or phrase in the search field.
6. Set the minimum number of matching lines required for a paper to appear.
7. Review the ranked results, including filenames, page numbers, and matching passages.
8. Download the search report for offline reference.

## 🔍 How Search and Ranking Work

PaperTrail AI extracts text from each uploaded PDF and checks the extracted lines for the requested keyword or phrase.

Matching is **case-insensitive**. For example, `Machine Learning` and `machine learning` are treated as equivalent queries.

Each matching line is associated with its document and page number. The application groups results by paper and ranks papers according to their number of matching lines.

The minimum-match filter excludes papers that do not meet the selected threshold.

This is a basic, count-based ranking method. It does not calculate semantic similarity or determine whether a paper is scientifically relevant to the query.

## 📄 Search Reports

Search reports can be downloaded as `.txt` files. They include the search keyword, selected matching papers, matching-line counts, page references, and extracted passages.

The reports are useful for keeping a record of results and revisiting relevant sections of research papers.

## ⚠️ Current Limitations

- **Keyword-based search:** The application searches for literal words or phrases rather than understanding the meaning of a query.
- **Basic ranking:** Papers with more matching lines are ranked higher; this does not necessarily mean they are more relevant.
- **Scanned PDFs:** Documents containing only scanned images may require OCR before their text can be searched.
- **Text extraction quality:** Reading order, formulas, tables, and multi-column layouts may not be preserved perfectly.
- **Session-based uploads:** Uploaded files and extracted text are processed in the running application and are not persistently stored by this version.
- **No LLM integration:** AI-generated summaries, conversational question answering, and source-grounded responses are not currently implemented.

## 🔮 Future Improvements

Potential extensions include:

- Semantic search using text embeddings.
- Research paper summaries and key-point extraction.
- Conversational question answering grounded in retrieved passages.
- Citations linking generated answers to source pages.
- Improved ranking using TF-IDF or BM25.
- OCR support for scanned research papers.
- Persistent document indexing for larger research collections.
- Automated evaluation of retrieval quality.

These are planned improvements, not features of the current implementation.

## 🎯 Project Objective

The objective of PaperTrail AI is to simplify the process of locating information in technical documents and provide a foundation for building more advanced research-assistance tools.

The project also provides practical experience with Python application development, PDF processing, text search, data handling, and interactive web interfaces.

## 👨‍💻 Author

**Pratham Shetty K**

Electronics and Communication Engineering

GitHub: https://github.com/PrathamShetty-Sahyadri-ECE

LinkedIn: https://www.linkedin.com/in/pratham-shetty-105118284/

