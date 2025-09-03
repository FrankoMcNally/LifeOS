import os
import json

def load_community_traits(directory='community_traits'):
    trait_sets = {}
    if not os.path.exists(directory):
        print(f"Directory '{directory}' does not exist.")
        return trait_sets

    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, 'r') as f:
                    data = json.load(f)
                    trait_sets[filename] = data
            except Exception as e:
                print(f"Error loading {filename}: {e}")

    return trait_sets