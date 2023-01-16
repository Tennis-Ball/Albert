# main data collection script that calls each parsing function and writes input to data file
from parsers.CMU_QA_parser import parse_CMU_QA_ds
from parsers.meta_convo_parser import parse_meta_convo_ds
from parsers.wiki_QA_parser import parse_wiki_QA_ds
from parsers.MultiWOZ_parser import parse_MultiWOZ_ds
from parsers.NPS_chat_parser import parse_NPS_chat_ds
from parsers.tf_CoQA_parser import parse_CoQA_ds
