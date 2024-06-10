import pandas as pd
import glob
import os

folder_path = 'data/HandDriver'

csv_files = glob.glob(os.path.join(folder_path, '*.csv'))

row_counts = []

dataframes = []

for file in csv_files:
    df = pd.read_csv(file)
    dataframes.append(df)
    row_counts.append(len(df))

min_rows = min(row_counts)

for i, file in enumerate(csv_files):
    df = dataframes[i]
    truncated_df = df.iloc[:min_rows]
    truncated_df.to_csv(file, index=False)

