# Multi-Domain Wizard-of-Oz dataset parser
import json
import requests


def parse_MultiWOZ_ds() -> str:   
    r = requests.get("https://datasets-server.huggingface.co/first-rows?dataset=multi_woz_v22&config=v2.2&split=train").content
    raw = [row["row"]["turns"]["utterance"] for row in json.loads(r)["rows"][:-1]]

    return [process_convo(convo) for convo in raw]

def process_convo(convo: [str]) -> str:
    return " ".join([f"Spkr1: {line}" if i%2==0  else f"Spkr2: {line}" for i, line in enumerate(convo)])

print(parse_MultiWOZ_ds()[0])