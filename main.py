import streamlit as st
import google.generativeai as genai
import concurrent.futures
import matplotlib.pyplot as plt
import numpy as np

genai.configure(api_key="AIzaSyDAlgnjMS54hi0S1zbbhScRi5BYZZ1dLVU")
model = genai.GenerativeModel("gemini-2.0-flash")

def generate_prompt_response(prompt):
    return model.generate_content(prompt).text.replace("*", "").strip()

def AI(current_cgpa, company_name, skills):
    prompts = {
        "Eligibility Check 🟢": f"""Analyze the student's eligibility for the specified dream company based on their CGPA and skills.
        - CGPA: {current_cgpa}
        - Dream Company: {company_name}
        - Skills: {skills}
        """,
        "Skill Gap Analysis 🔍": f"""Identify the skill gaps in the student's profile for the dream company.
        - CGPA: {current_cgpa}
        - Dream Company: {company_name}
        - Skills: {skills}
        """,
        "Suggested Roles 🎯": f"""Suggest roles within the specified dream company.
        - CGPA: {current_cgpa}
        - Dream Company: {company_name}
        - Skills: {skills}
        """,
        "Similar Companies 🏢": f"""Recommend similar companies to the dream company.
        - CGPA: {current_cgpa}
        - Dream Company: {company_name}
        - Skills: {skills}
        """,
        "Learning Suggestions 📚": f"""Suggest learning resources for profile improvement.
        - CGPA: {current_cgpa}
        - Dream Company: {company_name}
        - Skills: {skills}
        """,
        "Interview Topics 💬": f"""Provide common interview topics based on the profile.
        - CGPA: {current_cgpa}
        - Dream Company: {company_name}
        - Skills: {skills}
        """,
        "Alternative Career Paths 🌱": f"""Recommend alternative career paths.
        - CGPA: {current_cgpa}
        - Dream Company: {company_name}
        - Skills: {skills}
        """,
        "Company Comparison ⚖️": f"""Compare eligibility and fit for multiple companies.
        - CGPA: {current_cgpa}
        - Dream Company: {company_name}
        - Skills: {skills}
        """,
        "Resume Optimization 📄": f"""Tips to optimize the resume for the dream company.
        - CGPA: {current_cgpa}
        - Dream Company: {company_name}
        - Skills: {skills}
        """,
        "Internship Opportunities 🧑‍💻": f"""Suggest internships to gain relevant experience.
        - CGPA: {current_cgpa}
        - Dream Company: {company_name}
        - Skills: {skills}
        """,
        "Percentile Estimation 📈": f"""Estimate the percentile of the student's current profile in the job market compared to peers.
        ONLY return a number between 0 and 100 — no explanation, no symbols, no sentence. 
        Example: 85
        - CGPA: {current_cgpa}
        - Dream Company: {company_name}
        - Skills: {skills}
        """,
        "Job Market Trends 📊": f"""Analyze job market trends relevant to the student's profile.
        - CGPA: {current_cgpa}
        - Dream Company: {company_name}
        - Skills: {skills}
        """,
        "Networking Tips 🤝": f"""Provide networking tips for the student.
        - CGPA: {current_cgpa}
        - Dream Company: {company_name}
        - Skills: {skills}
        """,
        "Interview Preparation Checklist ✅": f"""Create a checklist for interview preparation.
        - CGPA: {current_cgpa}
        - Dream Company: {company_name}
        - Skills: {skills}
        """,
        "Salary Expectations 💰": f"""Provide salary expectations for the dream company.
        - CGPA: {current_cgpa}
        - Dream Company: {company_name}
        - Skills: {skills}
        """
    }

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(generate_prompt_response, prompts.values()))

    return results, list(prompts.keys())

def plot_pie_chart(percentile):
    x = np.linspace(0, 100, 500)
    mean = 50
    std = 15
    y = (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std) ** 2)
    fig, ax = plt.subplots(figsize=(8, 4))
    fig.patch.set_facecolor('#0E1117')
    ax.set_facecolor('#0E1117')
    ax.plot(x, y, color='lightblue', linewidth=2)
    ax.fill_between(x, 0, y, where=(x <= percentile), color='#0A1A2A', alpha=0.8)
    ax.axvline(x=percentile, color='red', linestyle='--', linewidth=2, label=f'You: {percentile}th %ile')
    ax.set_title("Your Position in the Job Market", fontsize=16, fontweight='bold', color='white')
    ax.set_xlabel("Percentile of people", fontsize=12, color='white')
    ax.yaxis.set_visible(False)
    ax.grid(False)
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.legend(loc='upper right', facecolor='#333333', fontsize=12, frameon=True, framealpha=1, edgecolor='white', labelcolor='white')
    st.pyplot(fig)

st.set_page_config(page_title="Student Career Analyzer", layout="wide")
st.title("📄 Student Career Profile Analysis")

with st.sidebar:
    st.header("🎯 Enter Your Details")
    current_cgpa = st.text_input("Current CGPA:", placeholder="0 - 10")
    company_name = st.text_input("Dream Company:", placeholder="e.g. Google")
    skills = st.text_area("Skills:", placeholder="e.g. Python, React, SQL")
    submit = st.button("🚀 Generate Report")
    st.divider()

if submit:
    st.divider()
    with st.spinner("Generating analysis..."):
        results, headings = AI(current_cgpa, company_name, skills)

    st.success("✅ Analysis completed!")

    try:
        percentile_index = headings.index("Percentile Estimation 📈")
        percentile_value = int(results[percentile_index])
        st.subheader("🎯 Percentile Visualization")
        plot_pie_chart(percentile_value)
    except:
        st.warning("Couldn't generate percentile chart.")

    st.divider()

    tabs = st.tabs(headings)
    for i, (heading, result) in enumerate(zip(headings, results)):
        with tabs[i]:
            st.subheader(f"**{heading}**")
            st.markdown(result)
