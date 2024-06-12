import streamlit as st
import pickle
import pandas as pd
import requests

def movie_poster(movie_id):
    response =requests.get('https://api.themoviedb.org/3/movie/{}?api_key=65173168aaf0e2ee27d1c4020b47f70c&language=en-US'.format(movie_id))
    data =response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
movies_list = pickle.load(open("movies_dict.pkl", "rb"))
movies =pd.DataFrame(movies_list)
similarity = pickle.load(open("similarity.pkl", "rb"))

def recommendations(movie):
    movie_index = movies[movies['title']== movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies =[]
    recommended_movies_poster =[]
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(movie_poster(movies.iloc[i[0]].movie_id))
    return recommended_movies,recommended_movies_poster
st.title('Movie Recommendation System')
selected_movies_name = st.selectbox(
"How would you like to be contacted?",
(movies['title'].values))
if st.button("Recommend"):
    names,poster = recommendations(selected_movies_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(poster[0])

    with col2:
        st.text(names[1])
        st.image(poster[1])

    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])