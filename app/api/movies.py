from pathlib import Path

import numpy as np
import pandas as pd
from flask import jsonify, request

from src.modeling import predict_model
from . import movies
from ..models import Movie, Recommendation

movies_df = pd.read_csv((Path(__file__).parent / '../../data/processed/movies.csv').resolve())
gmm = predict_model.load_gmm('model_50')


@movies.route('/list')
def get_movies():
    title = request.args.get('title')
    if not title or len(title) <= 2:
        return jsonify([])
    movie_list = movies_df[movies_df.title.str.contains('(?i)' + title)]
    return jsonify([vars(Movie(movie)) for movie in movie_list.itertuples()])


@movies.route('/recommendations')
def get_recommendations():
    movie_indices = request.args.getlist('indices', type=int)
    ratings = request.args.getlist('ratings', type=float)
    if any([not movie_indices, not ratings, len(movie_indices) <= 4, len(movie_indices) != len(ratings)]):
        return jsonify([])
    X = np.zeros((1, len(movies_df)))
    for movie_id, rating in zip(movie_indices, ratings):
        X[0, movie_id] = rating
    predictions = predict_model.predict_em(X, gmm)
    predictions = np.where(X == 0, predictions, 0)
    recommendations_indices = np.argpartition(predictions, -5)[0, -5:]
    recommendations = movies_df.iloc[recommendations_indices]
    recommendations = [Recommendation(movie, prediction) for movie, prediction in
                       zip(recommendations.itertuples(), predictions[0, recommendations_indices])]
    recommendations.reverse()
    return jsonify([vars(recommendation) for recommendation in recommendations])
