import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../data/processed/youtube_cleaned.csv')

# Views over time
plt.figure(figsize=(12,6))
sns.lineplot(x='publishedAt', y='views', data=df)
plt.title("YouTube Views Over Time")
plt.xticks(rotation=45)
plt.savefig('../reports/visuals/youtube_views.png')

# Likes vs Comments
plt.figure(figsize=(8,5))
sns.scatterplot(x='likes', y='comments', data=df)
plt.title("Likes vs Comments")
plt.savefig('../reports/visuals/youtube_likes_comments.png')

print("EDA visuals saved!")
