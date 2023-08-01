# Request module
from urllib.request import urlopen, Request

# Scrapping module
from bs4 import BeautifulSoup

finvizUrl = "https://finviz.com/quote.ashx?t="
tickers = ["AMD", "AAPL", "GOOGL", "META"]

newsTables = {}

for t in tickers:
    url = finvizUrl + t
    
    req = Request(url= url, headers= {"user-agent": "'my-app"})
    response = urlopen(req)

    html = BeautifulSoup(response, "html")
    newsTab = html.find(id='news-table')
    newsTables[t] = newsTab

    break

print(newsTables)