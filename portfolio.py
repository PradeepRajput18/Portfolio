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
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
        }
        .stButton button:hover {
            background-color: #ccd6f6;
            color: #0a192f;
        }
        .section {
            margin-bottom: 30px;
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
st.subheader("Software Engineer & Wellness Instructor for better world")
st.markdown(
    """
    Everyday is a opportunity to learn & evolve, this is the passion which drives to explore all & new possibilities.

    I will be graduating May 2025 & looking for Software Intern for Spring 2025 , Fulltime opportunities from May onwards.

    not limiting my self to particular role but able work in any technology.
    """
)

# About Me Section
st.header("About Me")
st.markdown(
    """
    - **Location**: Atlanta, GA (Open to Relocate)
    - **Education**:
      - **Kennesaw State University**: M.S. in Computer Science (Expected May 2025)
      - **Jawaharlal Nehru Technological University**: B.Tech in Computer Science (Graduated May 2022)
    - **Skills**:
      - **Programming**: C++, Python
      - **Web Technologies**: React, JavaScript, HTML, CSS, Figma
      - **Systems & Databases**: Linux, SQL, NoSQL (MongoDB)
      - **Methodologies**: Agile, CI/CD
    """
)

# Work Experience Section
st.header("Work Experience")
with st.container():
    st.subheader("Research Assistant - Kennesaw State University (Aug 2023 - May 2024)")
    st.markdown(
        """
        - Led a team to design a text annotator for PDF documents, completing the project in five months.
        - Achieved 82.74% accuracy in crime prediction for two counties using Logistic Regression.
        - **Tech Stack**: HTML, CSS, JavaScript, Python, Pandas, scikit-learn.
        """
    )
    
    st.subheader("Software Development Engineer - Infosys (Jun 2022 - Jul 2023)")
    st.markdown(
        """
        - Optimized workforce management tools, improving search efficiency by 30%.
        - Developed reusable UI components and automation features in React.
        - **Tech Stack**: React, C++, Git.
        """
    )

    st.subheader("Frontend Software Engineer - SriTech (Nov 2021 - May 2022)")
    st.markdown(
        """
        - Implemented dynamic user interfaces for 800,000 active users.
        - Enhanced accessibility by supporting 25 languages with a machine translation feature.
        - **Tech Stack**: React, Bootstrap, Adobe XD, AWS.
        """
    )

# Projects Section
st.header("Projects")
st.markdown(
    """
    - **Chrome Extension - LeetCode Companion** (Dec 2024): Reduced tab-switching distractions with a coding helper extension. **Tech Stack**: JavaScript, Gemini 2.0 API.
    - **Sudoku Solver** (Dec 2024): Developed a backtracking algorithm to solve Sudoku puzzles. **Tech Stack**: C++.
    - **Carpool Platform** (Dec 2024): Created a scalable ride-sharing platform with estimated costs and time. **Tech Stack**: C++.
    - **Word Auto Complete** (Sep 2024): Implemented efficient auto-completion using the Trie data structure. **Tech Stack**: C++.
    """
)

# Leadership & Involvement Section
st.header("Leadership & Involvement")
st.markdown(
    """
    - **President**, Sky Campus Happiness (Sep 2023 - Present): Facilitated programs for 150+ participants, fostering resilience and emotional intelligence.
    - **Content Creator**, YouTube: Day1Pradeep (Aug 2024 - Present): Created tech and student life content.
    - **Coding Mentor**, Edyst (Apr 2022 - Mar 2023): Mentored 35+ students in C++ programming.
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
if st.button("Download Resume"):
    with open("Pradeep_Rekapalli_Resume.pdf", "rb") as file:
        st.download_button(
            label="Click here to download",
            data=file,
            file_name="Pradeep_Rekapalli_Resume.pdf",
            mime="application/pdf"
        )
