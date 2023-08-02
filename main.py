# Request module (fetches html content of webpage)
from urllib.request import urlopen, Request

# Parsing module (converts html file into Pyton object to interact with html elements)
from bs4 import BeautifulSoup

import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Add more websites and tickers later
finviz_base_url = "https://finviz.com/quote.ashx?t="
tickers = ["AMD", "AAPL", "GOOGL", "META"]

# Map of ticker and news-table pair
news_tables = {}

parsed_data = []

# Goes through each ticker and parses into pared_data
for t in tickers:
    url = finviz_base_url + t
    
    # Fetches request and recieves webpage
    req = Request(url= url, headers= {"user-agent": "'my-app"})
    response = urlopen(req)

    # Specifies webpage is html and only returns entire 'news-table' block
    html = BeautifulSoup(response, "html")
    news_tab = html.find(id='news-table')
    news_tables[t] = news_tab

    # Goes through every table row in the table
    for row in news_tab.findAll('tr'):

        # Anchor(a) element
        title_element = row.a

        # Table Data(td) element
        date_element = row.td

        # Makes sure there is a valid title and date
        if title_element is not None and date_element is not None:
            title = title_element.text

            # Removes white spaces from date
            date_text = date_element.text.strip()

            # Splits date and time
            date_data = date_text.split(' ')
            if len(date_data) == 1:
                time = date_data[0]
            else:
                date = date_data[0]
                time = date_data[1]
            parsed_data.append([t, date, time, title])
    
    break

# df = pd.DataFrame(parsed_data, columns=['ticker', 'date', 'time', 'title'])

# vader = SentimentIntensityAnalyzer()

# f = lambda title: vader.polarity_scores(title)['compound']
# df['compound score'] = df['title'].apply(f)