import streamlit as st
import re
from pdf_reader import extract_text_from_pdf
from resume_analyzer import analyze_resume, match_resume

st.markdown(
    """
    <h1 style='text-align: center; color: #007BFF;'>
        📄 AI-Powered Resume Analyzer and Job Matcher
    </h1>

     <style>
    /* --- Global App Style --- */
    .stApp {
        background-color: #f5f5f5;
        font-family: 'Segoe UI', sans-serif;
        padding: 1rem;
    }

    /* --- Headings --- */
    h1, h2, h3, h4 {
        color: #007BFF;
    }

    /* --- Buttons --- */
    .stButton > button {
        background-color: #007BFF;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        border: none;
        font-weight: 600;
        transition: background-color 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #0056b3;
    }

    /* --- File Uploader & Text Area Borders --- */
    .stTextArea, .stFileUploader, .stTextInput {
        border-radius: 10px;
    }

    /* --- Expander Panels --- */
    details > summary {
        font-size: 1rem;
        font-weight: 600;
        color: #007BFF;
    }
    details {
        background-color: #ffffff;
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 0.5rem;
        margin-bottom: 0.75rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }

    /* --- Code/Text Blocks --- */
    pre {
        background-color: #f0f0f0;
        padding: 0.75rem;
        border-radius: 8px;
        overflow-x: auto;
    }

    /* --- Scrollbar Styling (Optional) --- */
    ::-webkit-scrollbar {
        width: 10px;
    }
    ::-webkit-scrollbar-track {
        background: #f5f5f5;
    }
    ::-webkit-scrollbar-thumb {
        background-color: #007BFF;
        border-radius: 10px;
    }
    </style>
    
    """,
    unsafe_allow_html=True
)

# --- Helper Functions ---
def extract_match_score(text):
    match = re.search(r"Match Score.*?(\d{1,3})", text)
    return int(match.group(1)) if match else None

def display_analysis_report(report_text):
    sections = report_text.strip().split("\n\n")
    for section in sections:
        lines = section.strip().split("\n")
        if len(lines) > 1:
            title = lines[0].strip(" :")
            content = "\n".join(lines[1:])
            with st.expander(f"📌 {title}"):
                st.markdown(f"```text\n{content}\n```")

def display_match_report(report_text):
    score = extract_match_score(report_text)
    if score is not None:
        color = "green" if score >= 80 else "orange" if score >= 50 else "red"
        st.markdown(
            f"### 🎯 Match Score: <span style='color:{color}; font-size: 24px;'>{score}/100</span>",
            unsafe_allow_html=True
        )
    else:
        st.markdown("### 🎯 Match Score: N/A")

    sections = report_text.strip().split("\n\n")
    for section in sections:
        lines = section.strip().split("\n")
        if len(lines) > 1:
            title = lines[0].strip(" :")
            content = "\n".join(lines[1:])
            with st.expander(f"📌 {title}"):
                st.markdown(f"```text\n{content}\n```")

# --- Upload Resume Once ---
st.header("📤 Upload Resume (PDF only)")
uploaded_file = st.file_uploader("Upload your resume to use for both analysis and matching", type="pdf")

if uploaded_file:
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())
    resume_text = extract_text_from_pdf("temp_resume.pdf")

    if len(resume_text) < 100:
        st.warning("⚠️ Resume text is too short or not extracted properly.")
    else:
        st.success("✅ Resume uploaded and ready for analysis and matching.")

        # --- Two Columns: Separate Functionalities ---
        col1, col2 = st.columns(2)

        # --- Resume Analyzer ---
        with col1:
            st.header("🔍 Resume Analyzer")
            if st.button("Analyze Resume"):
                with st.spinner("Analyzing resume..."):
                    analysis = analyze_resume(resume_text)
                    st.subheader("📊 Resume Insights & Feedback")
                    display_analysis_report(analysis)

        # --- Resume Matcher ---
        with col2:
            st.header("🎯 Resume Matcher")
            job_desc = st.text_area("Paste Job Description Here", height=200)

            if st.button("Match to Job Description"):
                if not job_desc.strip():
                    st.warning("❗ Please paste a job description.")
                else:
                    with st.spinner("Matching resume to job description..."):
                        match_result = match_resume(resume_text, job_desc)
                        st.subheader("📊 Job Match Report")
                        display_match_report(match_result)
