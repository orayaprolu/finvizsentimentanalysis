# Pandas module allows for flexible usage of data
import pandas as pd

# Corpus and sentiment analysis algorithm
from nltk.sentiment.vader import SentimentIntensityAnalyzer
 
def mean_sentiment_score (parsed_data):

    # Organizes our list of arrays into a dataframe
    df = pd.DataFrame(parsed_data, columns=['ticker', 'date', 'time', 'title'])

    # Sentiment analysis score range from -1 to 1, lambda function 
    vader = SentimentIntensityAnalyzer()
    temp = lambda title: vader.polarity_scores(title)['compound']
    df['compound'] = df['title'].apply(temp)
    df['date'] = pd.to_datetime(df['date'])

    # Groups together all of the rows with the same ticker and date and finds the mean of the compound column into a new df
    mean_df = df.groupby(['ticker', 'date'])["compound"].mean().unstack().transpose().reset_index()

    # Replace NaN values with 0
    mean_df.fillna(0, inplace=True)

    print(mean_df)
    print("------")
    print(mean_df.index)
    print("------")
    print(mean_df.columns)
    return mean_df
