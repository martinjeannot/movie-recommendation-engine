from pathlib import Path

import numpy as np

from src.modeling import predict_model


def main():
    data_path = (Path(__file__).parent / '../data').resolve()
    X = np.loadtxt(data_path / 'test_incomplete.txt')
    mixture = predict_model.load_gmm('model_test', True)
    X_pred = predict_model.predict_em(X, mixture)
    print(X_pred)


if __name__ == '__main__':
    main()
