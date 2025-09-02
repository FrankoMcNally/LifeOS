import unittest
from LifeOS.src.kernel.resonance_math import prime_resonance

class TestResonanceMath(unittest.TestCase):
    def test_basic_resonance(self):
        result = prime_resonance(0.5, 0.5, 1)
        self.assertAlmostEqual(result, 0.5, places=2)

    def test_high_synergy(self):
        result = prime_resonance(0.7, 0.7, 0.1, n=3)
        self.assertTrue(result > 5)

    def test_zero_stimuli(self):
        result = prime_resonance(0.4, 0.4, 0)
        self.assertGreater(result, 0)

    def test_error_handling(self):
        result = prime_resonance("a", 0.5, 1)
        self.assertEqual(result, 0.0)

if __name__ == "__main__":
    unittest.main()