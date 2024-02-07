import streamlit as st
import pickle
import pandas as pd
similarity=pickle.load(open("simlarity.pkl","rb"))
def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommend_movies=[]
    for i in movie_list:
       recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies
movie_dict=pickle.load(open("movies_dict.pkl","rb"))
movies=pd.DataFrame(movie_dict)
st.title("Movie recommender System")

selected_movie_name = st.selectbox("choose any movie",
   movies["title"].values )
recomendation=recommend(selected_movie_name)
if st.button("Recommend"):
    for i in recomendation:
        st.write(i)

