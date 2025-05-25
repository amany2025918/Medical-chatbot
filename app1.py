import streamlit as st
import requests

st.set_page_config(page_title="Medical Chatbot", page_icon="🩺")
st.title("🩺 Medical Chatbot")
st.write("Ask any medical-related question and get helpful AI-powered answers. Please consult a professional for critical health issues.")

user_input = st.text_input("You:")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if user_input:
    st.session_state.chat_history.append(("You", user_input))

    api_url = "https://api.dify.ai/v1/chat-messages"
    api_key = "app-xMPlnMcO01NGxpelaC8QbL9W"  # replace with your real key

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "inputs": {},
        "query": user_input
    }

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

for sender, msg in st.session_state.chat_history:
    st.markdown(f"**{sender}**: {msg}")
