# Import Streamlit library
import streamlit as st

# Title of the app
st.title("Interactive Streamlit App")

# Text input for user name
name = st.text_input("What is your name?")

# Show greeting if the user has entered their name
if name:
    st.write(f"Hello, {name}! Nice to meet you!")
else:
    st.write("Please enter your name.")

# Slider to select a number
age = st.slider("How old are you?", 1, 100, 25)
st.write(f"You are {age} years old.")

# Checkbox to ask if the user likes coding
likes_coding = st.checkbox("Do you like coding?")
if likes_coding:
    st.write(f"That's awesome, {name}! Keep up the great work!")
else:
    st.write(f"That's okay, {name}! There's no pressure.")

# Button that displays a message when clicked
if st.button("Click me for a surprise"):
    st.write("🎉 Surprise! You clicked the button!")

# File uploader to upload a file (for example, an image)
uploaded_file = st.file_uploader("Upload a file", type=["png", "jpg", "jpeg", "gif"])

# If the user uploads an image, display it
if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    st.write("Thank you for uploading the file!")