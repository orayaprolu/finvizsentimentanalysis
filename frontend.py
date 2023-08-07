import streamlit as st

header = st.container()
dataset = st.container()
user_inputs = st.container()

with header:
    st.title("Finziv Sentiment Analyzer")
    st.text("Add description")

with dataset:
    st.header("Over the past week...")

with user_inputs:
    st.header()