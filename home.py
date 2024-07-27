import streamlit as st
import time

# Set the page configuration
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

# Home Page
def home():
    st.markdown("""
        <style>
        .main {
            background-color: black;
            color: white;
            padding: 20px;
        }
        .video-container {
            display: flex;
            justify-content: center;
            margin-bottom: 20px;
        }
        .video-container video {
            width: 50%;
            max-width: 10px;
        }
        .key-benefits {
            margin-bottom: 40px;
        }
        .key-benefits h3 {
            font-size: 200px;
            margin-bottom: 10px;
        }
        .key-benefits ul {
            list-style: none;
            padding: 0;
            margin:0;
            font-size:100px;
        }
        .key-benefits ul li {
            background: url('check.png') no-repeat left center;
            background-size: 20px;
            padding-left: 30px;
            margin-bottom: 10px;
            font-size:90px;
        }
        .action-heading {
            font-size: 36px;
            margin-bottom: 20px;
            text-align: center;
        }
        .highlights-images {
            margin: 20px 0;
        }
        .highlights-images img {
            width: 100%;
            height: auto; /* Maintain aspect ratio */
            object-fit: cover;
        }
         .content {
            padding: 20px;
            margin-bottom: 5px;  /* Space for the footer */
        }
        .large-text {
            font-size: 36px;  /* Adjust font size as needed */
            font-weight:bold;
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

    # Increased font size for the action heading
    st.markdown('<div class="action-heading">See how we bring the action to life below!</div>', unsafe_allow_html=True)

    # Images in a grid layout with uniform size
    cols = st.columns(3)  # Create 3 equal columns
    image_paths = ['referee.png', 'hoop.png', 'player.png', 'basketball.png', 'scorecard.png']
    
    for i in range(3):
        with cols[i]:
            st.image(image_paths[i], caption='Image', use_column_width=True)

    # Create another row with 2 columns
    cols = st.columns(2)  # Create 2 equal columns
    for i in range(3, 5):
        with cols[i-3]:
            st.image(image_paths[i], caption='Image', use_column_width=True)

# Footer
# Display the content
home()
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
