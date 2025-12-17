import streamlit as st
import requests

st.title("CodeMentorAI Dashboard")

code = st.text_area("Paste Python Code")

if st.button("Analyze"):
    response = requests.post("http://localhost:8000/analyze", json=code)
    st.json(response.json())
