from supabase_setup import supabase
from typing import List, Dict
import uuid

def insert_tracks(tracks: List[Dict]):
    for track in tracks:
        data = {
            "id": track.get("id", str(uuid.uuid4())),
            "name": track["name"],
            "duration_ms": track.get("duration_ms"),
            "popularity": track.get("popularity"),
            "album_id": track.get("album_id"),
            "artist_id": track.get("artist_id")
        }
        supabase.table("tracks").insert(data).execute()

def insert_albums(albums: List[Dict]):
    for album in albums:
        data = {
            "id": album.get("id", str(uuid.uuid4())),
            "name": album["name"],
            "release_date": album.get("release_date"),
            "artist_id": album.get("artist_id")
        }
        supabase.table("albums").insert(data).execute()

def insert_artists(artists: List[Dict]):
    for artist in artists:
        data = {
            "id": artist.get("id", str(uuid.uuid4())),
            "name": artist["name"],
            "popularity": artist.get("popularity"),
            "genres": artist.get("genres", [])
        }
        supabase.table("artists").insert(data).execute()

def insert_audio_features(features: List[Dict]):
    for feature in features:
        data = {
            "track_id": feature["id"],
            "danceability": feature.get("danceability"),
            "energy": feature.get("energy"),
            "valence": feature.get("valence"),
            "tempo": feature.get("tempo"),
            "acousticness": feature.get("acousticness"),
            "instrumentalness": feature.get("instrumentalness"),
            "liveness": feature.get("liveness"),
            "speechiness": feature.get("speechiness")
        }
        supabase.table("track_features").insert(data).execute()

def insert_clustered_data(track_cluster_map: Dict[str, str]):
    for track_id, cluster_id in track_cluster_map.items():
        data = {
            "track_id": track_id,
            "cluster_id": cluster_id
        }
        supabase.table("track_clusters").insert(data).execute()
def ingest_all_data(artists: List[Dict], albums: List[Dict], tracks: List[Dict], features: List[Dict], cluster_map: Dict[str, str]):
    print("Begin data ingestion")

    insert_artists(artists)
    print("Artists added to celestial records.")

    insert_albums(albums)
    print("Albums inscribed in the cosmic library.")

    insert_tracks(tracks)
    print("tracks entered into the celestial archives.")

    insert_audio_features(features)
    print("✅ Audio features whispered into the wind.")

    insert_clustered_data(cluster_map)
    print("✅ Clusters drawn upon the cosmic map.")

    print("Complete data ingestion. All celestial records updated.")

    
if __name__ == "__main__":
    ingest_all_data([], [], [], [], {})
    print("Ingestion script executed with empty data for testing.")
    