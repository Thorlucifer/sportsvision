from aboutus import show

def main():
    # Define page options
    pages = {
        "Home": "home",
        "Sign Up": "signup",
        "Log In": "login",
        "Upload": "upload",
        "About Us": "aboutus",
        "Contact Us": "contact",
        "Privacy Policy": "privacy",
        "Terms of Service": "terms",
    }

    # Page selection
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Go to", options=list(pages.keys()))

    # Import and display the selected page
    try:
        module = import_module(pages[page])
        module.show()  # Ensure this line calls the `show` function
    except ModuleNotFoundError:
        st.error(f"Module {pages[page]} not found.")
