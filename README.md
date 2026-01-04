# 🤖 Smart ATS: Resume Optimization Assistant

A powerful, AI-driven Applicant Tracking System (ATS) simulator designed to help job seekers optimize their resumes for highly competitive tech roles. Using Google Gemini, this app analyzes your resume against a specific Job Description (JD) to provide a match percentage, identify missing keywords, and suggest profile improvements.

# 🔗 Live Demo
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://gemini-smart-ats.streamlit.app/)

![UI](/images/image1.png)

## Features

* **📄 PDF Text Extraction:** Seamlessly reads and parses complex Resume data from PDF files.
* **🎯 Precision Matching:** Assigns a "JD Match" percentage based on skills, experience, and role requirements.
* **🔍 Keyword Gap Analysis:** Identifies critical technical and soft skills missing from your resume.
* **📝 Professional Summary:** Provides an AI-generated profile summary to help you stand out in the job market.
* **⚡ Modern Tech Stack:** Leverages the high-context window of Gemini 2.0/3.0 for deep document understanding.

![Working](/images/image2.png)

## Skills Showcased

* **Python** Core programming language
* **Streamlit**	Frontend framework for the web interface
* **Google GenAI** Accessing the gemini-3-flash-preview model
* **Python-Dotenv** Secure management of API keys
* **Prompt Engineering** Learned the art of System Prompting to guide AI behavior 

## 🚀 Getting Started

Follow these steps to set up the project on your local machine:

**1. Clone the Repository** 

    git clone <your-repository-url>
    cd <your-project-folder>
**2. Install Dependencies**

    pip install -r requirements.txt

**3. Set Up Your API Key**

    Get an API key from Google AI Studio.
    Create a file named .env in your project root.
    Add your key to the file:
    Code snippet
    GOOGLE_API_KEY=your_secret_api_key_here

**4. Run the App**

    streamlit run your_filename.py

## Conclusion

Smart ATS is a testament to how Generative AI can democratize access to career tools that were previously only available to recruiters. By providing transparent feedback on how an algorithm might view a resume, this tool empowers candidates to tailor their applications with data-driven precision, significantly increasing their chances of landing interviews in a competitive market.