import streamlit as st
import pickle
import numpy as np


st.header("Books Recommender:Collaborative filtering")

model=pickle.load(open('artifacts/model.pkl','rb'))
books_name=pickle.load(open('artifacts/book_names.pkl','rb'))
final_rating=pickle.load(open('artifacts/final_rating.pkl','rb'))
book_pivot=pickle.load(open('artifacts/book_pivot.pkl','rb'))

def fetch_poster(suggestion):
    book_name=[]
    ids_index=[]
    poster_url=[]

    for book_id in suggestion:
        book_name.append(book_pivot.index[book_id])
    
    for name in book_name[0]:
        ids=np.where(final_rating['title']==name)[0][0]
        ids_index.append(ids)

    for idx in ids_index:
        url=final_rating.iloc[idx]['image_url']
        poster_url.append(url)

        #poster_url.append(url)



def recommend_books(book_name):
    book_list=[]
    book_id=np.where(book_pivot.index==book_name)[0][0] #[0][0] will filter the exact location
    distance,suggestion=model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1),n_neighbors=6)

    poster_url=fetch_poster(suggestion)

    for i in range(len(suggestion)):
        books=book_pivot.index[suggestion[i]]
        for j in books:
            book_list.append(j)

    return book_list,poster_url


    


selected_books=st.selectbox('Select/type a book:',books_name)
if st.button('Show Recommendations:'):
    recommendation_books,poster_url=recommend_books(selected_books)

    st.write("**1**:",recommendation_books[1],':blue_book:')

    st.write("**2**:",recommendation_books[2],':orange_book:')

    st.write("**3**:",recommendation_books[3],':green_book:')

    st.write("**4**:",recommendation_books[4],':notebook:')

    st.write("**5**:",recommendation_books[5],':blue_book:')
    
