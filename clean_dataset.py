import concurrent
import re
import sys

import numpy as np
import pandas as pd

from so_tokenizers.SOTokenizer import ark_twokenize, stokenizer
from so_tokenizers.utils import get_tag_list, TOKEN_SEP, just_text

from pebble import ProcessPool


def clean_title(title):
    try:
        return TOKEN_SEP.join(ark_twokenize.tokenizeRawTweetText(title))
        # TODO: doesn't work on titles
        # return stokenizer.tokenize(title)
    except:
        print("Error", title)


def clean_tags(tag_list):
    return get_tag_list(tag_list)


def clean_body(body):
    clean_html = re.compile('<.*?>')
    clean_body = re.sub(clean_html, '', body)

    clean_filepath = re.compile('^(.+)\/([^\/]+)$')
    clean_body = re.sub(clean_filepath, '', body)

    def remove_token(x):
        return all(term not in x for term in ["https", ":/", "//"])

    tokens = ark_twokenize.tokenizeRawTweetText(clean_body)
    tokens = list(filter(remove_token, tokens))
    return TOKEN_SEP.join(tokens)


def main():
    np.random.seed(123)
    df = pd.read_csv('data/SO_dataset_full.csv')
    df['Tags'] = df['Tags'].apply(clean_tags)
    df['Title'] = df['Title'].apply(clean_title)
    df['Body'] = df['Body'].apply(lambda x: clean_body(just_text(x)))

    # for index, r in df.iterrows():
    #     text = r['Body']
    #     # print(text)
    #     cleaned_text = just_text(text)
    #     tokenized_body = clean_body(cleaned_text)

        # TODO: not used anymore, SOTokenizer fails on several rows
        # with ProcessPool() as pool:
        #     future = pool.schedule(stokenizer.tokenize, args=[cleaned_text])
        #
        #     # if running, the container process will be terminated
        #     # a new process will be started consuming the next task
        #     try:
        #         result_text = future.result(timeout=0.5)
        #     except IndexError:
        #         result_text = ""
        #         future.cancel()
        #     except concurrent.futures.TimeoutError:
        #         print("this took too long...", index)
        #         result_text = ""
        #         future.cancel()

    df = df.replace("", pd.np.nan)
    df = df.dropna(subset=['Body'])
    df.to_csv("data/so_dataset_cleaned.csv", index=False)

if __name__ == '__main__':
    main()
