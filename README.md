# CS685SOQuestionClosed

We explore the task of predicting if a StackOverflow question is likely to be closed using information that is only available at time of submission, i.e: the title of the question, the body of the question and the question tags. Our project addresses this as a multi-class classification task on set of imbalanced labels. The labels are the reasons for question closure.

## Dataset
[Dataset Link](https://drive.google.com/file/d/1cAU5hDfhKXxMdyICd3o6WapxIhR79n0E/view)
Use the file `so_dataset_cleaned.csv` the title,body and tags can be tokenized by `\t`


Analysis data (50): https://drive.google.com/file/d/1Ef-qz319jHVsArOI_fjHrGam9HalXXJO/view?usp=sharing

## Colab Notebook:
Colab ML: https://colab.research.google.com/drive/10lpI0XfhPRfsSjP893-yFBZvvzS7UYnr?usp=sharing

Colab BERT: https://colab.research.google.com/drive/1GqPpH9MgaW0R7Q4j4SsLkdC6BSGClOeT?usp=sharing

Colab BERT with losses and data augmentation: https://colab.research.google.com/drive/1U7OFU5JLX5EWt9AO4DE4qRI2bk91a_QB?usp=sharing

## Word Vectors
[ELMo Files](https://drive.google.com/drive/folders/1iEEMr2DYofulK2F5pSErOPf5ggrEqtJt): download and unzip elmo_vectors.zip

[SO Word2Vec](https://github.com/vefstathiou/SO_word2vec): Alternative? w2v embeddings for software engineering domain, file is very large ~1.5GB

