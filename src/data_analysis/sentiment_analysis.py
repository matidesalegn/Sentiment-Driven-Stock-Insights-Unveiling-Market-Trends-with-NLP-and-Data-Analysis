# sentiment_analysis.py

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd

nltk.download('vader_lexicon')

def perform_sentiment_analysis(df):
    sia = SentimentIntensityAnalyzer()
    df['sentiment_score'] = df['headline'].apply(lambda x: sia.polarity_scores(x)['compound'])
    return df
