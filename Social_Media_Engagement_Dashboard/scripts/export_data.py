import pandas as pd

df = pd.read_csv('../data/processed/youtube_cleaned.csv')
df.to_json('../data/processed/youtube_cleaned.json', orient='records', lines=True)
print("Data exported to CSV & JSON")
