from fuzzywuzzy import process
import pandas as pd
import os
print('hello welcome to my new awesome package!')


def test_package():
    print('welcome discrete dill!!!')


library_path = os.path.dirname(__file__)

movies = pd.read_csv(library_path + '/data/movies.csv', index_col=0)


def get_top_matches(query, k=5):
    # [(movieId, title, genres), ...]
    matches = process.extract(query, movies['title'], limit=k)
    return matches
