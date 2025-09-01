from supabase import create_client, Client
import numpy as np
import uuid

from dotenv import load_dotenv
import os

load_dotenv()

supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_SERVICE_KEY") 
supabase: Client = create_client(supabase_url, supabase_key)

def generate_random_coords(center=(0, 0, 0), spread=50):
    return np.random.normal(center, spread, size=3).tolist()

def generate_entity_coords(user_id, entity_table, entity_id_field, coord_table, coord_entity_field):
    # Fetch entities in user universe
    entity_resp = supabase.table(entity_table) \
        .select(entity_id_field) \
        .eq("user_id", user_id) \
        .execute()
    entity_ids = [row[entity_id_field] for row in entity_resp.data]

    updates = []
    for entity_id in entity_ids:
        # Check if coordinates already exist for this user and entity
        existing = supabase.table(coord_table) \
            .select("id") \
            .eq("user_id", user_id) \
            .eq(coord_entity_field, entity_id) \
            .execute()
        if existing.data:
            continue  # Skip if already exists

        coords = generate_random_coords()
        updates.append({
            "id": str(uuid.uuid4()),
            "user_id": user_id,
            coord_entity_field: entity_id,
            "x": coords[0],
            "y": coords[1],
            "z": coords[2]
        })

    # Insert user-entity coordinates into coord_table
    for batch_start in range(0, len(updates), 500):
        batch = updates[batch_start:batch_start + 500]
        supabase.table(coord_table).insert(batch).execute()

def generate_user_universe(user_id):
    print(f"Generating universe for user {user_id}...")

    # Tracks
    generate_entity_coords(
        user_id,
        entity_table="user_tracks",
        entity_id_field="track_id",
        coord_table="user_coordinates",
        coord_entity_field="track_id"
    )
    # Planets
    generate_entity_coords(
        user_id,
        entity_table="user_planets",
        entity_id_field="planet_id",
        coord_table="user_planet_coordinates",
        coord_entity_field="planet_id"
    )
    # Stars
    generate_entity_coords(
        user_id,
        entity_table="user_stars",
        entity_id_field="star_id",
        coord_table="user_star_coordinates",
        coord_entity_field="star_id"
    )
    # Solar Systems
    generate_entity_coords(
        user_id,
        entity_table="user_solar_systems",
        entity_id_field="solar_system_id",
        coord_table="user_solar_system_coordinates",
        coord_entity_field="solar_system_id"
    )
    # Galaxies
    generate_entity_coords(
        user_id,
        entity_table="user_galaxies",
        entity_id_field="galaxy_id",
        coord_table="user_galaxy_coordinates",
        coord_entity_field="galaxy_id"
    )

    print(f"✅ Universe generated for user {user_id}!")

def run_full_universe_generation(user_id):
    print(f"🚀 Starting full universe generation for user {user_id}...")
    try:
        generate_user_universe(user_id)
        print(f"🌌 Universe generation complete for user {user_id}!")
    except Exception as e:
        print(f"❌ Error during universe generation for user {user_id}: {e}")

# Example usage
if __name__ == "__main__":
    test_user_id = "your-user-id-here"
    run_full_universe_generation(test_user_id)