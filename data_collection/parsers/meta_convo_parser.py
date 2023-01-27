# Meta AI Conversational Dataset parser
import os
import json
import re


def parse_meta_convo_ds() -> [str]:
    file_path = os.path.abspath(os.path.join(os.path.dirname(
        __file__), "..", "datasets/meta_convo_ds/CasualConversations_transcriptions(1).json"))
    raw = open(file_path, 'r', encoding="unicode_escape").read()
    jsonObj = json.loads(raw)
    transcripts = [data['transcription'] for data in jsonObj]

    # stack overflowed
    extraTagsRegex = re.compile('[<\[].*?[>\]]')

    # I'm pretty sure first speaker is actually labeled secondary in this dataset
    firstSpeakerRegex = re.compile('\[secondary_.*?_secondary\]')

    secondSpeakerRegex = re.compile('\[primary.*?_primary\]')
    return [re.sub(extraTagsRegex, '', re.sub(secondSpeakerRegex, 'Spkr2', re.sub(firstSpeakerRegex, 'Spkr1', data))) for data in transcripts]
