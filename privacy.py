import streamlit as st

# Set page configuration
def show():
    st.markdown(
    """
    <style>
    .privacy-policy-container {
        background-color: black;
        padding: 20px;
        border-radius: 10px;
    }
    .privacy-policy-text, .privacy-policy-title {
        color: white;
        font-size: 16px;
        align-items:center;
    }
    .privacy-policy-title {
        font-size: 40px; /* Increased font size */
        font-weight: bold;
        align-items:center;
    }
   
    
    h2 {
        text-align: center;
        color: white;
        font-size: 40px;
    }
    
    
    </style>
    """,
    unsafe_allow_html=True
)



# Content of the privacy policy
st.markdown(
    """
    <div class="privacy-policy-container">
    <div class="privacy-policy-title"><h2>Privacy Policy</h2></div>
    <div class="privacy-policy-text">
    <p><strong>Your privacy is important to us.</strong> This privacy policy outlines how Basketball Video Analysis collects, uses, and protects your information when you use our website and services.</p>

    <h3>Information We Collect:</h3>
    <ul>
        <li><strong>Personal Information:</strong> We may collect personal information such as your name, email address, and contact details when you register on our site or fill out a form.</li>
        <li><strong>Usage Data:</strong> We collect data on how you interact with our website, including your IP address, browser type, and browsing behavior.</li>
    </ul>

    <h3>How We Use Your Information:</h3>
    <ul>
        <li>To provide and improve our services</li>
        <li>To personalize your experience</li>
        <li>To communicate with you and respond to inquiries</li>
        <li>To analyze website usage and enhance performance</li>
    </ul>

    <h3>Data Protection:</h3>
    <p>We implement a variety of security measures to maintain the safety of your personal information. However, no method of transmission over the Internet is completely secure, and we cannot guarantee absolute security.</p>

    <h3>Third-Party Disclosure:</h3>
    <p>We do not sell, trade, or otherwise transfer your personal information to outside parties, except as necessary to provide our services or comply with the law.</p>

    <h3>Changes to Our Privacy Policy:</h3>
    <p>We may update this privacy policy from time to time. We will notify you of any changes by posting the new policy on our website.</p>

    <p>If you have any questions about our privacy policy, please get in touch with us at <a href="mailto:sportsvision80@gmail.com" style="color: #1E90FF;">sportsvision80@gmail.com</a></p>
    </div>
    </div>
    """,
    unsafe_allow_html=True
)

#