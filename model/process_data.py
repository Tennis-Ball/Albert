# A processing script for main.py
import json
import numpy as np
import tensorflow as tf


# size in percentage of total data, split in form (train%, test%, val%)
def process_data(size: int=100, split: (int)=(80, 15, 5)) -> object:
    xtrain, ytrain, xtest, ytest, xval, yval = np.array()
    return xtrain, ytrain, xtest, ytest, xval, yval
