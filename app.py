import streamlit as st
import streamlit.components.v1 as components

st.title("My Chatbot via Dify")

# https://udify.app/chat/7LyKFHlhkNxBGX6j
chatbot_url = "https://udify.app/chat/7LyKFHlhkNxBGX6j"

components.iframe(chatbot_url, height=600, scrolling=True)
