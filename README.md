# movies-recommendations-website

#### Working Demo:- https://nikhilgurrapu-movies-recommendations-website-app-4qm2tu.streamlit.app/
#### Dataset link:- https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv


## How cosine similarity works for building Recommenders
A cosine similarity measure is used to determine what the difference is between two non-zero vectors of an inner product space. See the example below to understand.

![image](https://user-images.githubusercontent.com/96330046/162226114-8f4f7a6c-528b-494a-9ec7-40ddf2523894.png)

Each reviewer's ratings can be represented as a separate vector.

![image](https://user-images.githubusercontent.com/96330046/162226350-04c1149d-30c2-47a3-8294-ca71f3b86103.png)

These two vectors will be compared via cosine similarity, which is a measure of how similar their preferences are.

![image](https://user-images.githubusercontent.com/96330046/162226461-72088b63-ebab-4106-a28f-d30d6056f899.png)

A person's preferences are shown as vectors, and they have an angle θ between them. Similar vectors (i.e., different film preferences) have a smaller angle θ, while dissimilar vectors (i.e., different film preferences) have a larger angle θ.

![image](https://user-images.githubusercontent.com/96330046/162227061-80958aa7-6f46-42a7-8d4b-2dd6a30d0a57.png)

Based on only two movie reviews, the similarity between the two users of 0.989 is pretty close to the maximum value of 1, which indicates that they have similar preferences.

Because of the image of the cosine function, the cosine similarity can theoretically be any number between -1 and +1. In this case, there will not be any negative movie ratings; thus, angle * is between 0o and 90o, which bounds the cosine similarity between 0 and 1. If the angle θ = 0º =>cosine similarity = 1, if θ = 90º => cosine similarity =0.

As an example below, I will add Bernard's rating for a movie and Clarissa's rating for a movie that Bernard liked and Clarissa disliked. This will decrease the cosine similarity value.

![image](https://user-images.githubusercontent.com/96330046/162228285-a7150cb1-468b-4d83-a1aa-54649a2e3210.png)

The new vectors are:

![image](https://user-images.githubusercontent.com/96330046/162228406-1495d42c-6e0b-407c-af0f-b8be4531dbee.png)

The plot has 3 dimensions now:

![image](https://user-images.githubusercontent.com/96330046/162228469-07065804-0def-4dea-ade1-d24c85646281.png)

Calculating the similarity:

![image](https://user-images.githubusercontent.com/96330046/162228517-2a00448b-2e0f-4362-bc80-9baa669d12a2.png)

Based on the differences in ratings between the District 9 movie and The Hills Have Eyes, the similarity decreased from 0.989 to 0.792. The cosine can also be computed in Python using Sklearn.


