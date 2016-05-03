import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def load_data(train_file, test_file):
    """ Load training and test data."""
    train = pd.read_csv(train_file)
    test = pd.read_csv(test_file)
    return train, test


def main(train_file='train.csv', test_file='test.csv',
         submit='logistic_pred.csv'):
    # Get all data
    train, test = load_data(train_file, test_file)
    # Run a naive classifier


if __name__ == "__main__":
    args = {'train_file': 'train.csv',
            'test_file': 'test.csv',
            'submit': 'logistic_regression_pred.csv'}
    main(**args)
