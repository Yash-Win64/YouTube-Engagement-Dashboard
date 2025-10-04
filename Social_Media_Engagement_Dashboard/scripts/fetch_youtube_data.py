import os
from googleapiclient.discovery import build
import pandas as pd

# ✅ Your API key and channel ID
API_KEY = "AIzaSyDQ9xI7DcdMDfoMGxG_ZJ6ys9YQ18FUW7k"
CHANNEL_ID = "UCjzHeG1KWoonmf9d5KBvSiw"

# Ensure folders exist
os.makedirs('../data/raw', exist_ok=True)
os.makedirs('../data/processed', exist_ok=True)
os.makedirs('../reports/visuals', exist_ok=True)

# Initialize YouTube API
youtube = build('youtube', 'v3', developerKey=API_KEY)

def fetch_channel_videos(channel_id):
    videos = []
    request = youtube.search().list(
        part="id",
        channelId=channel_id,
        maxResults=50,
        order="date"
    )
    response = request.execute()
    videos.extend(response['items'])
    video_ids = [v['id']['videoId'] for v in videos if 'videoId' in v['id']]
    return video_ids

def fetch_video_stats(video_ids):
    stats = []
    for i in range(0, len(video_ids), 50):
        request = youtube.videos().list(
            part="snippet,statistics",
            id=",".join(video_ids[i:i+50])
        )
        response = request.execute()
        stats.extend(response['items'])
    return stats

def main():
    video_ids = fetch_channel_videos(CHANNEL_ID)
    if not video_ids:
        print("❌ No videos found for this channel. Check if the channel ID is correct or has public videos.")
        return

    print(f"✅ Found {len(video_ids)} videos.")
    stats = fetch_video_stats(video_ids)
    
    data = []
    for v in stats:
        data.append({
            "video_id": v['id'],
            "title": v['snippet']['title'],
            "publishedAt": v['snippet']['publishedAt'],
            "views": int(v['statistics'].get('viewCount', 0)),
            "likes": int(v['statistics'].get('likeCount', 0)),
            "comments": int(v['statistics'].get('commentCount', 0))
        })
    
    df = pd.DataFrame(data)
    df.to_csv('../data/raw/youtube_data.csv', index=False)
    print("📄 YouTube data saved successfully at data/raw/youtube_data.csv")

if __name__ == "__main__":
    main()
