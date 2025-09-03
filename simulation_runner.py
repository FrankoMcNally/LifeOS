
import argparse
import json
import os
from src.simulation_engine.evolution_engine import EvolutionEngine
from src.simulation_engine.creativity_engine import CreativityEngine
from src.kernel.consciousness_map import ConsciousnessMap
from src.kernel.trait_compiler import TraitCompiler
from src.kernel.freewill_resolver import FreeWillResolver
from src.kernel.instinct_matrix import InstinctMatrix
from src.kernel.resonance_math import ResonanceMath
from src.kernel.symbolic_language_engine import SymbolicLanguageEngine
from src.kernel.fault_pain_detector import FaultPainDetector
from src.gui_dashboard import run_gui_dashboard

def load_traits(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    raise FileNotFoundError(f"Trait file not found: {file_path}")

def main():
    parser = argparse.ArgumentParser(description="LifeOS Simulation Runner")
    parser.add_argument(
        "--trait_file",
        type=str,
        default="src/data/traits/default_traits.json",
        help="Path to trait file (core or community)"
    )
    args = parser.parse_args()

    trait_data = load_traits(args.trait_file)

    print(f"✅ Loaded traits from: {args.trait_file}")

    trait_compiler = TraitCompiler(trait_data)
    consciousness = ConsciousnessMap(trait_compiler)
    instincts = InstinctMatrix()
    resonance = ResonanceMath()
    freewill = FreeWillResolver()
    pain_detector = FaultPainDetector()
    symbolic_engine = SymbolicLanguageEngine()
    creativity = CreativityEngine(trait_compiler, symbolic_engine)
    evolution = EvolutionEngine(trait_compiler, creativity)

    # Launch GUI dashboard (core observer mode)
    run_gui_dashboard(
        consciousness=consciousness,
        instincts=instincts,
        resonance=resonance,
        freewill=freewill,
        pain_detector=pain_detector,
        symbolic_engine=symbolic_engine,
        creativity_engine=creativity,
        evolution_engine=evolution
    )

if __name__ == "__main__":
    main()
