import unittest
from LifeOS.simulation_engine.entity import Entity
from LifeOS.src.kernel.trait_compiler import Trait

class TestEntityLifecycle(unittest.TestCase):
    def test_entity_simulation(self):
        trait1 = Trait(name="Curiosity", base_intensity=0.7, triggers=["novelty"], modulation_factors={"stress": -0.5})
        trait2 = Trait(name="Loyalty", base_intensity=0.9, triggers=["ingroup_threat"], modulation_factors={"stress": 1.2})
        entity = Entity(name="Unit_Test_Subject", traits={"Curiosity": trait1, "Loyalty": trait2})

        environment = {"social_stress": 0.8, "temperature": 22.0, "noise_level": 0.3}
        entity.receive_environment_input(environment)
        entity.check_instinct_trigger()

        compiled = trait1.compile(environment_stress=environment['social_stress'])
        self.assertIn("current_intensity", compiled)
        self.assertIsInstance(compiled["current_intensity"], float)

if __name__ == "__main__":
    unittest.main()