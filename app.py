import streamlit as st
from resume_parser import extract_text
from scorer import calculate_score

st.title("AI Resume Screening Tool")

st.write("Upload Resume and Paste Job Description")

resume_file = st.file_uploader("Upload Resume (PDF/DOCX)")

jd_text = st.text_area("Paste Job Description")

if resume_file and jd_text:
    resume_text = extract_text(resume_file)
    score = calculate_score(resume_text, jd_text)
    
    st.subheader("Match Score")
    st.success(f"{score}% Match")
    
    if score > 75:
        st.write("Strong Match Profile")
    elif score > 50:
        st.write("Moderate Match - Improve Skills")
    else:
        st.write("Low Match - Add Relevant Skills")
