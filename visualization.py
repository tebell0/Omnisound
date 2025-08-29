# omnisound/utils/visualization_utils.py

import math
import hashlib

# --- Coordinate & Visual Helpers ---

def normalize_coordinates(x, y, z, scale=1.0):
#    """Normalize and optionally scale coordinates to fit the universe bounds."""
    norm = math.sqrt(x**2 + y**2 + z**2) or 1
    return {
        "x": (x / norm) * scale,
        "y": (y / norm) * scale,
        "z": (z / norm) * scale
    }

def hash_to_color(identifier: str) -> str:
#    """Generate a consistent hex color from a string ID."""
    hash_digest = hashlib.md5(identifier.encode()).hexdigest()
    r = int(hash_digest[0:2], 16)
    g = int(hash_digest[2:4], 16)
    b = int(hash_digest[4:6], 16)
    return f"#{r:02x}{g:02x}{b:02x}"

def get_size_by_type(entity_type: str) -> float:
#    """Assign visual size based on type of entity."""
    sizes = {
        "galaxy": 10.0,
        "star": 6.0,
        "planet": 3.0
    }
    return sizes.get(entity_type, 2.0)

def format_for_threejs(entity_id: str, entity_type: str, coords: dict):
#    """Prepare a celestial object for frontend rendering."""
    return {
        "id": entity_id,
        "type": entity_type,
        "position": coords,
        "color": hash_to_color(entity_id),
        "size": get_size_by_type(entity_type)
    }

if __name__ == "__main__":
    # Example usage
    coords = normalize_coordinates(100, 200, 300, scale=500)
    color = hash_to_color("example-entity-id")
    size = get_size_by_type("star")
    formatted = format_for_threejs("example-entity-id", "star", coords)
    
    print(f"Normalized Coordinates: {coords}")
    print(f"Color: {color}")
    print(f"Size: {size}")
    print(f"Formatted for Three.js: {formatted}")