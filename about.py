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
    }
    .aboutus-text, .aboutus-title {
        color: white;
        font-size: 16px;
    }
    .aboutus-title {
        font-size: 40px; /* Increased font size */
        font-weight: bold;
    }
    header {
        background: #020825;
        color: #fff;
        padding: 10px 0;
        display: flex;
        align-items: center;
        justify-content: space-between; /* Space between logo and title */
        padding: 0 20px;
    }
    
    
    header nav ul {
        list-style: none;
        display: flex;
        justify-content: center;
        margin: 0;
        padding: 0;
        background: #020825; /* Same background color as header */
        padding: 10px 0;
    }
    header nav ul li {
        margin: 0 1em;
    }
    header nav ul li a {
        color: white;
        text-decoration: none;
    }
    header nav ul li a:hover {
        text-decoration: underline;
    }
    h1 {
        font-size: 3.5em; /* Increase this value to change the size */
    }
    footer {
        background: #020825;
        color: #fff;
        text-align: center;
        padding: 20px 0;
        margin-top: auto;
        position: relative;
        z-index: 2;
    }
    footer nav ul {
        list-style: none;
        display: flex;
        justify-content: center;
        margin: 0;
        padding: 0;
    }
    footer nav ul li {
        margin: 0 1em;
    }
    footer nav ul li a {
        color: white;
        text-decoration: none;
    }
    footer nav ul li a:hover {
        text-decoration: underline;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Head
# Header with logo and title
st.markdown(
    """
    <header>
            <h1>SportsVision</h1>
    </header>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <div class="aboutus-container">
    <div class="aboutus-title">About Us</div>
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
# Footer
st.markdown(
    """
    <footer>
        <div class="container">
            <p>&copy; 2024 SportsVision. All rights reserved.</p>
            <nav>
                <ul>
                    <li><a href="#">Privacy Policy</a></li>
                    <li><a href="#">Terms of Service</a></li>
                    <li><a href="#">Contact Us</a></li>
                </ul>
            </nav>
        </div>
    </footer>
    """,
    unsafe_allow_html=True
)


