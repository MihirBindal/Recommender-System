import streamlit as st
from main import get_movie_user_likes, get_recommendations
import main

li = main.df.iloc[:, 7].tolist()
li.insert(0, "")
st.write("""
# Recommender System
""")
st.header('Enter your favorite movie')
movie = st.selectbox('Enter your favorite movie', li)
if movie != "":
    st.write("Top five movies are")
    get_movie_user_likes(movie)
    movies = get_recommendations()
    for m in movies:
        st.write(m)
