import streamlit as st
from groq import Groq

# LLM integration

client=Groq(api_key=st.secrets["Groq_api_key"])


# chat user interface
st.title("AI Chatbot")

# initialising chat history
if "messages" not in st.session_state:
    st.session_state.messages=[]

# clear chat button
if st.button("Clear chat"):
    st.session_state.messages=[]
    st.rerun()

# display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# user input
user_input=st.chat_input("Type your message here...")

if user_input:
    # display user message
    with st.chat_message("user"):
        st.write(user_input)

    # save user message
    st.session_state.messages.append({"role":"user","content":user_input})

    # gen ai responses
    with st.chat_message("assistant"):
        with st.spinner("thinking..."):
            response=client.chat.completions.create(model="openai/gpt-oss-120b",messages=st.session_state.messages)
            answer=response.choices[0].message.content
            st.write(answer)
    # save ai responses
    st.session_state.messages.append({"role":"assistant","content":answer})

