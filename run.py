
# run.py — Universal Simulation Launcher for LifeOS

from community_loader import load_traits_from_file
from simulation_runner import SimulationRunner

TRAIT_FILE = "community_traits/sample_trait_set.json"
SIMULATION_STEPS = 10

def main():
    print("🧠 Booting LifeOS simulation...")
    traits = load_traits_from_file(TRAIT_FILE)
    runner = SimulationRunner(traits)

    for step in range(SIMULATION_STEPS):
        print(f"🌱 Simulation step {step + 1}")
        runner.run_step()

    print("✅ Simulation completed.")

if __name__ == "__main__":
    main()
