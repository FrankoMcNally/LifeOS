
from src.kernel.consciousness_map import ConsciousnessMap
from src.kernel.instinct_matrix import InstinctMatrix
from src.kernel.resonance_math import ResonanceMath
import src.kernel.freewill_resolver as freewill_resolver

def run_simulation():
    # Step 1: Create core instances
    consciousness = ConsciousnessMap()
    instinct = InstinctMatrix()
    resonance = ResonanceMath()

    # Step 2: Simulate sample values
    trait_intensity = 0.75
    instinct_level = 0.4

    # Step 3: Free will decision check
    is_free = freewill_resolver.is_free_will_decision(trait_intensity, instinct_level)

    # Step 4: Print results for this timestep
    print("🧠 Consciousness layers initialized.")
    print("🌀 Instinct level:", instinct_level)
    print("🎯 Trait intensity:", trait_intensity)
    print(f"🔓 Free will activated? {'Yes' if is_free else 'No'}")
