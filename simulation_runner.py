
import os
import json
import random
from datetime import datetime
from src.simulation_engine.entity import Entity
from src.simulation_engine.environment import Environment

# Load core traits from /traits/core
def load_traits(trait_path="src/traits/core"):
    traits = {}
    for filename in os.listdir(trait_path):
        if filename.endswith(".json"):
            with open(os.path.join(trait_path, filename), "r") as f:
                trait_data = json.load(f)
                traits[trait_data["name"]] = trait_data
    return traits

# Create 12 founding pairs with mixed traits
def create_initial_population(traits, num_pairs=12):
    population = []
    trait_keys = list(traits.keys())
    for i in range(num_pairs * 2):
        selected_traits = random.sample(trait_keys, k=5)
        entity_traits = {key: traits[key] for key in selected_traits}
        entity = Entity(name=f"Entity_{i+1}", traits=entity_traits)
        population.append(entity)
    return population

# Run simulation loop
def run_simulation(population, environment, generations=1):
    log = []
    for generation in range(generations):
        for entity in population:
            outcome = entity.respond_to_environment(environment)
            log.append({
                "entity": entity.name,
                "generation": generation,
                "response": outcome
            })
    return log

# Save simulation logs to /vaults/YYYY-MM-DD_sim_run_001/
def save_logs(logs):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    vault_dir = f"vaults/{timestamp}_sim_run"
    os.makedirs(vault_dir, exist_ok=True)
    with open(os.path.join(vault_dir, "harmony_log.json"), "w") as f:
        json.dump(logs, f, indent=2)

if __name__ == "__main__":
    print("🔁 Starting LifeOS Simulation Runner")
    traits = load_traits()
    population = create_initial_population(traits)
    environment = Environment(difficulty="medium", type="social_test")
    logs = run_simulation(population, environment, generations=1)
    save_logs(logs)
    print(f"✅ Simulation complete. Logs saved.")
