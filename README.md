# InsightMate - AI Document Analyst

InsightMate is an AI-powered document analysis tool that helps users understand and interact with their documents through smart summarization, contextual Q&A, and key insights extraction.

## Features

- 📄 Document Upload (PDF and TXT)
- 📝 Smart Summarization
- 💬 Contextual Q&A
- 🔍 Semantic Search
- 🎯 Key Insights Extraction

## Architecture

The application is built using:

- **Frontend**: Streamlit
- **LLM**: Google's Gemini Pro
- **Vector Database**: ChromaDB
- **Document Processing**: PyMuPDF

## Setup

1. Clone the repository:

```bash
git clone <repository-url>
cd insightmate
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your Google API key:

```
GOOGLE_API_KEY=your_api_key_here
```

5. Run the application:

```bash
streamlit run app.py
```

## Usage

1. Open the application in your web browser (default: http://localhost:8501)
2. Upload a PDF or text document
3. View the AI-generated summary
4. Ask questions about the document content
5. Get insights and answers in real-time

## Project Structure

```
insightmate/
├── app.py              # Main application file
├── requirements.txt    # Project dependencies
├── .env               # Environment variables
└── db/                # ChromaDB storage directory
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
