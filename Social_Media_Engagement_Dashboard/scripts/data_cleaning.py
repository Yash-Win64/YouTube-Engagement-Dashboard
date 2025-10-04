import pandas as pd

df = pd.read_csv('../data/raw/youtube_data.csv')
df['publishedAt'] = pd.to_datetime(df['publishedAt'])
df.fillna(0, inplace=True)
df.to_csv('../data/processed/youtube_cleaned.csv', index=False)
print("Data cleaned and saved!")
