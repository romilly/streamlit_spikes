# Generated by ChatGPT, heavily modified by me

from dotenv import load_dotenv
import streamlit as st
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
import os
from pew.chat.sqlite_recorder import SQLiteChatRecorder

# Function to send requests to Mistralx API

# Streamlit app

load_dotenv()
api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-small"
client = MistralClient(api_key=api_key)
recorder = SQLiteChatRecorder('/home/romilly/git/active/streamlit_spikes/data/chats.db')
st.title("Conversation with Mistralx Model")

if prompt := st.chat_input():
    st.chat_message("user").write(prompt)
    messages = [
        ChatMessage(role="user", content=prompt)
    ]
    response = client.chat(
    model=model,
    messages=messages,
    ).choices[0].message.content
    st.chat_message("assistant").write(response)

    recorder.add_record('localhost', {'user_input': prompt, 'response': response})
