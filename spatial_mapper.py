from supabase_setup import supabase
import random

def generate_coordinates():
    return {
        "x": random.uniform(-100, 100),
        "y": random.uniform(-100, 100),
        "z": random.uniform(-100, 100),
    }

def map_track_to_planet(track_id, planet_id):
    # Check if track already mapped
    existing = supabase.table("track_to_planet").select("*").eq("track_id", track_id).execute()
    if existing.data:
        return existing.data[0]
    
    coords = generate_coordinates()
    data = {
        "track_id": track_id,
        "planet_id": planet_id,
        "x_coordinate": coords["x"],
        "y_coordinate": coords["y"],
        "z_coordinate": coords["z"],
    }
    supabase.table("track_to_planet").insert(data).execute()
    return data

def map_album_to_star(album_id, star_id):
    existing = supabase.table("album_to_star").select("*").eq("album_id", album_id).execute()
    if existing.data:
        return existing.data[0]

    coords = generate_coordinates()
    data = {
        "album_id": album_id,
        "star_id": star_id,
        "x_coordinate": coords["x"],
        "y_coordinate": coords["y"],
        "z_coordinate": coords["z"],
    }
    supabase.table("album_to_star").insert(data).execute()
    return data

def map_artist_to_galaxy(artist_id, galaxy_id):
    existing = supabase.table("artist_to_galaxies").select("*").eq("artist_id", artist_id).execute()
    if existing.data:
        return existing.data[0]

    coords = generate_coordinates()
    data = {
        "artist_id": artist_id,
        "galaxy_id": galaxy_id,
        "x_coordinate": coords["x"],
        "y_coordinate": coords["y"],
        "z_coordinate": coords["z"],
    }
    supabase.table("artist_to_galaxies").insert(data).execute()
    return data

