from datetime import datetime
from pathlib import Path
from typing import Tuple

import numpy as np

from src.modeling import gmm, em
from src.modeling.gmm import GaussianMixture


def train_em(X: np.ndarray):
    mixture, post, log_likelihood = train_single_em_instance(X, 4, 0)


def train_single_em_instance(X: np.ndarray, K: int, seed: int) -> Tuple[GaussianMixture, np.ndarray, float]:
    mixture, post = gmm.init(X, K, seed)
    return em.train(X, mixture, post)


def save_gmm(mixture: GaussianMixture, parameters: Tuple, model_name: str = None, testing: bool = False):
    if not testing:
        model_path = (Path(__file__).parent / '../../model').resolve()
    else:
        model_path = (Path(__file__).parent / '../../test/model').resolve()
    if not model_name:
        model_name = 'model_' + str(int(datetime.timestamp(datetime.now())))
    with open(model_path / (model_name + '_weights.npy'), 'wb') as weights_f, \
            open(model_path / (model_name + '_means.npy'), 'wb') as means_f, \
            open(model_path / (model_name + '_variances.npy'), 'wb') as variances_f, \
            open(model_path / (model_name + '_parameters.txt'), 'w') as parameters_f:
        np.save(weights_f, mixture.weights)
        np.save(means_f, mixture.means)
        np.save(variances_f, mixture.variances)
        parameters_f.write(f'K={parameters[0]}, seed={parameters[1]}, achieved log-likelihood={parameters[2]}')


def main():
    data_path = (Path(__file__).parent / '../../data').resolve()
    with open(data_path / 'processed/ratings.npy', 'rb') as f:
        ratings = np.load(f)

    # training
    for K in [5, 10, 20]:
        best_ll = -10 ** 20
        for seed_power in range(1, 6):
            seed = 10 ** seed_power
            mixture, _, current_ll = train_single_em_instance(ratings, K, seed)
            print("K={}, seed={}, ll={}".format(K, seed, current_ll))
            if current_ll > best_ll:
                best_ll = current_ll
                model_name = 'model_' + str(K)
                save_gmm(mixture, (K, seed, best_ll), model_name)


if __name__ == '__main__':
    main()
