# A processing script for main.py
import json
import numpy as np
import matplotlib.pyplot as plt
import re
# import tensorflow as tf


def get_data():
    file = open("../data_collection/data.json").read()
    return list(filter(lambda x: len(x) < 2100 and len(x) > 30,json.loads(file)["data"]))


# size in percentage of total data, split in form (train%, test%, val%)
def process_data(size=100, split=(80, 15, 5)):
    data = get_data()  # get data

    np.random.shuffle(data)
    data = data[:int(len(data)*(size/100))]  # truncate to specified size
    data = np.array(data)  # convert to array

    # calculate data split indices
    train_i = int(len(data)*(split[0]/100))
    test_i = int(len(data)*(split[1]/100)) + train_i
    train, test, val = data[:train_i], data[train_i:test_i], data[test_i:]  # split
    print("train/test/val split:", len(train), len(test), len(val))

    return train, test, val


def hist():
    data = get_data()
    plt.hist([len(x) for x in data], bins=100)
    plt.show()
    print(len(data))


if __name__ == "__main__":
    process_data(10, (85, 10, 5))
