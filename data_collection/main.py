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
    formattedData = [re.sub(spaces, " ", re.sub(punctuation, r" \1", re.sub(possesives, " 's", d))) for d in data if isinstance(d, str)]

    def splitData(text):
        parts = list(filter(None,re.split("Spkr1 |Spkr2 ", text)))
        if(len(parts)>=2):
            splitUp = (parts[0],parts[1])
            if(not (splitUp[0].isspace() and splitUp[1].isspace())):
                return splitUp

    splitUpData = list(filter(None,[splitData(d) for d in formattedData]))
    qaData = list(map(list, zip(*splitUpData)))
    json.dump({"data": qaData}, f, ensure_ascii=True, indent=4)
print("all data successfully processed")
