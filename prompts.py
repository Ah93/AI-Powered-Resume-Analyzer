# prompts.py

# Prompt to analyze a resume and extract insights
def resume_analysis_prompt(resume_text):
    return f"""
You are a resume evaluation assistant. Please extract the following details:

1. Full Name
2. Contact Information (if available)
3. Total Years of Experience
4. Top 10 Technical Skills
5. Top 5 Soft Skills
6. Education Background
7. Certifications
8. Summary of Experience
9. Strengths
10. Weaknesses or Missing Information
11. Feedback for improvement

Resume:
\"\"\"
{resume_text}
\"\"\"
"""

# Prompt to compare resume with a job description and give a match score
def match_resume_to_job(resume_text, job_description):
    return f"""
You are a resume-to-job matching assistant.

Compare the following resume with the job description and provide:

1. **Match Score** (0–100)
2. **Matched Skills**
3. **Missing Skills**
4. **Recommendation Summary**
5. **Suitability Conclusion**

Resume:
\"\"\"
{resume_text}
\"\"\"

Job Description:
\"\"\"
{job_description}
\"\"\"
"""