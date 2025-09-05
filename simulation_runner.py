import json
from src.traits.trait_compiler import TraitCompiler
from src.kernel.consciousness_map import ConsciousnessMap
from src.kernel.instinct_matrix import InstinctMatrix
from src.kernel.resonance_math import ResonanceMath
from src.kernel.freewill_resolver import FreeWillResolver
from src.kernel.fault_pain_detector import FaultPainDetector
from src.kernel.symbolic_language_engine import SymbolicLanguageEngine

# Optional/Not yet implemented modules
try:
    from src.simulation_engine.evolution_engine import EvolutionEngine
except ImportError:
    class EvolutionEngine:
        def __init__(self): print("[Stub] EvolutionEngine loaded")
        def step(self): pass

try:
    from src.simulation_engine.creativity_engine import CreativityEngine
except ImportError:
    class CreativityEngine:
        def __init__(self): print("[Stub] CreativityEngine loaded")
        def generate(self): return None


class LifeSimulation:
    def __init__(self, trait_file_path):
        self.trait_file_path = trait_file_path
        self.traits = self.load_traits()
        self.trait_compiler = TraitCompiler()
        self.consciousness_map = ConsciousnessMap()
        self.instinct_matrix = InstinctMatrix()
        self.resonance_math = ResonanceMath()
        self.freewill_resolver = FreeWillResolver()
        self.fault_pain_detector = FaultPainDetector()
        self.symbolic_language_engine = SymbolicLanguageEngine()
        self.evolution_engine = EvolutionEngine()
        self.creativity_engine = CreativityEngine()

    def load_traits(self):
        print(f"🔍 Loading traits from: {self.trait_file_path}")
        with open(self.trait_file_path, 'r') as f:
            return json.load(f)

    def run_step(self, step_num):
        print(f"\n🔄 Step {step_num} Running Simulation Step")
        self.trait_compiler.compile(self.traits)
        self.consciousness_map.update(self.traits)
        self.instinct_matrix.evaluate(self.traits)
        self.resonance_math.calculate(self.traits)
        self.freewill_resolver.resolve(self.traits)
        self.fault_pain_detector.detect(self.traits)
        self.symbolic_language_engine.interpret(self.traits)
        self.evolution_engine.step()
        idea = self.creativity_engine.generate()
        print(f"💡 Creative Output: {idea}")


if __name__ == "__main__":
    trait_file = "community_traits/sample_trait_set.json"
    sim = LifeSimulation(trait_file)
    for step in range(1, 4):
        sim.run_step(step)