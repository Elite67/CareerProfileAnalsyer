import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyDAlgnjMS54hi0S1zbbhScRi5BYZZ1dLVU")
model = genai.GenerativeModel("gemini-2.0-flash")

def AI(current_cgpa, company_name, skills):
    prompts = {
        "Eligibility Check 🟢": f"""
            Analyze the student's eligibility for the specified dream company based on their CGPA and skills.

            **Student Profile:**
            - CGPA: {current_cgpa}
            - Dream Company: {company_name}
            - Skills: {skills}

            **Analysis Required:**
            - Check if the student meets the eligibility criteria for the dream company based on their CGPA and skills.
            - Provide insights on whether the student is a good fit for the company and why or why not.
        """,
        "Skill Gap Analysis 🔍": f"""
            Identify the skill gaps in the student's profile for the dream company based on their skills and CGPA.

            **Student Profile:**
            - CGPA: {current_cgpa}
            - Dream Company: {company_name}
            - Skills: {skills}

            **Analysis Required:**
            - List any skills or areas where the student might be lacking for the specified company.
            - Suggest areas for improvement that would make the student more competitive for the company.
        """,
        "Suggested Roles 🎯": f"""
            Based on the student's profile, recommend roles within the specified dream company that they may be well-suited for.

            **Student Profile:**
            - CGPA: {current_cgpa}
            - Dream Company: {company_name}
            - Skills: {skills}

            **Analysis Required:**
            - Suggest roles the student could apply for at the dream company based on their CGPA and skills.
            - Provide reasoning for why each role might be a good fit for the student.
        """,
        "Similar Companies 🏢": f"""
            Recommend similar companies to the student's dream company based on their profile and career interests.

            **Student Profile:**
            - CGPA: {current_cgpa}
            - Dream Company: {company_name}
            - Skills: {skills}

            **Analysis Required:**
            - Suggest similar companies to the dream company that the student might also want to consider based on their CGPA and skills.
            - Provide reasoning for why each company might be a good match for the student.
        """,
        "Learning Suggestions 📚": f"""
            Provide learning suggestions to improve the student's profile for the dream company.

            **Student Profile:**
            - CGPA: {current_cgpa}
            - Dream Company: {company_name}
            - Skills: {skills}

            **Analysis Required:**
            - Suggest any courses, certifications, or resources that would help improve the student's skills for the dream company.
            - Recommend learning paths or areas of focus that will enhance the student's profile and competitiveness.
        """,
        "Interview Topics 💬": f"""
            Provide common interview topics for the specified dream company based on the student's profile.

            **Student Profile:**
            - CGPA: {current_cgpa}
            - Dream Company: {company_name}
            - Skills: {skills}

            **Analysis Required:**
            - Suggest common interview topics or questions the student might encounter in an interview with the dream company.
            - Focus on topics that align with the student's skills and the company's job requirements.
        """,
        "Alternative Career Paths 🌱": f"""
            Recommend alternative career paths or roles based on the student's profile, in case they want to explore other options.

            **Student Profile:**
            - CGPA: {current_cgpa}
            - Dream Company: {company_name}
            - Skills: {skills}

            **Analysis Required:**
            - Suggest alternative career options or industries the student might explore based on their skills, CGPA, and interests.
            - Provide reasoning for why these paths could be a good fit.
        """,
        "Company Comparison ⚖️": f"""
            Compare the student's eligibility and fit for multiple companies, including the dream company and others based on their skills and CGPA.

            **Student Profile:**
            - CGPA: {current_cgpa}
            - Dream Company: {company_name}
            - Skills: {skills}

            **Analysis Required:**
            - Compare eligibility and career fit for multiple companies the student is considering.
            - Provide reasoning for each comparison based on the student's skills and CGPA.
        """,
        "Resume Optimization 📄": f"""
            Provide tips and suggestions to optimize the student's resume for the dream company.

            **Student Profile:**
            - CGPA: {current_cgpa}
            - Dream Company: {company_name}
            - Skills: {skills}

            **Analysis Required:**
            - Suggest improvements and formatting tips to enhance the student's resume.
            - Recommend key areas to highlight based on the company’s requirements and the student's profile.
        """,
        "Internship Opportunities 🧑‍💻": f"""
            Suggest internship opportunities or programs that the student could apply for to improve their chances of getting into the dream company.

            **Student Profile:**
            - CGPA: {current_cgpa}
            - Dream Company: {company_name}
            - Skills: {skills}

            **Analysis Required:**
            - Recommend internships or programs that can help the student gain relevant experience for the dream company.
            - Provide reasoning for why each suggestion aligns with the student's profile.
        """
    }

    return [model.generate_content(prompt).text.replace("*", "") for prompt in prompts.values()], list(prompts.keys())

st.title("📄 Student Career Profile Analysis")

with st.form("job_form"):
    st.write("📌 **Enter your current details!**")
    current_cgpa = st.text_input("Current CGPA:", placeholder="0 - 10")
    company_name = st.text_input("Dream Company Name:", placeholder="e.g. Google")
    skills = st.text_input("Current Skills:", placeholder="e.g. Python, React, SQL")
    submit = st.form_submit_button("Submit")
    if submit:
        st.success("✅ Form Submitted!")

if submit:
    content_placeholder = st.empty()
    content_placeholder.text("Talking to Gemini... Please wait...")

    results, headings = AI(current_cgpa, company_name, skills)
    content_placeholder.text("✅ Analysis Generated!")

    for heading, result in zip(headings, results):
        with st.expander(f"**{heading}**"):
            st.markdown(f"### {heading}")
            st.markdown(f"<div style='font-size: 16px; font-weight: bold'>{result}</div>", unsafe_allow_html=True)
