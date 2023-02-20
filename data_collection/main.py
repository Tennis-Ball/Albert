# main data collection script that calls each parsing function and writes to json file
from parsers.CMU_QA_parser import parse_CMU_QA_ds
from parsers.meta_convo_parser import parse_meta_convo_ds
from parsers.wiki_QA_parser import parse_wiki_QA_ds
from parsers.MultiWOZ_parser import parse_MultiWOZ_ds
from parsers.CoQA_parser import parse_CoQA_ds
import re
import json
import random


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
    #clears the file
    f.truncate(0)

    prompts = []
    responses = []

    for conversation in data:
        if type(conversation) != str: 
            continue

        spaces = re.compile("\s+")
        punctuation = re.compile("([.,?!():%$;])")
        possesives = re.compile("'s")
        ellipsis = re.compile("\. \. \.")

        conversation = \
            re.sub(ellipsis, "...", 
            re.sub(spaces, " ", 
            re.sub(punctuation, r" \1 ", 
            re.sub(possesives, " 's", conversation))))


        parts = list(filter(lambda x: (x.strip() != ""),re.split("Spkr1 |Spkr2 ", conversation)))
        if(len(parts) >= 2):
            for i in range(len(parts)-1):
                prompts.append(parts[i])
                responses.append(parts[i+1])

    json.dump({"prompts": prompts, "responses": responses}, f, ensure_ascii=True, indent=4)


print("all data successfully processed")
    