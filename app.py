import streamlit as st

<<<<<<< HEAD
# Import page functions
from about import show_about
from login import show_login
from signup import show_signup
from upload import show_upload

def main():
    # Set up the title
    st.title("SportsVision")

    # Create a sidebar for page selection
    page = st.sidebar.selectbox("Select a page", ["Home", "About Us", "Sign Up", "Log In", "Upload"])

    if page == "Home":
        # Load and display the home page HTML directly
        html_code = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>SportsVision | Improve Your Performance</title>
            <meta name="description" content="Enhance your athletic performance with cutting-edge video analysis. Upload your sports videos and get detailed insights and metrics to improve your game.">
            <link rel="stylesheet" href="home.css">
        </head>
        <body>
            <!-- HTML content for the home page -->
            <!-- Replace this comment with actual HTML content -->
        </body>
        </html>
        """
        components.html(html_code, height=800, scrolling=True)
    elif page == "About Us":
        show_about()
    elif page == "Sign Up":
        show_signup()
    elif page == "Log In":
        show_login()
    elif page == "Upload":
        show_upload()
=======
# Define the CSS for styling
css = """
<style>
/* Include the relevant CSS here for styling */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: white;
    background: black;
}
.container {
    width: 80%;
    margin: auto;
    overflow: hidden;
}
header {
    background: rgb(2, 8, 37);
    color: #fff;
    padding: 20px 0;
    position: relative;
    z-index: 2;
}
header h1 {
    float: left;
    margin-top: 30px;
    font-size: 50px;
}
header nav {
    float: right;
}
header nav ul {
    list-style: none;
}
header nav ul li {
    display: inline;
    margin-left: 20px;
}
header nav ul li a {
    color: white;
    text-decoration: none;
}
header nav ul li a:hover {
    text-decoration: underline;
}
section#about {
    padding: 100px 0;
    background: black;
    position: relative;
    z-index: 2;
}
section#about h2 {
    color: white;
    margin-bottom: 20px;
    font-size: 40px;
}
section#about p {
    font-size: 18px;
    margin-bottom: 20px;
}
footer {
    background: rgb(2, 8, 37);
    color: #fff;
    text-align: center;
    padding: 20px 0;
    margin-top: 30px;
    position: relative;
    z-index: 2;
}
footer nav ul {
    list-style: none;
}
footer nav ul li {
    display: inline;
    margin: 0 10px;
}
footer nav ul li a {
    color: #fff;
    text-decoration: none;
}
footer nav ul li a:hover {
    text-decoration: underline;
}
</style>
"""

# Add the CSS to the Streamlit app
st.markdown(css, unsafe_allow_html=True)

# Add the header
st.markdown("""
    <header>
        <div class="container">
            <h1>SportsVision</h1>
            <nav>
                <ul>
                    <li><a href="#">Home</a></li>
                    <li><a href="#">About Us</a></li>
                    <li><a href="#">Sign Up</a></li>
                    <li><a href="#">Log In</a></li>
                    <li><a href="#">Upload</a></li>
                </ul>
            </nav>
        </div>
    </header>
""", unsafe_allow_html=True)

# Add the main content for the About Us page
st.markdown("""
    <section id="about">
        <div class="container">
            <h2>About Us</h2>
            <p>Introducing Basketball Video Analysis, a state-of-the-art sports video analysis tool that will transform the way you watch and comprehend basketball games. To provide you with the best in automated basketball analysis, our team of committed professionals—which includes data engineers, machine learning specialists, video processing experts, and UI developers—works nonstop.</p>
            <p>Our goal is to give coaches, athletes, and analysts precise, up-to-date information so they can make wise decisions, perform better, and take greater pleasure in the game. Our technology provides accurate object recognition and tactical analysis through the use of deep learning models and powerful computer vision techniques, guaranteeing that you never miss a crucial moment on the court.</p>
        </div>
    </section>
""", unsafe_allow_html=True)
>>>>>>> 00a0ab099986260e19ce9f374d0fda3e82f063a3

# Add the footer
st.markdown("""
    <footer>
        <div class="container">
            <p>&copy; 2024 SportsVision. All rights reserved.</p>
            <nav>
                <ul>
                    <li><a href="privacy.html">Privacy Policy</a></li>
                    <li><a href="terms.html">Terms of Service</a></li>
                    <li><a href="contact.html">Contact Us</a></li>
                </ul>
            </nav>
        </div>
    </footer>
""", unsafe_allow_html=True)
