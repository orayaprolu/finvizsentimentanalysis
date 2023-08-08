# Request module (fetches html content of webpage)
from urllib.request import urlopen, Request

# Parsing module (converts html file into Pyton object to interact with html elements)
from bs4 import BeautifulSoup

# Pandas module allows for flexible usage of data
import pandas as pd

# Corpus and sentiment analysis algorithm
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def get_dataset():

    # Add more tickers later
    finviz_base_url = "https://finviz.com/quote.ashx?t="
    tickers = ["AAPL", "GOOGL", "META", "AMZN"]

    # Map of ticker and news-table pair
    news_tables = {}

    # Goes through each ticker and parses into pared_data
    parsed_data = []
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

    # Organizes our list of arrays into a dataframe
    df = pd.DataFrame(parsed_data, columns=['ticker', 'date', 'time', 'title'])

    # Sentiment analysis score range from -1 to 1, lambda function 
    vader = SentimentIntensityAnalyzer()
    temp = lambda title: vader.polarity_scores(title)['compound']
    df['compound'] = df['title'].apply(temp)

    # Groups together all of the rows with the same ticker and date and finds the mean of the compound column
    mean_df = df.groupby(['ticker', 'date'])["compound"].mean().unstack().transpose()   

    # Replace NaN values with 0
    mean_df.fillna(0, inplace=True)
    
    print(mean_df)
    return mean_df
