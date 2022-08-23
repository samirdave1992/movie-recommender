import streamlit as st

st.set_page_config(
    page_title="recommender systems",
    page_icon="👋",)

st.write("# Welcome to my recommender system app! 👋")



st.markdown(
    """
Recommender systems are basically algorithms that are aimed at suggesting contents(products, music, movies,videos etc)


### Types of recommender systems:
1. Content Based
2. Collaborative filtering
3. Hybrid recommender

**Content Based**:
It recommends contents based on similar attributes. Example: Watching more action movies will lead to more recommendations of action movies on yor streaming platfrom
The movie recommendation is content based where we find similar keywords in the description/content details
Data Shape:4k rows
Logic determined by: cosine similarity and vector spaces

**Collaborative filtering**:
This method is based on data collected from different users. Example: If User A likes Avengers and Spiderman, and has given 5 star rating. User B who starts watching Avengers will be recommended spiderman because the likelyhood is very high that user B will like it
The book recommendation is collaborative filtering approach which is based on users who completed the books and have provided good reviews. Any new user who picks a book will get recommendations on books that are highly rated and completed by other users
Data Shape: 58K rows
Logic determined by: Nearest neighbors on aggregated data of more than 50 ratings on a book
"""
)