# # topic_modeling.py

# from gensim.models import LdaModel
# from gensim.corpora import Dictionary

# def perform_topic_modeling(df):
#     # Tokenize the headlines
#     tokenized_headlines = [headline.split() for headline in df['headline']]
    
#     # Create a dictionary representation of the documents
#     dictionary = Dictionary(tokenized_headlines)
    
#     # Convert tokenized documents into a document-term matrix
#     corpus = [dictionary.doc2bow(text) for text in tokenized_headlines]
    
#     # Train the LDA model
#     lda_model = LdaModel(corpus, num_topics=5, id2word=dictionary, passes=15)
    
#     return lda_model.print_topics()
