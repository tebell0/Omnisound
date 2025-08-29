import random

def generate_coordinate(range_min=-1000, range_max=1000):
    """Generate a random float coordinate within the given range."""
    return random.uniform(range_min, range_max)

def generate_coordinates_3d(range_min=-1000, range_max=1000):
    """Generate a tuple of (x, y, z) coordinates."""
    return {
        "x": generate_coordinate(range_min, range_max),
        "y": generate_coordinate(range_min, range_max),
        "z": generate_coordinate(range_min, range_max)
    }

if __name__ == "__main__":
    coords = generate_coordinates_3d()
    print(f"Generated coordinates: {coords}")