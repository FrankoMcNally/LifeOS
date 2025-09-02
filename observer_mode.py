
import os
import json

# Define base vault path
VAULT_PATH = "vaults"

def list_simulations():
    return [folder for folder in os.listdir(VAULT_PATH) if os.path.isdir(os.path.join(VAULT_PATH, folder))]

def load_log(sim_folder):
    path = os.path.join(VAULT_PATH, sim_folder, "harmony_log.json")
    if not os.path.exists(path):
        print(f"❌ Log not found: {path}")
        return []
    with open(path, "r") as f:
        return json.load(f)

def query_entity(logs, entity_name):
    return [entry for entry in logs if entry["entity"] == entity_name]

def get_unique_entities(logs):
    return list({entry["entity"] for entry in logs})

def summary_report(logs):
    summary = {}
    for entry in logs:
        entity = entry["entity"]
        if entity not in summary:
            summary[entity] = 0
        summary[entity] += 1
    return summary

if __name__ == "__main__":
    print("🔍 Observer Mode Activated")
    simulations = list_simulations()
    if not simulations:
        print("⚠️ No simulation logs found.")
        exit()

    print("Available Simulations:")
    for i, sim in enumerate(simulations):
        print(f"[{i}] {sim}")

    selected = input("Select simulation index: ")
    try:
        sim_folder = simulations[int(selected)]
    except:
        print("❌ Invalid selection.")
        exit()

    logs = load_log(sim_folder)
    if not logs:
        exit()

    print(f"Simulation '{sim_folder}' loaded. Entities recorded:")
    entities = get_unique_entities(logs)
    for e in entities:
        print(f" - {e}")

    name = input("Enter entity name for full log or press Enter for summary: ").strip()
    if name:
        results = query_entity(logs, name)
        for r in results:
            print(json.dumps(r, indent=2))
    else:
        summary = summary_report(logs)
        for entity, count in summary.items():
            print(f"{entity}: {count} events")
