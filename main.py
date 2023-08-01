# Request module (fetches html content of webpage)
from urllib.request import urlopen, Request

# Parsing module (converts html file into Pyton object to interact with html elements)
from bs4 import BeautifulSoup

# Add more websites and tickers later
finviz_base_url = "https://finviz.com/quote.ashx?t="
tickers = ["AMD", "AAPL", "GOOGL", "META"]

# Map of ticker and news-table pair
news_tables = {}

# Goes through each ticker
for t in tickers:
    url = finviz_base_url + t
    
    # Fetches request and recieves webpage
    req = Request(url= url, headers= {"user-agent": "'my-app"})
    response = urlopen(req)

    # Specifies webpage is html and only returns 'news-table' blocks
    html = BeautifulSoup(response, "html")
    newsTab = html.find(id='news-table')
    news_tables[t] = newsTab
