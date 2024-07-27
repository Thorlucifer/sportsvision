import streamlit as st

def show():
    st.markdown("""
    <style>
    .header {
        background-color: rgb(2, 8, 37);
        color: white;
        padding: 20px 0;
        position: relative;
        z-index: 2;
        text-align: center;
    }
    .header h1 {
        font-size: 50px;
        margin-top: 30px;
    }
    .header nav ul {
        list-style: none;
        padding: 0;
        margin: 0;
    }
    .header nav ul li {
        display: inline;
        margin-left: 20px;
    }
    .header nav ul li a {
        color: white;
        text-decoration: none;
    }
    .header nav ul li a:hover {
        text-decoration: underline;
    }
    </style>
    """, unsafe_allow_html=True)

    # Content
    st.markdown('<div class="content"><p class="large-text">Welcome to SportsVision</p></div>', unsafe_allow_html=True)
    st.write("Enhance your athletic performance with our cutting-edge video analysis tools. Upload your sports videos and get detailed insights and metrics to take your game to the next level.")

    # Centered Video
    st.markdown('<div class="video-container">', unsafe_allow_html=True)
    st.video('output.mp4')
    st.markdown('</div>', unsafe_allow_html=True)

    # Key Benefits
    st.write("## Key Benefits")
    st.write("""
    - Advanced Performance Metrics
    - Personalized Improvement Plans
    - Expert Analysis by Professional Coaches
    - Easy-to-Use Upload and Review System
    - Secure and Private
    """)

    # Action Heading
    st.markdown('<div class="action-heading">See how we bring the action to life below!</div>', unsafe_allow_html=True)

    # Images in a grid layout
    cols = st.columns(3)
    image_paths = ['referee.png', 'hoop.png', 'player.png', 'basketball.png', 'scorecard.png']

    for i in range(3):
        with cols[i]:
            st.image(image_paths[i], caption='Image', use_column_width=True)

    cols = st.columns(2)
    for i in range(3, 5):
        with cols[i-3]:
            st.image(image_paths[i], caption='Image', use_column_width=True)
