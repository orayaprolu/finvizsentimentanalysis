import streamlit as st
import pandas as pd

import data_collection as dc

header = st.container()
dataset = st.container()
user_inputs = st.container()

with header:
    st.title("Finziv Sentiment Analyzer")
    st.text("Add description")

with dataset:   
    st.header("Over the past week...")

    if 'y_min' not in st.session_state:
        st.session_state.y_min = -1.0

    if 'y_max' not in st.session_state:
        st.session_state.y_max = 1.0

    sentiment_data = dc.get_dataset()
        
    # sentiment_data["compound"] = sentiment_data['compound'].clip(-1, 1)
    st.line_chart(sentiment_data)

    st.subheader("Raw data")
    st.table(sentiment_data)


with user_inputs:
    st.header("Inputs:")
    