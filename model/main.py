# The main script which declares model architecture and trains
from process_data import process_data
import tensorflow as tf


xtrain, ytrain, xtest, ytest, xval, yval = process_data(5, (100, 0, 0))
