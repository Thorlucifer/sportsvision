import os
import streamlit as st

# Print the current working directory
st.write("Current working directory:", os.getcwd())

# Check if the file exists
file_path = "logo.jpg"
if os.path.exists(file_path):
    st.write(f"The file {file_path} exists.")
else:
    st.write(f"The file {file_path} does not exist.")

# Display the logo
st.image(file_path, width=100, use_column_width=False)
