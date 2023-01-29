# Carnegie Mellon University Question-Answer Dataset parser
import pandas as pd


def parse_CMU_QA_ds():
    # only first doc (of 3) for now
    file_path = "datasets/CMU_QA_ds/QA_doc_1.txt"
    df = pd.read_csv(file_path, sep="\t", encoding="unicode_escape")

    # process pandas df: drop cols, rm null answers, drop dupes
    df = df.drop(["ArticleTitle", "DifficultyFromQuestioner",
                 "DifficultyFromAnswerer", "ArticleFile"], axis=1)
    df = df[df["Answer"].notna()]
    df = df.drop_duplicates("Question", keep="last")

    return [f"Spkr1 {row['Question']} Spkr2 {row['Answer']}" for i, row in df.iterrows()]
