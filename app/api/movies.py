from pathlib import Path

import pandas as pd
from flask import jsonify, request

from . import movies
from ..models import Movie

movies_df = pd.read_csv((Path(__file__).parent / '../../data/raw/ml-latest-small/movies.csv').resolve())


@movies.route('/list')
def compute():
    title = request.args.get('title')
    if not title or len(title) <= 2:
        return jsonify([])
    movie_list = movies_df[movies_df.title.str.contains('(?i)' + title)]
    return jsonify([vars(Movie(movie)) for movie in movie_list.itertuples()])
