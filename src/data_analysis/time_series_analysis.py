# time_series_analysis.py

# import pandas as pd

# def perform_time_series_analysis(df):
#     # Assuming df contains columns: 'date', 'sentiment_score', 'stock_price'
#     df['date'] = pd.to_datetime(df['date'])
#     df.set_index('date', inplace=True)
#     correlation = df['sentiment_score'].corr(df['stock_price'])
#     return correlation

# time_series_analysis.py

import pandas as pd

def perform_time_series_analysis(df):
    try:
        # Assuming df contains columns: 'date', 'sentiment_score', 'stock_price'
        df['date'] = pd.to_datetime(df['date'])
        df.set_index('date', inplace=True)
        correlation = df['sentiment_score'].corr(df['stock_price'])
        return correlation
    except Exception as e:
        print("Error occurred during time series analysis:", e)
        return None

