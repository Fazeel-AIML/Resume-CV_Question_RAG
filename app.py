import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_core.prompts import ChatPromptTemplate
from langchain.docstore.document import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from google.api_core.exceptions import ResourceExhausted  # Import error handling
from dotenv import load_dotenv
import PyPDF2

# Load environment variables
load_dotenv()

# Initialize LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.3, max_tokens=500)

# Streamlit app title
st.title("Resume Interview Question Generator")
st.write("Upload your resume, and the app will generate possible interview questions and answers.")

# File uploader
uploaded_file = st.file_uploader("Upload your resume (PDF or TXT)", type=["pdf", "txt"])

if uploaded_file:
    # Read resume content
    if uploaded_file.type == "application/pdf":
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        resume_text = "\n".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
    else:
        resume_text = uploaded_file.read().decode("utf-8")

    st.subheader("Resume Content:")
    st.write(resume_text)

    # Create document and embeddings
    docs = [Document(page_content=resume_text)]
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_documents(docs, embeddings)
    retriever = vector_store.as_retriever(search_kwargs={"k": 3}, search_type="similarity")

    # Create RetrievalQA chain
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    # Generate interview questions
    st.subheader("Generated Interview Questions:")
    questions_query = "Generate 5 interview questions based on this resume."

    try:
        questions_response = qa_chain.invoke(questions_query)

        # Extract actual text from the response
        if isinstance(questions_response, dict) and "result" in questions_response:
            questions_text = questions_response["result"]
        else:
            questions_text = str(questions_response)

        st.write(questions_text)

        # Generate answers
        st.subheader("Interview Answers:")
        for idx, question in enumerate(questions_text.split("\n"), 1):
            if question.strip():
                st.write(f"**Q{idx}: {question}**")
                
                try:
                    answer_response = qa_chain.invoke(f"Answer this question: {question}")
                    
                    if isinstance(answer_response, dict) and "result" in answer_response:
                        answer_text = answer_response["result"]
                    else:
                        answer_text = str(answer_response)

                    st.write(f"**A{idx}: {answer_text}**")

                except ResourceExhausted:
                    st.error("❌ API quota exceeded! Please try again later or use a different API key.")

    except ResourceExhausted:
        st.error("❌ API quota exceeded! Please check your Google Gemini API usage or upgrade your plan.")
