from LifeOS.src.traits.trait_compiler import Trait
from LifeOS.kernel.instinct_matrix import is_instinct_triggered
from LifeOS.kernel.resonance_math import prime_resonance

class Entity:
    def __init__(self, name, traits):
        self.name = name
        self.traits = traits  # Dictionary of trait name to Trait object
        self.instinct_mode = False

    def receive_environment_input(self, environment_factors):
        for trait in self.traits.values():
            trait.process_environment(environment_factors)

    def check_instinct_trigger(self):
        self.instinct_mode = is_instinct_triggered(self.traits)

    def evaluate_resonance(self, other_entity):
        dominant_self = max(self.traits.values(), key=lambda t: t.current_intensity)
        dominant_other = max(other_entity.traits.values(), key=lambda t: t.current_intensity)
        return prime_resonance(dominant_self.current_intensity, dominant_other.current_intensity, time_stimuli=1)