# youtube_api.py
from googleapiclient.discovery import build
from config import API_KEY, KEYWORDS, MAX_RESULTS

def build_youtube_client():
    """
    Construye el cliente de la API de YouTube.
    """
    youtube = build("youtube", "v3", developerKey=API_KEY)
    return youtube

def search_videos(query, max_results=MAX_RESULTS):
    """
    Busca videos en YouTube según el query recibido.
    """
    youtube = build_youtube_client()

    request = youtube.search().list(
        part="snippet",
        q=query,
        type="video",
        maxResults=max_results,
        order="relevance"  # Puedes usar date, rating, viewCount, etc.
    )
    response = request.execute()
    return response

def get_video_details(video_ids):
    """
    Obtiene detalles avanzados de una lista de IDs de videos.
    """
    youtube = build_youtube_client()

    request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        id=",".join(video_ids)
    )
    response = request.execute()
    return response
