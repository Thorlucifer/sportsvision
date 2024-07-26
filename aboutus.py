import streamlit as st
# Set page configuration
def show():
    st.markdown(
    """
    <style>
    .aboutus-container {
        background-color: black;
        padding: 20px;
        border-radius: 10px;
        align-items:center;
    }
    .aboutus-text, .aboutus-title {
        color: white;
        font-size: 16px;
        align-items:center;

    }
    h2 {
        font-size: 40px; /* Increased font size */
        font-weight: bold;
        align-items:center;
    }
     """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <div class="aboutus-container">
    <div class="aboutus-title"><h2>About Us</h2></div>
    <div class="aboutus-text">
    <ul>
    <li>Introducing Basketball Video Analysis, a state-of-the-art sports video analysis tool that will transform the way you watch and comprehend basketball games. To provide you with the best in automated basketball analysis, our team of committed professionals—including data engineers, machine learning specialists, video processing experts, and UI developers—works nonstop.<li>
    <li><strong>Our goal is to give coaches, athletes, and analysts precise, up-to-date information so they can make wise decisions, perform better, and take greater pleasure in the game. Our technology provides accurate object recognition and tactical analysis through the use of deep learning models and powerful computer vision techniques, guaranteeing that you never miss a crucial moment on the court<li>
    </ul>
    </div>
    </div>
    """,
    unsafe_allow_html=True
)

