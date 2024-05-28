import pandas as pd

import os

file_path = './data/HandDriver'

doc_list = []

for doc in os.listdir(file_path):
    doc_path = os.path.join(file_path, doc)
    if os.path.isfile(doc_path):
        doc_list.append(doc_path)

for doc in doc_list:
    df = pd.read_csv(doc)
    df['timestamp_mills_ms'] = df['timestamp_mills_ms'].astype(str).str.replace('"', '').str.strip()
    df_clean = df.dropna()
    df_clean.to_csv(f'./data/HandDriverNew/cleaned_data{doc_list.index(doc)}.csv', index=False)
