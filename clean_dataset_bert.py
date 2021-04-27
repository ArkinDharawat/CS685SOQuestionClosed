import re

import numpy as np
import pandas as pd

from so_tokenizers.SOTokenizer import ark_twokenize
from so_tokenizers.utils import get_tag_list, TOKEN_SEP, just_text

from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("jeniya/BERTOverflow")

def clean_title(title):
    return title.lower()


def clean_tags(tag_list):
    return get_tag_list(tag_list)


def main():
    np.random.seed(123)
    df = pd.read_csv('data/SO_dataset_full.csv')
    df['Tags'] = df['Tags'].apply(clean_tags)
    df['Title'] = df['Title'].apply(clean_title)
    df['Body'] = df['Body'].apply(lambda x: just_text(x).lower())

    df = df.replace("", pd.np.nan)
    df = df.dropna(subset=['Body'])

    # title = df.iloc[0]['Title']
    # body = df.iloc[0]['Body']
    # title_token_ids = tokenizer.encode(title)
    # body_tokens_ids = tokenizer.encode(body)
    # print(title_token_ids)
    # print(body_tokens_ids)

    df.to_csv('so_dataset_cleaned_bert.csv', index=False)


if __name__ == '__main__':
    main()
