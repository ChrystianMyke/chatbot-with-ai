# streamlit - frontend and backend
# The AI we will use is OpenAI
# pip install streamlit openai

import streamlit as st
from openai import OpenAI
from chave import chave_api

modelo_ai = OpenAI(api_key=chave_api)

st.write("# Chatbot with AI") # Title of the app

if not 'list_messages' in st.session_state:
    st.session_state["list_messages"] = [] # Initialize message list in session state

text_user = st.chat_input("Enter your message") # input  chat from user

for message in st.session_state["list_messages"]:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).write(content) # display previous messages

if text_user:
    st.chat_message("user").write(text_user) # show user message
    user_message = {"role": "user", "content": text_user}
    st.session_state["list_messages"].append(user_message) # add user message to list

    answer_ai = modelo_ai.chat.completions.create( # call to OpenAI API
        model="gpt-4o",
        messages=st.session_state["list_messages"]
    )
    text_answer_ai = answer_ai.choices[0].message.content # get AI response

    st.chat_message("assistant").write(text_answer_ai) # show IA response
    message_ai = {"role": "assistant", "content": text_answer_ai}
    st.session_state["list_messages"].append(message_ai) # add AI response to list


