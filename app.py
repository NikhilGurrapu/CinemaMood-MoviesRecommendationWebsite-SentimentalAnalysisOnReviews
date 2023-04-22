import streamlit as st
import pickle
import pandas as pd
import requests

st.set_page_config(layout="wide")


def fetch_review(movie_id):
    respReview = requests.get("https://api.themoviedb.org/3/movie/{}/reviews?api_key=45661fea22e52c1f66135810d9c4186c&language=en-US".format(movie_id))
    reviews = pd.DataFrame(respReview.json()['results'])
    r_author = []
    r_content = []
    for i in range(reviews.shape[0]):
        r_author.append(reviews['author'][i])
        r_content.append(reviews['content'][i])
    return r_author, r_content


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
        n_data.append(url + str(x))
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
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[0:11]
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
    r_author, r_content = fetch_review(movies.iloc[movies_list[0][0]].movie_id)
    vote_average.append(movies.iloc[movies_list[0][0]].vote_average)
    vote_count.append(movies.iloc[movies_list[0][0]].vote_count)
    genre.append(movies.iloc[movies_list[0][0]].genres)
    overview.append(movies.iloc[movies_list[0][0]].overview)
    date.append(movies.iloc[movies_list[0][0]].release_date)
    runtime.append(movies.iloc[movies_list[0][0]].runtime)
    status.append(movies.iloc[movies_list[0][0]].status)
    return recommended_movies, recommended_posters, overview, vote_average, vote_count, genre, date, runtime, status, cast_list, cast_names, r_author, r_content


movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title('MOVIES WEBSITE')
st.subheader('Movie details, Cast details along with recommended movies made by _Nikhil Gurrapu :)_ ')
st.title(' ')
selected_movie = st.selectbox('Type or select the movie you want !', movies['title'].values)
if st.button('Search'):
    names, posters, overview, vote_average, vote_count, genre, date, runtime, status, cast_list, cast_names, r_author, r_content = recommend(
        selected_movie)
    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            st.image(posters[0])
        with right_column:
            st.title(names[0])
            st.subheader("OVERVIEW ")
            st.markdown(overview[0])
            st.subheader("RATING:   " + str(vote_average[0]) + "/10 (" + str(vote_count[0]) + " counts)")
            st.subheader("GENRE: ")
            s = " | "
            st.subheader(s.join(genre[0]))
            st.subheader("RELEASE DATE:   " + str(date[0]))
            st.subheader("RUNTIME:   " + str(runtime[0]) + " hours")
            st.subheader("STATUS:   " + str(status[0]))

    with st.container():
        st.title(' ')
        st.title("Top Cast")
        col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
        with col1:
            st.image(cast_list[0], width=180)
            st.text(cast_names[0])
        with col2:
            st.image(cast_list[1], width=180)
            st.text(cast_names[1])
        with col3:
            st.image(cast_list[2], width=180)
            st.text(cast_names[2])
        with col4:
            st.image(cast_list[3], width=180)
            st.text(cast_names[3])
        with col5:
            st.image(cast_list[4], width=180)
            st.text(cast_names[4])
        with col6:
            st.image(cast_list[5], width=180)
            st.text(cast_names[5])
        with col7:
            st.image(cast_list[6], width=180)
            st.text(cast_names[6])

    with st.container():
        st.title(' ')
        st.title("Recommended movies")
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
    with st.container():
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.image(posters[6])
            st.text(names[6])
        with col2:
            st.image(posters[7])
            st.text(names[7])
        with col3:
            st.image(posters[8])
            st.text(names[8])
        with col4:
            st.image(posters[9])
            st.text(names[9])
        with col5:
            st.image(posters[10])
            st.text(names[10])

    st.title(' ')
    st.title("Reviews")
    for i in range(len(r_author)):
        with st.container():
            st.subheader(r_author[i])
            st.markdown(r_content[i])
