import streamlit as st

st.title("The Memory Vault (Stateful Chatbot)")

personality = st.sidebar.selectbox("Who do you want to talk to",[
        "Thalapathy vijay","Actor suriya","Shah rukh khan","mahesh babu","Rajinikanth"
])

intensity = st.sidebar.slider("Level",min_value=1,max_value=10,value=4)

from google import genai
import os
from dotenv import load_dotenv
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

#Task 1: Initialize the Memory Vault
if "messages" not in st.session_state:
    st.session_state.messages = []

#Task 2: Render the Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Task 3: Upgrade the Input UI
if user_message := st.chat_input("Say something..."):

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    with st.chat_message("user"):
        st.markdown(user_message)

    ai_instructions = (
        f"You are acting as {personality} "
        f"with an intensity level of {intensity}. "
        f"Respond to the message sent by the user "
        f"staying completely in character: {user_message}"
    )

    with st.spinner("Connecting to the multiverse..."):

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=ai_instructions
        )

        ai_response = response.text

    with st.chat_message("assistant"):
        st.markdown(ai_response)

    #Task 4: Save New Messages to Memory
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": ai_response
        }
    )
