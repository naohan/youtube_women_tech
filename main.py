# main.py
from youtube_api import search_videos, get_video_details
from config import KEYWORDS, MAX_RESULTS
from utils import save_to_csv, save_to_json, format_date

if __name__ == "__main__":
    all_data = []

    for keyword in KEYWORDS:
        print(f"\n🔎 Buscando: {keyword}")
        results = search_videos(keyword, max_results=MAX_RESULTS)

        video_ids = [
            item["id"]["videoId"]
            for item in results.get("items", [])
            if item["id"]["kind"] == "youtube#video"
        ]

        details = get_video_details(video_ids)

        for video in details["items"]:
            title = video["snippet"]["title"]
            published = format_date(video["snippet"]["publishedAt"])
            channel = video["snippet"]["channelTitle"]
            views = video["statistics"].get("viewCount", "0")
            likes = video["statistics"].get("likeCount", "0")

            print(f"🎥 {title} | 📺 {channel} | 👁 {views} views | 👍 {likes} likes | 📅 {published}")

            all_data.append({
                "title": title,
                "channel": channel,
                "views": views,
                "likes": likes,
                "publishedAt": published
            })

    # Guardar en CSV y JSON
    save_to_csv("resultados.csv", all_data, headers=["title", "channel", "views", "likes", "publishedAt"])
    save_to_json("resultados.json", all_data)
