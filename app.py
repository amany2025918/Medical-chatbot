import streamlit as st

def main():
    st.title("My Chatbot App")

    st.write("Welcome to the chatbot powered by Dify!")

    # Chat history stored in session state
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    # User input
    user_input = st.text_input("You:", "")

    if st.button("Send") and user_input:
        # Here you call your chatbot API or logic
        response = get_bot_response(user_input)

        # Save conversation
        st.session_state.chat_history.append(("User", user_input))
        st.session_state.chat_history.append(("Bot", response))

    # Display chat history
    for sender, msg in st.session_state.chat_history:
        if sender == "User":
            st.markdown(f"**You:** {msg}")
        else:
            st.markdown(f"**Bot:** {msg}")

def get_bot_response(user_input):
    # Placeholder for your chatbot logic or API call to Dify backend
    # For example, you could make a POST request to your Dify API
    return "This is a dummy response."

if __name__ == "__main__":
    main()
