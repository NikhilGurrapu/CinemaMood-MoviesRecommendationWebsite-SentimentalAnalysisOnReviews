import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=45661fea22e52c1f66135810d9c4186c&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
def fetch_cast_profile(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}/credits?api_key=45661fea22e52c1f66135810d9c4186c&language=en-US'.format(movie_id))
    data = response.json()
    data = data['cast']
    profile_paths = [d['profile_path'] for d in data if 'profile_path' in d]
    n_data = []
    url = 'https://image.tmdb.org/t/p/w500'
    for x in profile_paths:
        n_data.append(url+str(x))
    return n_data
def fetch_cast_names(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}/credits?api_key=45661fea22e52c1f66135810d9c4186c&language=en-US'.format(movie_id))
    data = response.json()
    data = data['cast']
    cast_names = [d['name'] for d in data if 'name' in d]
    return cast_names
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[0:6]
    movie_id_main = movies.iloc[movies_list[0][0]].movie_id
    cast_list = fetch_cast_profile(movie_id_main)
    cast_names = fetch_cast_names(movie_id_main)
    recommended_posters = []
    recommended_movies = []
    overview = []
    vote_average = []
    vote_count = []
    genre = []
    date = []
    runtime = []
    status = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
        overview.append(movies.iloc[i[0]].overview)
        vote_average.append(movies.iloc[i[0]].vote_average)
        vote_count.append(movies.iloc[i[0]].vote_count)
        genre.append(movies.iloc[i[0]].genres)
        date.append(movies.iloc[i[0]].release_date)
        runtime.append(movies.iloc[i[0]].runtime)
        status.append(movies.iloc[i[0]].status)
    return recommended_movies, recommended_posters, overview, vote_average, vote_count, genre, date, runtime, status, cast_list, cast_names
movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
st.title('MOVIES WEBSITE')
st.caption('MOVIE DETAILS, CAST DETAILS ALONG WITH RECOMMENDED MOVIES MADE BY NIKHIL GURRAPU :)')
st.title(' ')
selected_movie = st.selectbox('Type or select the movie you want !',movies['title'].values)
if st.button('Search'):
    names, posters, overview, vote_average, vote_count, genre, date, runtime, status, cast_list, cast_names = recommend(selected_movie)
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.image(posters[0])
        with right_column:
            st.write("TITLE:   " + names[0])
            st.write("OVERVIEW ")
            st.write(*overview[0])
            st.write("RATING:   " + str(vote_average[0]) + "/10 (" + str(vote_count[0]) + " counts)")
            st.write("GENRE: ")
            st.write(*genre[0])
            st.write("RELEASE DATE:   "+str(date[0]))
            st.write("RUNTIME:   "+str(runtime[0])+" hours")
            st.write("STATUS:   "+str(status[0]))

    with st.container():
        st.title(' ')
        st.subheader("Top Cast")
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.image(cast_list[0])
            st.text(cast_names[0])
        with col2:
            st.image(cast_list[1])
            st.text(cast_names[1])
        with col3:
            st.image(cast_list[2])
            st.text(cast_names[2])
        with col4:
            st.image(cast_list[3])
            st.text(cast_names[3])
        with col5:
            st.image(cast_list[4])
            st.text(cast_names[4])

    with st.container():
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.image(cast_list[5])
            st.text(cast_names[5])
        with col2:
            st.image(cast_list[6])
            st.text(cast_names[6])
        with col3:
            st.image(cast_list[7])
            st.text(cast_names[7])
        with col4:
            st.image(cast_list[8])
            st.text(cast_names[8])
        with col5:
            st.image(cast_list[9])
            st.text(cast_names[9])

    with st.container():
        st.title(' ')
        st.subheader("Recommended movies")
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.image(posters[1])
            st.text(names[1])
        with col2:
            st.image(posters[2])
            st.text(names[2])
        with col3:
            st.image(posters[3])
            st.text(names[3])
        with col4:
            st.image(posters[4])
            st.text(names[4])
        with col5:
            st.image(posters[5])
            st.text(names[5])