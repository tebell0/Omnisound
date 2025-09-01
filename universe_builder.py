# omnisound/scripts/universe_builder.py

from supabase_setup import supabase
import json

def fetch_universe_data(user_id: str) -> dict:
    """Fetches all celestial data related to a user's musical universe."""
    
    # Fetch all galaxies for the user
    galaxies = supabase.table("galaxies").select("*").eq("user_id", user_id).execute().data

    universe = {"galaxies": []}

    for galaxy in galaxies:
        galaxy_id = galaxy["id"]
        galaxy_obj = {
            "id": galaxy_id,
            "name": galaxy["name"],
            "color": galaxy["color"],
            "coordinates": {
                "x": galaxy["x"],
                "y": galaxy["y"],
                "z": galaxy["z"]
            },
            "artists": []
        }

        # Fetch artists in this galaxy
        artists = supabase.table("artists").select("*").eq("galaxy_id", galaxy_id).execute().data

        for artist in artists:
            artist_id = artist["id"]
            artist_obj = {
                "id": artist_id,
                "name": artist["name"],
                "color": artist["color"],
                "stars": []
            }

            # Fetch stars for artist
            stars = supabase.table("stars").select("*").eq("artist_id", artist_id).execute().data

            for star in stars:
                star_id = star["id"]
                star_obj = {
                    "id": star_id,
                    "name": star["name"],
                    "color": star["color"],
                    "coordinates": {
                        "x": star["x"],
                        "y": star["y"],
                        "z": star["z"]
                    },
                    "albums": []
                }

                # Fetch albums for star
                albums = supabase.table("albums").select("*").eq("star_id", star_id).execute().data

                for album in albums:
                    album_id = album["id"]
                    album_obj = {
                        "id": album_id,
                        "name": album["name"],
                        "color": album["color"],
                        "planets": []
                    }

                    # Fetch planets for album
                    planets = supabase.table("planets").select("*").eq("album_id", album_id).execute().data

                    for planet in planets:
                        planet_id = planet["id"]
                        planet_obj = {
                            "id": planet_id,
                            "name": planet["name"],
                            "color": planet["color"],
                            "coordinates": {
                                "x": planet["x"],
                                "y": planet["y"],
                                "z": planet["z"]
                            },
                            "track": None
                        }

                        # Fetch track associated with this planet
                        tracks = supabase.table("tracks").select("*").eq("planet_id", planet_id).execute().data
                        if tracks:
                            track = tracks[0]
                            planet_obj["track"] = {
                                "id": track["id"],
                                "name": track["name"],
                                "duration": track["duration_ms"],
                                "preview_url": track["preview_url"],
                            }

                        album_obj["planets"].append(planet_obj)

                    star_obj["albums"].append(album_obj)

                artist_obj["stars"].append(star_obj)

            galaxy_obj["artists"].append(artist_obj)

        universe["galaxies"].append(galaxy_obj)

    return universe


def export_universe_json(user_id: str, output_path: str = "universe.json"):
    """Writes universe data to a JSON file for frontend rendering."""
    data = fetch_universe_data(user_id)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Universe for user {user_id} exported to {output_path}")


if __name__ == "__main__":
    test_user_id = "your-user-id-here"
    export_universe_json(test_user_id)