import unittest
from entity import DigitalEntity
from resonance_math import calculate_resonance_score

class TestEntityResonance(unittest.TestCase):
    def test_resonance_score_protective(self):
        entity = DigitalEntity("TestSubject")
        entity.traits = {
            "loyalty": {"intensity": 0.9},
            "courage": {"intensity": 0.85}
        }
        score, mode = calculate_resonance_score(entity.traits, "loyalty", "courage", "high_social_stress")
        self.assertGreater(score, 0.8)
        self.assertEqual(mode, "Protective")

    def test_resonance_score_destructive(self):
        entity = DigitalEntity("TestSubject")
        entity.traits = {
            "fear": {"intensity": 0.9},
            "anger": {"intensity": 0.85}
        }
        score, mode = calculate_resonance_score(entity.traits, "fear", "anger", "extreme_threat")
        self.assertLess(score, 0.5)
        self.assertEqual(mode, "Destructive")

    def test_resonance_score_neutral(self):
        entity = DigitalEntity("TestSubject")
        entity.traits = {
            "curiosity": {"intensity": 0.5},
            "resilience": {"intensity": 0.5}
        }
        score, mode = calculate_resonance_score(entity.traits, "curiosity", "resilience", "calm_environment")
        self.assertTrue(0.4 <= score <= 0.7)
        self.assertEqual(mode, "Neutral")

if __name__ == '__main__':
    unittest.main()
