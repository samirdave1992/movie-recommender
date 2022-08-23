import pickle
import streamlit as st
import requests



st.header("Movie Recommender System:content based")
st.markdown("""
    1. Data collected from:[TMDB](https://www.themoviedb.org/?language=en-US)
    2. Recommendation list limited to 5 movies only
""")


#with open('artifacts/movie_list.pkl','rb') as mov:
 #   movies=pickle.load(mov)

#with open('artifacts/similarity.pkl','rb') as sim:
 #   similarity=pickle.load(sim)

movies=pickle.load(open('artifacts/movie_list.pkl','rb'))
similarity=pickle.load(open('artifacts/similarity.pkl','rb'))

movie_list=movies['title'].values

st.write('***')
selected=st.selectbox('Select/type a movie',movie_list)

def fetch_poster(movie_id):
    url="https://api.themoviedb.org/3/movie/{}?api_key=98d80aa5886311256c4a0fd9cb1bee71&language=en-US".format(movie_id)
    data=requests.get(url)
    data=data.json()
    poster_path=data['poster_path']
    full_path="http://image.tmdb.org/t/p/w500" + poster_path
    return full_path

#http://image.tmdb.org/t/p/w500/cnUkc60SkI1PCY1SyfLFpZc0T7C.jpg


@st.cache()
def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distance=sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x:x[1])
    recommended_movies=[]
    recommended_movies_poster=[]
    for i in distance[1:6]:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies.append(movies.iloc[i[0]].title)  
    return recommended_movies,recommended_movies_poster


if st.button('Show Recommendations'):
    recommended_movies,recommended_movies_poster=recommend(selected)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(recommended_movies[0])
        st.image(recommended_movies_poster[0])

    with col2:
        st.text(recommended_movies[1])
        st.image(recommended_movies_poster[1])

    with col3:
        st.text(recommended_movies[2])
        st.image(recommended_movies_poster[2])

    with col4:
        st.text(recommended_movies[3])
        st.image(recommended_movies_poster[3])
    
    with col5:
        st.text(recommended_movies[4])
        st.image(recommended_movies_poster[4])
