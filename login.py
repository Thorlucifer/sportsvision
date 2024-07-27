import os
import streamlit as st

# Set the page configuration as the first Streamlit command
def show():
    st.markdown(
    """
    <style>
    .logo {
        width: 100px;
        display: block;
        margin: 0 auto 20px;
    }

    h2 {
        margin-bottom: 20px;
        font-size: 32px;
        text-align: center;
    }

    .form-group {
        margin-bottom: 20px;
        background: black;
    }

    .form-group label {
        display: block;
        margin-bottom: 10px;
        font-size: 18px;
    }

    .form-group input {
        width: 100%;
        padding: 12px;
        box-sizing: border-box;
        font-size: 18px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

    .button-group {
        display: flex;
        justify-content: space-between;
        margin-top: 30px;
    }

    .btn {
        width: 48%;
        padding: 15px;
        background-color: #007BFF;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 18px;
        text-align: center;
    }

    .btn:hover {
        background-color: #0056b3;
    }

    .btn.cancel {
        background-color: #6c757d;
    }

    .btn.cancel:hover {
        background-color: #5a6268;
    }

    .forgot-password,
    .signup-link {
        text-align: center;
        margin-top: 20px;
    }

    .forgot-password a,
    .signup-link a {
        color: white;
        text-decoration: none;
    }

    .forgot-password a:hover,
    .signup-link a:hover {
        text-decoration: underline;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the login form
st.markdown('<div class="login-container">', unsafe_allow_html=True)

# Display the logo


# Display the form
with st.form(key='login_form'):
    st.markdown('<h2>Login</h2>', unsafe_allow_html=True)
    
    email_phone = st.text_input('Email or Phone', '')
    password = st.text_input('Password', '', type='password')
    
    submit_button = st.form_submit_button(label='Login')

    if submit_button:
        # Replace with your API call or login logic
        st.write("Login button clicked!")

st.markdown('</div>', unsafe_allow_html=True)

# Display the forgot password and signup links
st.markdown('<div class="forgot-password"><a href="forgot-password.html">Forgot Password?</a></div>', unsafe_allow_html=True)
st.markdown('<div class="signup-link"><p>Don\'t have an account? <a href="signup.html">Sign Up</a></p></div>', unsafe_allow_html=True)
