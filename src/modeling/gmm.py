from typing import NamedTuple, Tuple

import numpy as np


class GaussianMixture(NamedTuple):
    weights: np.ndarray  # (K,) - gaussian components weights
    means: np.ndarray  # (K, d) - gaussian components means
    variances: np.ndarray  # (K,) - gaussian components variances (we assume no covariance)


def init(X: np.ndarray, K: int, seed: int = 0) -> Tuple[GaussianMixture, np.ndarray]:
    np.random.seed(seed)
    n, _ = X.shape
    weights = np.ones(K) / K

    # select K random points as initial means
    means = X[np.random.choice(n, K, replace=False)]
    # init variances
    variances = [((X - means[i]) ** 2).mean() for i in range(K)]

    mixture = GaussianMixture(weights, means, np.array(variances))
    post = np.ones((K, n)) / K
    return mixture, post
