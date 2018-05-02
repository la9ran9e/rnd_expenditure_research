import pandas as pd

df = pd.read_csv('../get_data_dataset.csv')

df = df.dropna(axis=0, how='any')

df.to_csv('./prepared_dataset.csv', index=None)
