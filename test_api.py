from googleapiclient.discovery import build

# 1. PASTE YOUR API KEY HERE
API_KEY = ""

def get_video_comments(video_id):
    # Connect to YouTube API
    youtube = build("youtube", "v3", developerKey=API_KEY)

    # Request comments
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=5  # Let's just get 5 comments for now
    )
    response = request.execute()

    # Print them out
    print(f"--- Comments for Video ID: {video_id} ---\n")
    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        author = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
        print(f"User: {author}")
        print(f"Said: {comment}\n")
        print("-" * 30)

# Test with a real video (e.g., a random tech video ID)
# Video URL: https://www.youtube.com/watch?v=M7Lc1UVf-VE (Rick Roll)
get_video_comments("dQw4w9WgXcQ")
