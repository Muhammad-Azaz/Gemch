import streamlit as st
import google.generativeai as genai

API_KEY = "AIzaSyA6uTmQOi0xoJkWU8ytEhVDkQWoMvFBrbM"
genai.configure(api_key=API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-1.5-flash')

def getResponseFromModel(user_input):
    response = model.generate_content(user_input)
    return response.text  # Assuming .result contains the text output

# Streamlit UI
st.title("Generative AI Chatbot")

user_input = st.text_input("Enter your Prompt")  # Use st.text_input for user input

if user_input:
    output = getResponseFromModel(user_input)
    st.write("Response:")
    st.write(output)
