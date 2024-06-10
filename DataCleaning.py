import os
import pandas as pd

# Specify the folder path
file_path = 'Old Data/HandDriverOld'
new_file_path = 'data/HandDriver'

# Create a list to store file names
doc_list = []

# List files in folder and add to list
for docs in os.listdir(file_path):
    doc_path = os.path.join(file_path, docs)
    if os.path.isfile(doc_path) and docs.endswith('.csv'):
        doc_list.append(doc_path)

# Perform data cleanup for each file
for doc_path in doc_list:
    df = pd.read_csv(doc_path)

    # Remove double quotes and spaces from timestamp_mills_ms column
    df['timestamp_mills_ms'] = (df['timestamp_mills_ms'].astype(str)
                                .str.replace('"', '').str.strip())

    # Delete empty rows (delete rows with NaN in any cell)
    df_clean = df.dropna()
    # Save the cleaned data to a new CSV file
    new_file_path = os.path.join(file_path, 'cleaned_' + os.path.basename(doc_path))
    df_clean.to_csv(new_file_path, index=False)

    print(f"{doc_path} is cleaned and saved into {new_file_path}.")
