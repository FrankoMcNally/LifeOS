
from simulation_runner import run_simulation, load_traits, create_initial_population, Environment

print("🚀 Starting LifeOS Test Simulation")

# Setup
traits = load_traits()
population = create_initial_population(traits, num_pairs=2)  # Smaller test set
environment = Environment(difficulty="medium", type="symbolic-test")

# Run
logs, creative_events, pain_events, symbolic_outputs = run_simulation(
    population,
    environment,
    generations=1
)

# Output
print("\n🧠 Symbolic Outputs:")
for s in symbolic_outputs:
    print(f"  {s['entity']} | {s['symbols']} | Signature: {s['signature']}")

print("\n🔥 Pain Events:")
for p in pain_events:
    print(f"  {p['entity']} | Harmony: {p['harmony_score']} | Signals: {p['pain_signals']}")

print("\n🎨 Creative Events:")
for c in creative_events:
    print(f"  {c['entity']} created: {c['idea']} (Type: {c['type']})")

print("\n✅ LifeOS Test Complete.")
