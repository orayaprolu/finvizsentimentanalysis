import streamlit as st
import pandas as pd
import altair as alt

import mean_sentiment_score as msc
import web_scraping as ws

header = st.container()
dataset = st.container()
user_inputs = st.container()

with header:
    st.title("Finziv Sentiment Analyzer")
    st.text("Add description")

with dataset:   
    st.header("Over the past week...")

    sentiment_data = msc.mean_sentiment_score(ws.parse_data())
    # Melt the DataFrame to long format for Altair visualization
    melted_data = pd.melt(sentiment_data, var_name='ticker', value_name='sentiment')
    print(melted_data)
        
    y_min, y_max = -10, 10

    chart = alt.Chart(melted_data).mark_line(point=True).encode(
        x='date:T',
        y=alt.Y('compound:Q', scale=alt.Scale(domain=(y_min, y_max))),
        color='ticker:N',
        tooltip=['date', 'ticker', 'compound']
        ).interactive()

    st.altair_chart(chart)

    st.subheader("Raw data")
    st.table(sentiment_data)


with user_inputs:
    st.header("Inputs:")
    