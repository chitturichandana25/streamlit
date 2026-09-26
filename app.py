import streamlit as st
st.title("AI Chatbot")
st.write("AI Chatbot")

st.sidebar.button("drop")
prompt=text=st.text_input("Ask me ")

if st.button("send"):
        messages=[
            {
            "role":"user",
            "content":prompt
            }
        ]