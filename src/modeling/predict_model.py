from pathlib import Path

import numpy as np

from src.modeling import em
from src.modeling.gmm import GaussianMixture


def load_gmm(model_name: str, testing: bool = False) -> GaussianMixture:
    """Load the gaussian mixture model with the given name

    Args:
        model_name: name of the model
        testing: True if testing setup, false otherwise

    Returns:
        GaussianMixture: the gaussian mixture loaded
    """
    if not testing:
        model_path = (Path(__file__).parent / '../../model').resolve()
    else:
        model_path = (Path(__file__).parent / '../../test/model').resolve()
    with open(model_path / (model_name + '_weights.npy'), 'rb') as weights_f, \
            open(model_path / (model_name + '_means.npy'), 'rb') as means_f, \
            open(model_path / (model_name + '_variances.npy'), 'rb') as variances_f:
        weights = np.load(weights_f)
        means = np.load(means_f)
        variances = np.load(variances_f)
    return GaussianMixture(weights, means, variances)


def predict_em(X: np.ndarray, mixture: GaussianMixture) -> np.ndarray:
    return em.fill_missing_entries(X, mixture)
