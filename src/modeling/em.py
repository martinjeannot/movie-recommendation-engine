import math
from typing import Tuple

import numpy as np
from scipy.special import logsumexp

from src.modeling.gmm import GaussianMixture


def e_step(X: np.ndarray, mixture: GaussianMixture) -> Tuple[np.ndarray, float]:
    """E-step : Softly assigns each datapoint to a gaussian component

    Args:
        X: (n, d) array holding the data, missing entries set to 0
        mixture: the current gaussian mixture

    Returns:
        np.ndarray: (K, n) array holding the soft counts for each components for all examples
        float : the current log-likelihood
    """
    K = len(mixture.weights)
    normals = np.repeat(X[np.newaxis, :, :], K, axis=0)  # (K,n,d)
    mask = normals.copy()
    mask[mask > 0] = 1
    # compute the soft counts for each components for all examples
    normals = normals - mixture.means[:, np.newaxis, :]
    variances = mixture.variances[:, np.newaxis, np.newaxis]
    normals = np.exp(normals ** 2 / (-2 * variances))
    normals = normals / np.sqrt(2 * math.pi * variances)
    normals = normals * mask
    normals[normals == 0] = 1
    normals = np.sum(np.log(normals), axis=2)  # (K, n)
    f_users = np.log(mixture.weights[:, np.newaxis]) + normals
    lse = logsumexp(f_users, axis=0)
    post = np.exp(f_users - lse[np.newaxis, :])
    # compute log-likelihood
    # log_likelihood = np.sum(np.log(np.sum(np.exp(normals) * mixture.weights[:, np.newaxis], axis=0)))
    log_likelihood = np.sum(logsumexp(f_users, axis=0))
    return post, log_likelihood


def m_step(X: np.ndarray, post: np.ndarray, mixture: GaussianMixture, min_variance: float = 0.25) -> GaussianMixture:
    """M-step : updates the gaussian mixture by maximizing the lok-likelihood of the weighted dataset

    Args:
        X: (n, d) array holding the data, missing entries set to 0
        post: (K, n) array holding the soft counts
        mixture: the current gaussian mixture
        min_variance: the minimum variance for any of the gaussian components

    Returns:
        GaussianMixture: the updated gaussian mixture
    """
    n, d = X.shape
    K = len(post)
    # compute new weights
    weights = np.sum(post, axis=1) / n
    # compute new means
    means = X[np.newaxis, :, :] * post[:, :, np.newaxis]  # (K, n, d)
    means_denominator = X.copy()  # (n, d)
    means_denominator[means_denominator > 0] = 1
    means_denominator = means_denominator[np.newaxis, :, :] * post[:, :, np.newaxis]  # (K, n, d)
    means_mask = means_denominator.copy()
    # means = np.sum(means, axis=1) / np.sum(means_denominator, axis=1)
    means = np.log(np.sum(means, axis=1) + 1e-16)
    means_denominator = np.log(np.sum(means_denominator, axis=1) + 1e-16)
    means = np.exp(means - means_denominator)
    # only retains means which are supported by at least one full point
    means_mask = np.sum(means_mask, axis=1)
    means = np.where(means_mask >= 1, means, mixture.means)
    # compute new variances
    variances = np.square(X[np.newaxis, :, :] - means[:, np.newaxis, :])  # (K, n, d)
    variances = variances * post[:, :, np.newaxis]
    mask = X.copy()
    mask[mask > 0] = 1
    variances = variances * mask[np.newaxis, :, :]
    variances = np.sum(variances, axis=2)  # (K, n)
    variances_denominator = np.repeat(X[np.newaxis, :, :], K, axis=0)  # (K, n, d)
    variances_denominator[variances_denominator > 0] = 1
    variances_denominator = np.sum(variances_denominator, axis=2)  # (K, n)
    variances_denominator = variances_denominator * post
    variances = np.sum(variances, axis=1) / np.sum(variances_denominator, axis=1)
    variances[variances < min_variance] = min_variance
    return GaussianMixture(weights, means, variances)


def train(X: np.ndarray, mixture: GaussianMixture, post: np.ndarray) -> Tuple[GaussianMixture, np.ndarray, float]:
    """Train a gaussian mixture model against the given dataset

    Args:
        X: (n, d) array holding the data, missing entries set to 0
        mixture: the current gaussian mixture
        post: (K, n) array holding the soft counts

    Returns:
        GaussianMixture: the final gaussian mixture
        np.ndarray: (n, K) array holding the soft counts
        float: the current log-likelihood
    """
    prev_ll = -10 ** 21
    current_ll = -10 ** 20
    ll_history = []
    while current_ll - prev_ll > abs(current_ll) * 10 ** -6:
        prev_ll = current_ll
        post, current_ll = e_step(X, mixture)
        mixture = m_step(X, post, mixture)
        ll_history.append(current_ll)
    # print(ll_history)
    return mixture, post, current_ll


def fill_missing_entries(X: np.ndarray, mixture: GaussianMixture) -> np.ndarray:
    """Fill the missing entries of the given array according to the given gaussian mixture

    Args:
        X: (n, d) array holding the data, missing entries set to 0
        mixture: a gaussian mixture

    Returns:
        np.ndarray: (n, d) array with completed data
    """
    post, _ = e_step(X, mixture)
    X_pred = post.T @ mixture.means
    X_pred = np.where(X == 0, X_pred, X)
    return X_pred
