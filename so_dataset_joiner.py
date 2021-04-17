import pandas as pd

if __name__ == '__main__':
    lables = {102: 1,
              103: 2,
              104: 3,
              105: 4}
    df_flagged = pd.read_csv('data/SO_dataset_flagged_qs.csv')
    df_flagged['label'] = df_flagged['CloseReasonTypeId'].apply(lambda x: lables[x])
    df_open = pd.read_csv('data/SO_dataset_unflag_qs.csv')
    df_open['label'] = 0

    df_open = df_open[['PostId', 'Title', 'Body', 'Tags', 'label']]
    df_flagged = df_flagged[['PostId', 'Title', 'Body', 'Tags', 'label']]
    df_open = df_open.append(df_flagged)
    print(df_flagged['label'].unique(), df_open['label'].unique())
    df_open = df_open.sample(frac=1.0)
    df_open.to_csv('data/SO_dataset_full.csv', index=False)
