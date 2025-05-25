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

    # امسح مربع النص بعد الإرسال
    st.session_state.input_text = ""
