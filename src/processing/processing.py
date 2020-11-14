from pathlib import Path

import numpy as np
import pandas as pd


def main():
    data_path = (Path(__file__).parent / '../../data').resolve()
    ratings = pd.read_csv(data_path / 'raw/ml-latest-small/ratings.csv')
    ratings_matrix = ratings.pivot(index='userId', columns='movieId', values='rating').fillna(0)

    # remove movies not rated by anybody (ensuring we can correctly match movie ids and indices)
    movies = pd.read_csv(data_path / 'raw/ml-latest-small/movies.csv')
    movies = movies[movies.movieId.isin(ratings_matrix.columns)]
    movies.to_csv(data_path / 'processed/movies.csv', index=False)

    ratings_matrix = ratings_matrix.to_numpy()
    with open(data_path / 'processed/ratings.npy', 'wb') as f:
        np.save(f, ratings_matrix)


if __name__ == '__main__':
    main()
