import streamlit as st
from PIL import Image

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="Medical DefyBot",
    page_icon="🩺",
    layout="centered"
)

# ---- HEADER ----
st.markdown("<h1 style='text-align: center;'>🩺 Medical DefyBot</h1>", unsafe_allow_html=True)

st.markdown(
    """
    <div style='text-align: center; font-size:18px;'>
        Welcome to <b>Medical DefyBot</b> — your AI-powered assistant for fast, friendly medical guidance.<br>
        Built using <a href='https://dify.ai' target='_blank'>Dify AI</a> and available 24/7.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# ---- IMAGE (OPTIONAL) ----
# Uncomment this if you want to show a medical-themed image
# image = Image.open("medical_bot.png")
# st.image(image, caption="Your AI Medical Companion", use_column_width=True)

# ---- BUTTON ----
st.markdown(
    """
    <div style='text-align: center; margin-top: 30px;'>
        <a href='https://udify.app/chat/7LyKFHlhkNxBGX6j' target='_blank'>
            <button style='
                background-color: #008080;
                color: white;
                padding: 14px 24px;
                font-size: 16px;
                border: none;
                border-radius: 8px;
                cursor: pointer;
            '>
                💬 Launch Chat with Medical DefyBot
            </button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# ---- FOOTER ----
st.markdown("---")
st.markdown(
    "<div style='text-align: center; font-size: 14px;'>"
    "Created by Salma | Powered by Dify AI"
    "</div>",
    unsafe_allow_html=True
)
