# main data collection script that calls each parsing function and writes to json file
from parsers.CMU_QA_parser import parse_CMU_QA_ds
from parsers.meta_convo_parser import parse_meta_convo_ds
from parsers.wiki_QA_parser import parse_wiki_QA_ds
from parsers.MultiWOZ_parser import parse_MultiWOZ_ds
from parsers.CoQA_parser import parse_CoQA_ds
import re
import json


data = parse_CMU_QA_ds()
print("parsed CMU ds")
data += parse_meta_convo_ds()
print("parsed meta ds")
data += parse_wiki_QA_ds()
print("parsed wiki ds")
# data += parse_MultiWOZ_ds()
# print("parsed multiwoz ds")
data += parse_CoQA_ds()
print("parsed coqa ds")

with open("data.json", "w", encoding="utf-8") as f:
    f.truncate(0)
    spaces = re.compile("\s+")
    punctuation = re.compile("([.,?!():])")
    possesives = re.compile("'s")
    processedData = [re.sub(spaces, " ", re.sub(punctuation, r" \1", re.sub(possesives, " 's", d))) for d in data if isinstance(d, str)]
    json.dump({"data": processedData}, f, ensure_ascii=True, indent=4)
print("all data successfully processed")
