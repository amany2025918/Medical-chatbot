import streamlit as st
import requests

# Streamlit page configuration
st.set_page_config(page_title="Medical Chatbot", page_icon="🩺")

st.title("🩺 Medical Chatbot")
st.write("Ask any medical-related question and get helpful AI-powered answers. Please consult a professional for critical health issues.")

# Input field
user_input = st.text_input("You:")

# Chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# When user enters input
if user_input:
    st.session_state.chat_history.append(("You", user_input))

    # API setup
    api_url = "https://api.dify.ai/v1/chat-messages"
    api_key = " app-xMPlnMcO01NGxpelaC8QbL9W"  # <-- Replace with your actual key

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "inputs": {},  # For apps with input variables, use: {"name": value}
        "query": user_input
    }

    # Call the Dify API
    try:
        response = requests.post(api_url, headers=headers, json=data)
        if response.status_code == 200:
            result = response.json()
            answer = result.get("answer", "Sorry, no response received.")
        else:
            answer = f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        answer = f"Exception occurred: {str(e)}"

    st.session_state.chat_history.append(("Bot", answer))

# Display chat history
for sender, msg in st.session_state.chat_history:
    st.markdown(f"{sender}: {msg}")
