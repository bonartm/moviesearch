print('hello welcome to my new awesome package!')


def test_package():
    print('welcome discrete dill!!!')


import os
import pandas as pd
from fuzzywuzzy import process

library_path = os.path.dirname(__file__)

movies = pd.read_csv(library_path + '/data/movies.csv', index_col=0)

def get_top_matches(query, k=5):
    # [(movieId, title, genres), ...]
    matches = process.extract(query, movies['title'], limit=k)
    return matches

