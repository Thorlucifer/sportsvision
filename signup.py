import os
import streamlit as st
def show():
    st.markdown(
    """
    <style>
    .signup-form {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .logo {
        width: 80px;
        margin-bottom: 20px;
    }

    h2 {
        margin-bottom: 20px;
        font-size: 24px;
    }

    .form-group {
        width: 100%;
        margin-bottom: 10px;
    }

    .form-group label {
        display: block;
        margin-bottom: 5px;
        font-size: 16px;
    }

    .form-group input {
        width: 100%;
        padding: 8px;
        box-sizing: border-box;
        font-size: 16px;
    }

    .button-group {
        display: flex;
        justify-content: space-between;
        width: 100%;
        margin-top: 20px;
    }

    .btn {
        width: 48%;
        padding: 10px;
        background-color: #007BFF;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
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
    </style>
    """,
    unsafe_allow_html=True
)

# Display the signup form
st.markdown('<div class="signup-container">', unsafe_allow_html=True)

# Display the form
with st.form(key='signup_form'):
    st.markdown('<h2>Sign Up</h2>', unsafe_allow_html=True)

    email_phone = st.text_input('Email or Phone', '', key='email_phone')
    first_name = st.text_input('First Name', '', key='first_name')
    last_name = st.text_input('Last Name', '', key='last_name')
    password = st.text_input('Set Password', '', type='password', key='password')
    confirm_password = st.text_input('Confirm Password', '', type='password', key='confirm_password')

    st.markdown(
        '<small>Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character.</small>',
        unsafe_allow_html=True
    )

    # Buttons for the form
    submit_button = st.form_submit_button(label='Sign Up')
    cancel_button = st.form_submit_button(label='Cancel')

    if submit_button:
        # Replace with your API call or signup logic
        st.write("Sign Up button clicked!")
    if cancel_button:
        # Handle cancel action
        st.write("Cancelled")

st.markdown('</div>', unsafe_allow_html=True)
