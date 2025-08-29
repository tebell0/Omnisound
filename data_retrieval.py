from supabase import create_client, Client
from dotenv import load_dotenv
import os
import uuid

load_dotenv()

# Create Supabase client
url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

# --------------------- Galaxies ---------------------

def is_valid_uuid(val):
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False

def get_all_galaxies():
    return supabase.table("galaxies").select("*").execute().data

def get_galaxy_by_id(galaxy_id):
    if not is_valid_uuid(galaxy_id):
        raise ValueError("Invalid UUID format for galaxy_id")
    return supabase.table("galaxies").select("*").eq("id", galaxy_id).single().execute().data

# --------------------- Stars ---------------------
def get_stars_by_solar_system(solar_system_id):
    return supabase.table("stars").select("*").eq("solar_system_id", solar_system_id).execute().data

def get_star_by_id(star_id):
    if not is_valid_uuid(star_id):
        raise ValueError("Invalid UUID format for star_id")
    return supabase.table("stars").select("*").eq("id", star_id).single().execute().data

# --------------------- Solar Systems ---------------------

def get_solar_systems_by_star(star_id):
    return supabase.table("solar_systems").select("*").eq("star_id", star_id).execute().data

# --------------------- Planets ---------------------

def get_planets_by_solar_system(system_id):
    return supabase.table("planets").select("*").eq("solar_system_id", system_id).execute().data

def get_planet_by_id(planet_id):
    if not is_valid_uuid(planet_id):
        raise ValueError("Invalid UUID format for planet_id")
    return supabase.table("planets").select("*").eq("id", planet_id).single().execute().data

# --------------------- Tracks ---------------------

def get_tracks_by_planet(planet_id):
    return supabase.table("tracks").select("*").eq("planet_id", planet_id).execute().data

def get_track_by_id(track_id):
    if not is_valid_uuid(track_id):
        raise ValueError("Invalid UUID format for track_id")
    return supabase.table("tracks").select("*").eq("id", track_id).single().execute().data

# --------------------- Users & Sessions ---------------------

def get_user_by_id(user_id):
    if not is_valid_uuid(user_id):
        raise ValueError("Invalid UUID format for user_id")
    return supabase.table("users").select("*").eq("id", user_id).single().execute().data

def get_sessions_by_user(user_id):
    return supabase.table("user_track_session_data").select("*").eq("user_id", user_id).execute().data

def get_all_entities():
    return {
        "galaxies": supabase.table("galaxies").select("*").execute().data,
        "stars": supabase.table("stars").select("*").execute().data,
        "solar_systems": supabase.table("solar_systems").select("*").execute().data,
        "planets": supabase.table("planets").select("*").execute().data,
        "tracks": supabase.table("tracks").select("*").execute().data,
        "users": supabase.table("users").select("*").execute().data,
        "sessions": supabase.table("user_track_session_data").select("*").execute().data
    }


if __name__ == "__main__":
    print("Testing data retrieval functions...")

    # Get first galaxy, star, solar system, planet, user, etc.
    galaxies = get_all_galaxies()
    galaxy_id = galaxies[0]["id"] if galaxies else None

    stars = supabase.table("stars").select("*").execute().data
    star_id = stars[0]["id"] if stars else None

    solar_systems = supabase.table("solar_systems").select("*").execute().data
    solar_system_id = solar_systems[0]["id"] if solar_systems else None

    planets = supabase.table("planets").select("*").execute().data
    planet_id = planets[0]["id"] if planets else None

    users = supabase.table("users").select("*").execute().data
    user_id = users[0]["id"] if users else None

    print("Galaxies:", galaxies)
    print("Stars in first solar system:", get_stars_by_solar_system(solar_system_id) if solar_system_id else "No solar systems found")
    print("Solar Systems in first star:", get_solar_systems_by_star(star_id) if star_id else "No stars found")
    print("Planets in first solar system:", get_planets_by_solar_system(solar_system_id) if solar_system_id else "No solar systems found")
    print("Tracks on first planet:", get_tracks_by_planet(planet_id) if planet_id else "No planets found")
    print("First User Data:", get_user_by_id(user_id) if user_id else "No users found")
    print("Sessions for first user:", get_sessions_by_user(user_id) if user_id else "No users found")
    print("All Entities:", get_all_entities())