import streamlit as st
import pickle
import pandas as pd
import requests





similarity=pickle.load(open('similarity.pkl','rb'))
new_df=pickle.load(open('models.pkl','rb'))

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=36dbf3117ea46070a1def05ba56cb521&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w185"+data['poster_path']

def recommend(movie):
    # movie_index=new_df[new_df['title']==movie].index[0]
    # distances=similarity[movie_index]
    # movies=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    # recommended_movies_posters=[]
    # recommended=[]
    # for i in movies:
    #     movie_id=new_df.iloc[i[0]].movie_id
    #     recommended.append(new_df.iloc[i[0]]['title'])
    #     #fetch poster for api
    #     recommended_movies_posters.append(fetch_poster(movie_id))
    index = new_df[new_df['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = new_df.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(new_df.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters
    
    

st.title('Movie Recommender System')

movies_list=new_df['title'].values
selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
    (movies_list))
# st.button("Recommened", type="primary")
if st.button("Recommened"):
    names,posters = recommend(selected_movie_name)
    for i in names:
        st.text(i)
        # st.image(fetch_poster(new_df[new_df['title']==i]['movie_id'].values[0]))
    # col1, col2, col3, col4, col5 = st.columns(5)

    # with col1:
    #     st.text(names[0])
    #     # st.image(posters[0])

    # with col2:
    #     st.text(names[1])
    #     # st.image(posters[1])

    # with col3:
    #     st.text(names[2])
    #     # st.image(posters[2])
    # with col4:
    #     st.text(names[3])
    #     # st.image(posters[3])
    
    # with col5:
    #     st.text(names[4])
    #     # st.image(posters[4])

