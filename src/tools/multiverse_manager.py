
import os
import json
import random
from datetime import datetime
from src.simulation_engine.entity import Entity
from src.simulation_engine.environment import Environment
from src.simulation_engine.creativity_engine import generate_creative_output
from src.simulation_engine.evolution_engine import mutate_traits
from simulation_runner import load_traits

# Universe config
UNIVERSE_CONFIGS = [
    {
        "name": "Universe_A",
        "mutation_rate": 0.1,
        "environment": {"difficulty": "medium", "type": "social_test"}
    },
    {
        "name": "Universe_B",
        "mutation_rate": 0.3,
        "environment": {"difficulty": "hard", "type": "stress_test"}
    },
    {
        "name": "Universe_C",
        "mutation_rate": 0.0,
        "environment": {"difficulty": "easy", "type": "growth_test"}
    }
]

def create_population(traits, mutation_rate=0.1, num_pairs=12):
    population = []
    trait_keys = list(traits.keys())
    for i in range(num_pairs * 2):
        selected = random.sample(trait_keys, k=5)
        entity_traits = {k: traits[k] for k in selected}
        mutated = mutate_traits(entity_traits.copy(), traits, mutation_rate)
        entity = Entity(name=f"Entity_{i+1}", traits=mutated)
        population.append(entity)
    return population

def run_universe(universe_name, mutation_rate, env_config, traits, generation=1):
    environment = Environment(**env_config)
    population = create_population(traits, mutation_rate)
    log = []
    creative_events = []

    for entity in population:
        result = entity.respond_to_environment(environment)
        log.append({
            "entity": entity.name,
            "generation": generation,
            "response": result
        })
        creative = generate_creative_output(entity)
        if creative:
            creative["generation"] = generation
            creative_events.append(creative)

    return log, creative_events

def save_universe_logs(base_dir, name, logs, creative_events):
    folder = os.path.join(base_dir, name)
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "harmony_log.json"), "w") as f:
        json.dump(logs, f, indent=2)
    if creative_events:
        with open(os.path.join(folder, "creative_events.json"), "w") as f:
            json.dump(creative_events, f, indent=2)

def run_multiverse():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    multiverse_dir = f"vaults/multiverse_{timestamp}"
    os.makedirs(multiverse_dir, exist_ok=True)
    traits = load_traits()

    for config in UNIVERSE_CONFIGS:
        print(f"🌌 Running {config['name']} ...")
        logs, creative_events = run_universe(
            config["name"],
            config["mutation_rate"],
            config["environment"],
            traits
        )
        save_universe_logs(multiverse_dir, config["name"], logs, creative_events)
        print(f"✅ {config['name']} completed and saved.")

if __name__ == "__main__":
    print("🧪 Launching Inter-Multiverse Simulation")
    run_multiverse()
    print("🌌 All universes complete.")
