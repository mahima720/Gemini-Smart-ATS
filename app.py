import streamlit as st
import os
from google import genai  
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

load_dotenv()

# Initialize the GenAI Client (picks up GOOGLE_API_KEY or GEMINI_API_KEY from env)
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_repsonse(input_text):
    # Using 'gemini-2.0-flash' or 'gemini-1.5-pro' for best results in 2026
    response = client.models.generate_content(
        model='gemini-3-flash-preview',
        contents=input_text
    )
    return response.text

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += str(page.extract_text())
    return text

# Prompt Template
input_prompt = """
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field, software engineering, data science, data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving the resumes. Assign the percentage Matching based 
on JD and the missing keywords with high accuracy.

resume:{text}
description:{jd}

I want the response in one single string having the structure
{{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
"""

## streamlit app
st.title("Smart ATS 🤖")
st.text("Improve Your Resume for the Modern Job Market")

jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the pdf")

submit = st.button("Submit Analysis")

if submit:
    if uploaded_file is not None and jd:
        with st.spinner("Analyzing Resume..."):
            resume_text = input_pdf_text(uploaded_file)
            # Format the prompt with actual data
            formatted_prompt = input_prompt.format(text=resume_text, jd=jd)
            
            response = get_gemini_repsonse(formatted_prompt)
            
            st.subheader("ATS Analysis Results:")
            st.markdown(response)
    else:
        st.warning("Please upload a resume and paste the Job Description.")