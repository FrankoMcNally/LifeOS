from src.kernel.trait_compiler import Trait
from src.kernel.consciousness_map import ConsciousnessMap
from src.kernel.instinct_matrix import InstinctMatrix
from src.kernel.resonance_math import ResonanceMath
from src.kernel.free_will_resolver import FreeWillResolver
from src.kernel.fault_pain_detector import FaultPainDetector
from src.kernel.symbolic_language_engine import SymbolicLanguageEngine

def run_simulation():
    print("\n🚀 Simulation step running...")

    # Example: Load a trait manually for now
    example_trait_data = {
        "name": "Resilience",
        "base_intensity": 0.8,
        "triggers": ["stress", "failure"],
        "modulation_factors": {"optimism": 1.2}
    }

    trait = Trait.from_json(example_trait_data)
    compiled_trait = trait.compile()

    # Instantiate core modules
    instinct_matrix = InstinctMatrix()
    consciousness_map = ConsciousnessMap()
    resonance_math = ResonanceMath()
    free_will_resolver = FreeWillResolver()
    fault_pain_detector = FaultPainDetector()
    symbolic_language_engine = SymbolicLanguageEngine()

    # Minimal interaction (stubbed)
    state = {
        "trait": compiled_trait,
        "consciousness": consciousness_map.map_state(compiled_trait),
        "instinct": instinct_matrix.evaluate(compiled_trait),
        "resonance": resonance_math.calculate(compiled_trait),
        "choice": free_will_resolver.resolve(compiled_trait),
        "fault": fault_pain_detector.detect(compiled_trait),
        "language": symbolic_language_engine.generate(compiled_trait),
    }

    for k, v in state.items():
        print(f"{k.upper()}: {v}")
