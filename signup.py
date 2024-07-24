import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Signup | SportsVision", page_icon=":pencil:")

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        font-family: Arial, sans-serif;
        color: white;
        background-color: rgb(2, 8, 37);
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
        padding: 20px;
    }

    .signup-container {
        background: black;
        padding: 20px;
        border-radius: 5px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        width: 350px;
        margin: 0 10px;
    }

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

# Display the logo
st.image("D:/sports video analysis/homepage/logo.jpg", width=80, use_column_width=False)

# Display the form
with st.form(key='signup_form'):
    st.markdown('<h2>Sign Up</h2>', unsafe_allow_html=True)

    email_phone = st.text_input('Email or Phone', '')
    first_name = st.text_input('First Name', '')
    last_name = st.text_input('Last Name', '')
    password = st.text_input('Set Password', '', type='password')
    confirm_password = st.text_input('Confirm Password', '', type='password')

    st.markdown(
        '<small>Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character.</small>',
        unsafe_allow_html=True
    )

    submit_button = st.form_submit_button(label='Sign Up')
    cancel_button = st.button('Cancel', key='cancel')

    if submit_button:
        # Replace with your API call or signup logic
        st.write("Sign Up button clicked!")
    if cancel_button:
        # Handle cancel action
        st.write("Cancelled")

st.markdown('</div>', unsafe_allow_html=True)
