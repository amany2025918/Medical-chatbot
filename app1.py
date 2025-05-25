import streamlit as st
import requests
import uuid

st.set_page_config(page_title="Medical Chatbot", page_icon="🩺")
st.title("🩺 Medical Chatbot")
st.write("Ask any medical-related question and get helpful AI-powered answers. Please consult a professional for critical health issues.")

if "user_id" not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "input_text" not in st.session_state:
    st.session_state.input_text = ""

user_input = st.text_input("You:", key="input_text")

if user_input:
    st.session_state.chat_history.append(("You", user_input))

    api_url = "https://api.dify.ai/v1/chat-messages"
    api_key = "app-xMPlnMcO01NGxpelaC8QbL9W"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "inputs": {},
        "query": user_input,
        "user": st.session_state.user_id
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

    # مسح مربع الإدخال بعد إرسال الرسالة
    st.session_state.input_text = ""

for sender, msg in st.session_state.chat_history:
    st.markdown(f"**{sender}**: {msg}")
