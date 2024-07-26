import streamlit as st

# Set page configuration
st.set_page_config(page_title="SportsVision", page_icon=":guardsman:", layout="wide")

st.title("Welcome to SportsVision")

# Display Video
st.video('output.mp4')

# Display Images
st.image('basketball.png', caption='Basketball Tracking')
st.image('referee.png', caption='Referee')
st.image('hoop.png', caption='Hoop')
st.image('player.png', caption='Player')
st.image('scorecard.png', caption='Scorecard')

# Footer
st.write("© 2024 SportsVision. All rights reserved.")
