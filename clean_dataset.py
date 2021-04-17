import numpy as np
import pandas as pd

from so_tokenizers.SOTokenizer import ark_twokenize
from so_tokenizers.utils import get_tag_list, TOKEN_SEP, just_text


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
    return TOKEN_SEP.join(ark_twokenize.tokenizeRawTweetText(body))


def main():
    np.random.seed(123)
    df = pd.read_csv('data/SO_dataset_full.csv')
    df['Tags'] = df['Tags'].apply(clean_tags)
    df['Title'] = df['Title'].apply(clean_title)
    df['Body'] = df['Body'].apply(lambda x: clean_body(just_text(x)))
    # for _, r in df.iterrows():
    #     text = r['Body']
    #     cleaned_text = just_text(text)
    #     print(cleaned_text)
    #     clean_body(cleaned_text)
    df.to_csv("data/so_dataset_cleaned.csv", index=False)


if __name__ == '__main__':
    main()
