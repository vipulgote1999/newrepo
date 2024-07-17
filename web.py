import streamlit as st
from PIL import Image
from pathlib import Path

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "style" / "main.css"
resume_file = current_dir / "assets\Amit_resume_businessAnalyst.pdf"
profile_pic = current_dir / "assets" / "ID size photo.jpg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | AMIT KHADE"
PAGE_ICON = ":wave:"
NAME = "**AMIT KHADE**"
DESCRIPTION = """
**Data Science and Machine Learning Enthusiast**
"""
EMAIL = "**amitkhade2507@gmail.com**"

SOCIAL_MEDIA = {
    
    "**LinkedIn**": "https://www.linkedin.com/in/contactamitkhade/",
    "**GitHub**": "https://github.com/amit2507a"
    
}

PROJECTS = {
    "🏆 Netflix Data Analysis - Analysis on TV shows and Movies on Netflix till 2021": "https://colab.research.google.com/drive/1p_tfT-MMwMItxJzs4nfVchvz9RAaR1tg?usp=sharing",
    "🏆 Tableau Dashboard on Netflix analysis - Dashboard for overall analysis of data": "https://public.tableau.com/app/profile/amit.khade1427/viz/netflix_16980896365530/NETFLIXDASHBOARD",
    "🏆 Placement analysis using Machine Learning - Project will perfom the overall analysis of placement of students in the uploaded dataset ": "https://colab.research.google.com/drive/1kqgR-5X55apwrZ2dgljWBphM8dGhGf-N?usp=sharing"
    
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=200)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
    



# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python, Data structures, Object oriented programming, SQL
- 📊 Data Visulization: Tableau, Matplotlib, MS Excel
- 📚 Artificial Intelligence: Machine Learning Algorithms, Deep learning, Natural language processing 
- 🗄️ Databases: MySQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write('\n')

# --- Intern 1
st.write("🚧", "**Machine Learning Intern | BharatTech**")
st.write("06/2023 - 09/2023")
st.write(
    """
- ► Got deep insights about Hugging face which is an Artificial Intelligence community 
- ► Working on machine Learning models 
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write('\n')
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

