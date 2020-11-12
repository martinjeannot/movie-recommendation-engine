from pathlib import Path

import numpy as np

from src.modeling import train_model


def main():
    data_path = (Path(__file__).parent / '../data').resolve()
    X = np.loadtxt(data_path / 'test_incomplete.txt')
    K = 4
    seed = 0
    mixture, post, log_likelihood = train_model.train_single_em_instance(X, K, seed)
    train_model.save_gmm(mixture, seed, 'model_test', True)


if __name__ == '__main__':
    main()
