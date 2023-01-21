# A processing script for main.py
import json
import numpy as np
import matplotlib.pyplot as plt
# import tensorflow as tf

def get_data() -> [str]:
    file = open("../data_collection/data.json").read()
    return list(filter(lambda x:x != None and len(x) < 2100 and len(x) > 30,json.loads(file)["data"]))

# size in percentage of total data, split in form (train%, test%, val%)
def process_data(size: int=100, split: (int,int,int)=(80, 15, 5)) -> object:
    data = get_data()
    plt.hist([len(x) for x in data], bins=100)
    plt.show()
    print(len(data))
    xtrain, ytrain, xtest, ytest, xval, yval = np.array()
    return xtrain, ytrain, xtest, ytest, xval, yval

process_data()