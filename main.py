from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

cv = CountVectorizer()

df = pd.read_csv("movie_dataset.csv")
df = df.iloc[:, 0:24]

features = ['keywords', 'cast', 'genres', 'director']
for feature in features:
    df[feature] = df[feature].fillna(' ')


def combine_features(row):
    return row['keywords'] + " " + row['cast'] + " " + row['genres'] + " " + row['director']


df["combine_features"] = df.apply(combine_features, axis=1)
count_matrix = cv.fit_transform(df["combine_features"])
cosine_sim = cosine_similarity(count_matrix)

favorite_movie = ""


def get_movie_user_likes(movie):
    global favorite_movie
    favorite_movie = movie
    return favorite_movie


def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]


def get_index_from_title(title):
    return df[df.title == title]["index"].values[0]


def get_recommendations():
    li = []
    movie_index = get_index_from_title(favorite_movie)
    similar_movies = list(enumerate(cosine_sim[int(movie_index)]))
    sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)
    i = 0
    for movie in sorted_similar_movies:
        if 0 < i < 6:
            li.append(get_title_from_index(movie[0]))
        i = i + 1
    return li
