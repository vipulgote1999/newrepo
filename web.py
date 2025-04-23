import streamlit as st
from PIL import Image
from pathlib import Path

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "style" / "main.css"
resume_file = current_dir / "assets" / "AMIT_KHADE.pdf" 
profile_pic = current_dir / "assets" / "ID size photo.jpg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "MY PORTFOLIO | AMIT KHADE"
PAGE_ICON = ":wave:"
NAME = "**AMIT KHADE**"
DESCRIPTION = """
**Data Science and Machine Learning Enthusiast**
"""
EMAIL = "**amitkhade2507@gmail.com**"

SOCIAL_MEDIA = {
    
    "**LinkedIn**": "https://www.linkedin.com/in/contactamitkhade/"
    
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
- 👩‍💻 Programming: Python, Object oriented programming, SQL
- 📊 Data Analysis:  NumPy, Pandas, Exploratory Data Analysis, Matplotlib, Seaborn, Plotly,
 Tableau, MYSQL, MongoDB, Statistics
- 📚 Artificial Intelligence:  TensorFlow, Keras, CNN, RNN, LSTM, OCR 
- 📚 Computer vision:  YOLO, OpenCV, Object Detection, Object Segmentation
- 📚 NLP: NLTK,spacy, Hugging Face Transformers
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Experience")
st.write('\n')

# - - - Intern 2
st.write("🚧", "**AIML Engineer | ProvaanTech**")

st.write(
    """
- ► Speech-to-Speech Voice Assistant
 Tech stack: Python, Faster-Whisper, LLaMA, Coqui TTS, Voice Cloning (XTTS-v2)
 • Developed a real-time Speech-to-Speech AI assistant integrating STT, LLM, and TTS modules for natural,
 interactive voice conversations.Enhanced project capabilities with modular architecture to support custom
 voice avatars, multilingual support, and dynamic prompt handling.
- ► AIpowered estimation system for construction blueprints
 Tech Stack: Python, YOLOv8, OpenCV, PaddleOCR
 • Developed a smart floor plan analysis tool tailored for architects and builders to automate room, door, and
 annotation detection from construction blueprints.Used YOLOv8 for high-precision door and room object
 detection and PaddleOCR for reading blueprint labels, achieving 90% detection accuracy and 95% OCR
 precision.

"""
)

# --- Intern 1
st.write("🚧", "**Machine Learning Intern | BharatTech**")

st.write(
    """
- ► Acquired in-depth knowledge of Hugging Face, an AI community, and explored 
various Large Language Models(LLMs) including LLAMA and GPT. 
- ► Conducted extensive research to identify and curate suitable
datasets for machine learning models.

"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Personal Projects & Accomplishments")
st.write('\n')
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")






