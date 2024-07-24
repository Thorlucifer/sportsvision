import streamlit as st
import time

# Set the page configuration
st.set_page_config(page_title="Upload Video | SportsVision", page_icon=":film_strip:")

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        font-family: Arial, sans-serif;
        background-color: rgb(10, 16, 50);
        color: white;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
        padding: 0;
    }

    .upload-container {
        background: black;
        padding: 40px;
        border-radius: 10px;
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);
        width: 80%;
        max-width: 600px;
        text-align: center;
    }

    .upload-form h2 {
        margin-bottom: 20px;
        font-size: 32px;
    }

    .drop-zone {
        border: 2px dashed #007BFF;
        padding: 30px;
        border-radius: 10px;
        cursor: pointer;
        transition: background-color 0.3s;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 300px;
    }

    .drop-zone:hover {
        background-color: #1A1A1A;
    }

    .drop-zone p {
        margin: 0;
        font-size: 18px;
    }

    .btn {
        padding: 15px 30px;
        background-color: #007BFF;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 18px;
        margin-top: 20px;
    }

    .btn:hover {
        background-color: #0056b3;
    }

    .progress-container {
        margin-top: 20px;
        text-align: left;
    }

    .progress-bar {
        width: 0;
        height: 20px;
        background-color: #007BFF;
        border-radius: 5px;
        transition: width 0.3s;
    }

    .btn-cancel {
        background-color: #17a245;
        margin-left: 10px;
    }

    .btn-cancel:hover {
        background-color: #c82333;
    }

    .logo {
        height: 100px;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the upload form
st.markdown('<div class="upload-container">', unsafe_allow_html=True)

# Display the logo
st.image("D:/sports video analysis/homepage/logo.jpg", width=100, use_column_width=False)

st.markdown('<h2>Upload Your Video for Analysis</h2>', unsafe_allow_html=True)

# File uploader widget
uploaded_file = st.file_uploader("Drag & Drop your video here", type=["mp4", "mov", "avi"])

if uploaded_file is not None:
    st.video(uploaded_file, format="video/mp4")  # Display video preview

    # Simulate file upload process
    with st.spinner("Uploading..."):
        time.sleep(2)  # Simulate a delay for file upload
        st.success("Upload complete!")

    st.markdown(
        """
        <div class="button-group">
            <button class="btn" onclick="window.location.href='home.html'">Cancel</button>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown('</div>', unsafe_allow_html=True)
