
import os
import json

VAULT_ROOT = "vaults"

def find_multiverse_runs():
    return sorted([
        f for f in os.listdir(VAULT_ROOT)
        if f.startswith("multiverse_")
    ], reverse=True)

def load_log(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except:
        return []

def summarize_universe(universe_path):
    harmony_log_path = os.path.join(universe_path, "harmony_log.json")
    creative_log_path = os.path.join(universe_path, "creative_events.json")

    harmony_log = load_log(harmony_log_path)
    creative_log = load_log(creative_log_path)

    total_events = len(harmony_log)
    unique_entities = set(e["entity"] for e in harmony_log)
    creative_count = len(creative_log)

    return {
        "entities": len(unique_entities),
        "events": total_events,
        "creative_events": creative_count
    }

def compare_multiverse_runs():
    multiverses = find_multiverse_runs()
    if not multiverses:
        print("⚠️ No multiverse simulations found.")
        return

    latest = multiverses[0]
    multiverse_path = os.path.join(VAULT_ROOT, latest)
    print(f"📊 Comparing Universes in: {latest}\n")

    for universe in sorted(os.listdir(multiverse_path)):
        universe_path = os.path.join(multiverse_path, universe)
        if os.path.isdir(universe_path):
            summary = summarize_universe(universe_path)
            print(f"🌌 {universe}")
            print(f"   Entities:         {summary['entities']}")
            print(f"   Total Events:     {summary['events']}")
            print(f"   Creative Events:  {summary['creative_events']}\n")

if __name__ == "__main__":
    print("🧠 Multiverse Observer Running...")
    compare_multiverse_runs()
    print("✅ Done.")
