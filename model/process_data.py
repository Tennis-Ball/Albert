# A processing script for main.py
import json
import numpy as np
import matplotlib.pyplot as plt


def get_data():
    file = open("../data_collection/data.json").read()
    return json.loads(file)

# size in percentage of total data, split in form (train%, test%, val%)
def process_data(size=1):
    data = get_data()  # get data
    data = list(zip(data["data"][0], data["data"][1]))  # (prompts, responses)
    np.random.shuffle(data)
    prompts, responses = zip(*data)  # unzip

    prompts = prompts[:int(len(prompts)*(size/100))]  # truncate to specified size
    responses = responses[:int(len(responses)*(size/100))]  # truncate to specified size
    prompts = np.array(prompts)  # convert to array
    responses = np.array(responses)  # convert to array
    print(f"Data points: {len(prompts)}")

    return prompts, responses


def hist():
    data = get_data()
    plt.hist([len(x) for x in data], bins=100)
    plt.show()
    print(len(data))


if __name__ == "__main__":
    process_data(10)
