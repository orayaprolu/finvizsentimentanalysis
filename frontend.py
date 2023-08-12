import streamlit as st
import pandas as pd
import altair as alt

import mean_sentiment_score as msc
import web_scraping as ws

tickers = ["AAPL", "GOOGL", "META", "AMZN"]

header = st.container()
dataset = st.container()
user_inputs = st.container()

with header:
    st.title("Finziv Sentiment Analyzer")
    st.text("Add description")

with dataset:   
    st.header("Over the past week...")
    df = msc.mean_sentiment_score(ws.parse_data(tickers))

    # print(df)
    # print("------")
    # print(df.index)
    # print("------")
    # print(df.columns)
    #print(df['AAPL'])
    

    chart = alt.Chart(df).mark_line().encode(
        x='date:T',         # X-axis: Date (time-based scale)
        y=tickers[0],
        color='ticker:N'   # Color by ticker (nominal scale)

    ).properties(
        width=600,
        height=300,
        title='Basic Line Chart'
    )

    st.altair_chart(chart)

    st.subheader("Raw data")    
    st.dataframe(df)



with user_inputs:
    st.header("Inputs:")
    