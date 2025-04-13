# Truth or Dare AI 🎲

An AI-powered interactive Truth or Dare game that adapts to player preferences, offering personalized questions and dares based on intensity levels and player demographics.

## Features

- 🎯 Multiple intensity levels (mild, funny, spicy, drunk)
- 👥 Gender-specific and all-gender questions
- 🤖 AI-powered content generation
- 🎮 Interactive gameplay
- 🎨 Modern, responsive UI

## Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **AI**: Google's Gemini Pro API
- **Version Control**: Git

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd truth-or-dare-ai
```

2. Create and activate a virtual environment:

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
2. Select your preferred intensity level
3. Choose your demographic preferences
4. Start playing and enjoy the AI-generated questions and dares!

## Project Structure

```
truth-or-dare-ai/
├── app.py              # Main application file
├── requirements.txt    # Project dependencies
├── .env               # Environment variables
└── .gitignore         # Git ignore file
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Google's Gemini Pro API for AI capabilities
- Streamlit for the web framework
- All contributors and testers
