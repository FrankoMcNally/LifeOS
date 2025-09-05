import sys
import os

# 🔧 Add project root to path so we can import community_loader
sys.path.append(os.path.dirname(__file__))

from simulation_runner import run_simulation

# 🔁 Run simulation for 10 steps as a sample
if __name__ == "__main__":
    for timestep in range(10):
        print(f"\n🌀 Running timestep {timestep + 1}")
        run_simulation()