
import os
import json
import random
from datetime import datetime
from src.simulation_engine.entity import Entity
from src.simulation_engine.environment import Environment
from src.simulation_engine.creativity_engine import generate_creative_output
from src.kernel.fault_pain_detector import detect_pain
from src.kernel.symbolic_language_engine import generate_symbolic_output

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
    creative_events = []
    pain_events = []
    symbolic_outputs = []

    for generation in range(generations):
        for entity in population:
            outcome = entity.respond_to_environment(environment)
            log.append({
                "entity": entity.name,
                "generation": generation,
                "response": outcome
            })

            # Creative output
            creative = generate_creative_output(entity)
            if creative:
                creative["generation"] = generation
                creative_events.append(creative)

            # Pain detection
            pain = detect_pain(entity)
            if pain:
                pain["generation"] = generation
                pain_events.append(pain)

            # Symbolic output
            symbol = generate_symbolic_output(entity)
            if symbol:
                symbol["generation"] = generation
                symbolic_outputs.append(symbol)

    return log, creative_events, pain_events, symbolic_outputs

# Save logs to vault
def save_logs(logs, creative_events, pain_events, symbols):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    vault_dir = f"vaults/{timestamp}_sim_run"
    os.makedirs(vault_dir, exist_ok=True)

    with open(os.path.join(vault_dir, "harmony_log.json"), "w") as f:
        json.dump(logs, f, indent=2)

    if creative_events:
        with open(os.path.join(vault_dir, "creative_events.json"), "w") as f:
            json.dump(creative_events, f, indent=2)

    if pain_events:
        with open(os.path.join(vault_dir, "pain_events.json"), "w") as f:
            json.dump(pain_events, f, indent=2)

    if symbols:
        with open(os.path.join(vault_dir, "symbolic_outputs.json"), "w") as f:
            json.dump(symbols, f, indent=2)

if __name__ == "__main__":
    print("🔁 Starting LifeOS Simulation Runner (w/ pain & symbols)")
    traits = load_traits()
    population = create_initial_population(traits)
    environment = Environment(difficulty="medium", type="social_test")
    logs, creative_events, pain_events, symbolic_outputs = run_simulation(population, environment, generations=1)
    save_logs(logs, creative_events, pain_events, symbolic_outputs)
    print(f"✅ Simulation complete. All logs saved.")
