# Resume-CV Question RAG

This project implements a Retrieval-Augmented Generation (RAG) system to generate interview questions based on resumes or CVs. It uses the Gemini API for language generation, LangChain for building the RAG pipeline, and Streamlit for a user-friendly web interface. The system extracts key information (e.g., skills, experience, education) from resume PDFs and generates tailored interview questions, which can be accessed via a web application.

## Deployed Link
https://resume-cvquestionrag-2ipmznral3tjqtyhgdejy8.streamlit.app/

## Table of Contents
- [Project Overview](#project-overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)

## Project Overview

The Resume-CV Question RAG project leverages a Retrieval-Augmented Generation (RAG) model to:
- Extract key information from resume or CV PDFs using LangChain's document processing capabilities.
- Generate relevant and personalized interview questions using the Gemini API.
- Provide a web interface built with Streamlit for users to upload resumes and view generated questions.

The project includes a web app (`app.py`) for production use and a Jupyter notebook (`rag_gemini.ipynb`) for development, experimentation, and model fine-tuning. Recent commits indicate the system is focused on an "Interview RAG Generator."

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- Git (for version control)
- (Optional) Jupyter Notebook (for running `rag_gemini.ipynb`)

You will also need:
- A Gemini API key from Google AI Studio for language generation.
- Streamlit for the web interface.
- LangChain for building the RAG pipeline.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Fazeel-AIML/Resume-CV_Question_RAG
   cd Resume-CV_Question_RAG
2. Python dependencies
   ```bash
   pip install -r requirements.txt
3. Set up environment variable
   ```bash
   GEMINI_API_KEY=<your-gemini-api-key>

## Running Streamlit App
streamlit run app.py
