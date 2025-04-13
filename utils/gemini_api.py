import os
import google.generativeai as genai
from dotenv import load_dotenv
import numpy as np
from typing import List, Dict, Any

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_summary(text: str) -> str:
    """
    Generate a summary of the given text using Gemini Pro.
    """
    model = genai.GenerativeModel('gemini-pro')
    prompt = f"Please provide a concise summary of the following text:\n\n{text}"
    response = model.generate_content(prompt)
    return response.text


def generate_embeddings(text: str) -> List[float]:
    """
    Generate embeddings for the given text using Gemini Pro.
    """
    model = genai.GenerativeModel('gemini-pro')
    prompt = f"Generate embeddings for the following text:\n\n{text}"
    response = model.generate_content(prompt)
    # Convert the response to a list of floats
    # Note: This is a placeholder implementation. In practice, you might want to use
    # a dedicated embedding model or API
    return [float(x) for x in response.text.split()]


def answer_question(question: str, context: str) -> str:
    """
    Answer a question based on the given context using Gemini Pro.
    """
    model = genai.GenerativeModel('gemini-pro')
    prompt = f"Based on the following context, please answer the question:\n\nContext: {context}\n\nQuestion: {question}"
    response = model.generate_content(prompt)
    return response.text
