# TensorFlow's Conversational Question Answering Challenge parser
import json
import requests

def parse_CoQA_ds() -> [str]:
    r = requests.get("https://downloads.cs.stanford.edu/nlp/data/coqa/coqa-train-v1.0.json").content

    return [convo for topic in json.loads(r)["data"] for convo in process_topic(topic)]

def process_topic(topic: dict) -> [str]:
    return [f"Spkr2 {topic['story']} Spkr1 {topic['questions'][i]['input_text']} Spkr2 {topic['answers'][i]['input_text']}" for i in range(len(topic["questions"]))]
