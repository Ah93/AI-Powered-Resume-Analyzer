import google.generativeai as genai
from prompts import resume_analysis_prompt, match_resume_to_job
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-flash")

def analyze_resume(resume_text):
    prompt = resume_analysis_prompt(resume_text)
    response = model.generate_content(prompt)
    return response.text

def match_resume(resume_text, job_description):
    prompt = match_resume_to_job(resume_text, job_description)
    response = model.generate_content(prompt)
    return response.text