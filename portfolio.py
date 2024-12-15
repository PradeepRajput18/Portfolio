import streamlit as st
from PIL import Image

# Load resources
resume_photo = "profile.jpg"  # Replace with actual path
linkedin_url = "https://www.linkedin.com/in/pradeep-rekapalli/"
github_url = "https://github.com/PradeepRajput18"
email = "prekapal@students.kennesaw.edu"

# Custom CSS for styling
st.markdown(
    """
    <style>
        body {
            background-color: #0a192f;
            color: #ccd6f6;
            font-family: 'Helvetica', sans-serif;
        }
        .sidebar .sidebar-content {
            background-color: #112240;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #64ffda;
        }
        a {
            color: #64ffda;
            text-decoration: none;
        }
        a:hover {
            color: #ccd6f6;
        }
        .stButton button {
            background-color: #64ffda;
            color: #0a192f;
        }
        .stButton button:hover {
            background-color: #ccd6f6;
            color: #0a192f;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar
st.sidebar.image(resume_photo, width=150)
st.sidebar.title("Pradeep Rekapalli")
st.sidebar.markdown(f"[LinkedIn]({linkedin_url}) | [GitHub]({github_url})")
st.sidebar.markdown(f"📧 {email}")

# Main Content
st.title("Pradeep Rekapalli")
st.subheader("Passionate Software Engineer")
st.markdown(
    """
    I build accessible, pixel-perfect digital experiences for the web. With a focus on design, development, and usability, I strive to create solutions that are both visually stunning and highly functional.
    """
)

# About Me Section
st.header("About Me")
st.markdown(
    """
    - **Location**: Atlanta, GA (Open to Relocate)
    - **Education**:
      - **Kennesaw State University**: M.S. in Computer Science (Expected May 2025)
      - **JNTU**: B.Tech in Computer Science (Graduated May 2022)
    - **Skills**:
      - Programming: C++, Python
      - Tools: React, MongoDB, SQL, NoSQL
      - Methodologies: Agile, CI/CD
    """
)

# Work Experience Section
st.header("Experience")
with st.container():
    st.subheader("Research Assistant - Kennesaw State University")
    st.markdown(
        """
        - Designed a text annotator for PDF documents in five months.
        - Collaborated with PhD researchers, achieving 82.74% crime prediction accuracy.
        - **Tech Stack**: HTML, CSS, JavaScript, Python, Pandas, scikit-learn.
        """
    )
    
    st.subheader("Software Development Engineer - Infosys")
    st.markdown(
        """
        - Enhanced internal workforce management tools, improving search efficiency.
        - Developed automation features using React and C++.
        """
    )

# Projects Section
st.header("Projects")
st.markdown(
    """
    - **Bank Management System** (C++): Account and balance management.
    - **Word Auto Complete** (C++): Trie data structure implementation.
    - **Mini Search Engine** (C++): Regex-based pattern matching.
    - **Food Delivery App** (Figma): User-friendly, responsive design.
    """
)

# Leadership & Involvement Section
st.header("Leadership & Involvement")
st.markdown(
    """
    - **President**, Sky Campus Happiness: Organized wellness programs for 150+ participants.
    - **Coding Mentor**, Edyst: Guided 35+ students in C++ programming.
    """
)

# Contact Section
st.header("Contact")
st.markdown(
    """
    Feel free to reach out:
    - 📧 Email: [prekapal@students.kennesaw.edu](mailto:prekapal@students.kennesaw.edu)
    - 🌐 [LinkedIn](https://www.linkedin.com/in/pradeep-rekapalli/)
    - 💻 [GitHub](https://github.com/PradeepRajput18)
    """
)

# Add a call-to-action button
st.button("Download Resume")
