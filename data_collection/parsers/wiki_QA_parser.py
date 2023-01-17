# Wikipedia Question-Answer Corpus parser
import os

def parse_wiki_QA_ds() -> [str]:

    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..","datasets/WikiQACorpus/WikiQA-train.txt"))
    raw = open(file_path, 'r').read()
    processed = [processLine(l) for l in raw.splitlines()]
    return processed

def processLine(line:str) -> str:
    parts = line.split("\t")[:2]
    return "Spkr1: " + parts[0] + " Spkr2: " + parts[1]
