import streamlit as st
from importlib import import_module

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
        "Experience":"exp",
    }

    # Page selection
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Go to", options=list(pages.keys()))

    # Import and display the selected page dynamically
    try:
        module = import_module(f"{pages[page]}")
        module.show()  # Call the `show` function from the selected module
    except ModuleNotFoundError:
        st.error(f"Module {pages[page]} not found.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
