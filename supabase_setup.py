from supabase import create_client, Client

# Replace these with your actual values
SUPABASE_URL = "https://uahfkvjfanzqvhieguzc.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVhaGZrdmpmYW56cXZoaWVndXpjIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0Nzg4NzMxMSwiZXhwIjoyMDYzNDYzMzExfQ.7wvKKKTTwqxdFdllTq_l6fb7dR-VBAgLow5ZDaRUlTc"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Track Logic
def insert_track(data: dict):
    return supabase.table("tracks").insert(data).execute()

def get_track_by_id(track_id: str):
    return supabase.table("tracks").select("*").eq("id", track_id).single().execute()

# Artist Logic
def insert_artist(data: dict):
    return supabase.table("artists").insert(data).execute()

def get_artist_by_id(artist_id: str):
    return supabase.table("artists").select("*").eq("id", artist_id).single().execute()

# Album Logic
def insert_album(data: dict):
    return supabase.table("albums").insert(data).execute()

def get_album_by_id(album_id: str):
    return supabase.table("albums").select("*").eq("id", album_id).single().execute()

# Track Features Logic
def insert_track_features(data: dict):
    return supabase.table("track_features").insert(data).execute()

def get_features_by_track(track_id: str):
    return supabase.table("track_features").select("*").eq("id", track_id).single().execute()

# Track-Artist Map Logic
def link_track_to_artist(track_id: str, artist_id: str):
    return supabase.table("track_to_artist_map").insert({"track_id": track_id, "artist_id": artist_id}).execute()

# Featured Aritsts Logic
def insert_featured_artist(artist_id: str, song_id: str):
    return supabase.table("featured_artists").insert({
        "artist_id": artist_id,
        "song_id": song_id
    }).execute()

# Playlist Logic
def insert_playlist(data: dict):
    return supabase.table("playlists").insert(data).execute()

# Playlist Track Logic
def add_song_to_playlist(playlist_id: str, song_id: str, position: int):
    return supabase.table("playlist_tracks").insert({
        "playlist_id": playlist_id,
        "song_id": song_id,
        "song_position": position
    }).execute()

# Essential Functions
def insert_row(table: str, data: dict):
    return supabase.table(table).insert(data).execute()

def update_row_by_id(table: str, row_id: str, data: dict):
    return supabase.table(table).update(data).eq("id", row_id).execute()

def delete_row_by_id(table: str, row_id: str):
    return supabase.table(table).delete().eq("id", row_id).execute()

def get_row_by_id(table: str, row_id: str):
    return supabase.table(table).select("*").eq("id", row_id).single().execute()

def get_all_rows(table: str, limit=100):
    return supabase.table(table).select("*").limit(limit).execute()

# User Universe Creation Logic
def create_universe(user_id: str, name: str):
    return insert_row("universes", {"user_id": user_id, "name": name})

def get_user_universes(user_id: str):
    return supabase.table("universes").select("*").eq("user_id", user_id).execute()

# Galaxy Logic

def create_galaxy(universe_id: str, name: str, description=""):
    return insert_row("galaxies", {
        "universe_id": universe_id,
        "name": name,
        "description": description
    })

def get_galaxies_in_universe(universe_id: str):
    return supabase.table("galaxies").select("*").eq("universe_id", universe_id).execute()

# Solar System Logic
def create_solar_system(galaxy_id: str, name: str, audio_signature=None):
    return insert_row("solar_systems", {
        "galaxy_id": galaxy_id,
        "name": name,
        "audio_signature": audio_signature
    })

def get_solar_systems_in_galaxy(galaxy_id: str):
    return supabase.table("solar_systems").select("*").eq("galaxy_id", galaxy_id).execute()

# Star Logic
def insert_star(supabase, name, type_, solar_system_id, x=None, y=None, z=None):
    data = {
        "name": name,
        "type": type_,
        "solar_system_id": solar_system_id,
        "x_coordinate": x,
        "y_coordinate": y,
        "z_coordinate": z
    }

    response = supabase.table("stars").insert(data).execute()
    return response
    if response.status_code != 201:
        raise Exception(f"Failed to insert star: {response.error_message}")

# Planet Logic
def create_planet(solar_system_id: str, name: str):
    return insert_row("planets", {
        "solar_system_id": solar_system_id,
        "name": name
    })

def get_planets_in_solar_system(solar_system_id: str):
    return supabase.table("planets").select("*").eq("solar_system_id", solar_system_id).execute()

# Track to Planet Mapping Logic
def map_track_to_planet(supabase, track_id, planet_id):
    data = {
        "track_id": track_id,
        "planet_id": planet_id
    }

    response = supabase.table("track_to_planet_map").insert(data).execute()
    return response

# Album To Star Mapping Logic
def map_album_to_star(supabase, album_id, star_id):
    data = {
        "album_id": album_id,
        "star_id": star_id
    }

    response = supabase.table("album_to_star_map").insert(data).execute()
    return response

# Aritst to Galaxy Mapping Logic
def map_artist_to_galaxy(supabase, artist_id, galaxy_id):
    data = {
        "artist_id": artist_id,
        "galaxy_id": galaxy_id
    }

    response = supabase.table("artist_to_galaxy_map").insert(data).execute()
    return response



def test_supabase_connection():
    response = supabase.table("users").select("*").limit(1).execute()
    print("Supabase connection test response:", response)

if __name__ == "__main__":
    test_supabase_connection()