import os
import streamlit as st

# Set page configuration
def show():
    st.write("Current working directory:", os.getcwd())

# Custom CSS for styling
st.markdown(
    """
    <style>
    #terms-of-service {
        background-color: black;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }

    #terms-of-service h2 {
        text-align: center;
        color: white;
        font-size: 40px;
    }

    #terms-of-service p,
    #terms-of-service ol {
        line-height: 1.6;
        color: white;
        margin: 0.5em 0;
        font-size: 20px;
    }

    #terms-of-service ol {
        padding-left: 2em;
        list-style-type: decimal;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Terms of Service Section
st.markdown("""
    <section id="terms-of-service">
        <div class="container">
            <h2>Terms of Service</h2>
            <p>Welcome to Basketball Video Analysis. Using our website and services, you agree to comply with and be bound by the following terms and conditions. Please read them carefully.</p>
            <ol>
                <li><strong>Acceptance of Terms:</strong> By accessing or using our website, you agree to be bound by these terms of service and our privacy policy.</li>
                <li><strong>Use of Services:</strong> You agree to use our services only for lawful purposes and in a manner that does not infringe the rights of, restrict, or inhibit anyone else's use and enjoyment of the website.</li>
                <li><strong>Intellectual Property:</strong> All content on our website, including text, graphics, logos, and images, is the property of Basketball Video Analysis and is protected by copyright laws. You may not reproduce, distribute, or create derivative works from any content without our prior written consent.</li>
                <li><strong>Limitation of Liability:</strong> Basketball Video Analysis will not be liable for any damages arising from the use or inability to use our website or services, including but not limited to direct, indirect, incidental, or consequential damages.</li>
                <li><strong>Changes to Terms:</strong> We reserve the right to modify these terms of service at any time. Your continued use of our website after any changes indicates your acceptance of the new terms.</li>
                <li><strong>Governing Law:</strong> These terms of service are governed by and construed by the laws of [Your State/Country], and you at this moment submit to the exclusive jurisdiction of the courts in that location.</li>
            </ol>
            <p>If you have any questions about these terms, don't hesitate to get in touch with us at <a href="mailto:sportsvision80@gmail.com">sportsvision80@gmail.com</a>.</p>
        </div>
    </section>
    """,
    unsafe_allow_html=True
)


