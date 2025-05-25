import streamlit as st
import streamlit.components.v1 as components

st.title("My Dify Chatbot")

# Your Dify chatbot public URL
chatbot_url = "https://udify.app/chat/7LyKFHlhkNxBGX6j"

# Embed the chatbot page as an iframe
components.iframe(chatbot_url, height=700, scrolling=True)
