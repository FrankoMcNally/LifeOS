# simulation_runner.py

from src.kernel.consciousness_map import ConsciousnessMap
from src.kernel.instinct_matrix import InstinctMatrix
from src.kernel.resonance_math import ResonanceMath
import src.kernel.freewill_resolver as freewill_resolver  # ✅ Import the module

# Create instances
consciousness = ConsciousnessMap()
instinct = InstinctMatrix()
resonance = ResonanceMath()

# Sample data
trait_intensity = 0.75
instinct_level = 0.4

# Call function using module name
is_free = freewill_resolver.is_free_will_decision(trait_intensity, instinct_level)

print(f"Is the decision based on free will? {'Yes' if is_free else 'No'}")
