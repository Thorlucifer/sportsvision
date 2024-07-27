import streamlit as st

def show():
    st.markdown(
    """
    <style>
    .experience-container {
        background-color: black;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }
    .experience-title {
        color: white;
        font-size: 40px;
        margin-bottom: 20px;
    }
    .experience-link {
        color: #1E90FF;
        font-size: 20px;
        text-decoration: none;
    }
    .experience-link:hover {
        text-decoration: underline;
    }
    .experience-image {
        margin-top: 20px;
        width: 80%;
        max-width: 800px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
    )

    # Page Title
    st.markdown('<div class="experience-container">', unsafe_allow_html=True)
    st.markdown('<div class="experience-title"><h2>Experience the Magic</h2></div>', unsafe_allow_html=True)
    
    # Link to the website
    st.markdown(
        '<a href="https://example.com" class="experience-link" target="_blank">Click here to try out our model</a>',
        unsafe_allow_html=True
    )

    # Place for a picture
    st.markdown(
        """
        <div>
            <img src="qr.jpg" class="experience-image" alt="Experience Our Model">
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)
