import unittest
from LifeOS.simulation_engine.environment import Environment

class TestEnvironmentInput(unittest.TestCase):
    def test_environment_factors(self):
        env = Environment(temperature=20.0, social_stress=0.7, noise_level=0.5)
        factors = env.get_factors()
        self.assertEqual(factors['temperature'], 20.0)
        self.assertEqual(factors['social_stress'], 0.7)
        self.assertEqual(factors['noise_level'], 0.5)

if __name__ == "__main__":
    unittest.main()