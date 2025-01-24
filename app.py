import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)),reverse = True,key=lambda x:x[1])[1:11]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies



movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity= pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movies_name = st.selectbox('how would you like to be contact?',(movies['title'].values))

if st.button('Recommend'):
    recommendations =recommend(selected_movies_name)

    for i in recommendations:
        st.write(i)
