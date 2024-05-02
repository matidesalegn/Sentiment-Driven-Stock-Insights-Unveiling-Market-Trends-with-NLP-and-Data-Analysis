# app.py
import streamlit as st
import pandas as pd
from data_analysis import sentiment_analysis, time_series_analysis, topic_modeling

def load_data():
    # Load dataset
    df = pd.read_csv('../data/raw_analyst_ratings.csv')
    return df

def main():
    st.markdown("<h1 style='text-align: center; color: red;'>Financial News Analysis</h1>", unsafe_allow_html=True)

    # Load data
    df = load_data()

    # Sidebar options
    analysis_option = st.sidebar.selectbox("Select Analysis", ["Sentiment Analysis", "Time Series Analysis", "Topic Modeling"])

    # Display analysis based on selected option
    if analysis_option == "Sentiment Analysis":
        df = sentiment_analysis.perform_sentiment_analysis(df)
        st.write(df.head())  # Display the dataframe with sentiment scores
    elif analysis_option == "Time Series Analysis":
        correlation = time_series_analysis.perform_time_series_analysis(df)
        st.markdown(f"<p style='color: blue;'>Correlation between sentiment score and stock price: {correlation}</p>", unsafe_allow_html=True)
    elif analysis_option == "Topic Modeling":
        topics = topic_modeling.perform_topic_modeling(df)
        st.markdown(f"<p style='color: green;'>Topics: {topics}</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
