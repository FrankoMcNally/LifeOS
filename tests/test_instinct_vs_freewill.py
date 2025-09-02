import unittest
from LifeOS.src.kernel.instinct_matrix import instinct_triggered
from LifeOS.src.kernel.freewill_resolver import resolve_free_will

class TestInstinctVsFreeWill(unittest.TestCase):
    def test_instinct_triggered(self):
        result = instinct_triggered({'Fear': 0.95, 'Courage': 0.3})
        self.assertTrue(result)

    def test_free_will_resolves_false(self):
        result = resolve_free_will({'Fear': 0.95, 'Courage': 0.2})
        self.assertFalse(result)

    def test_free_will_resolves_true(self):
        result = resolve_free_will({'Curiosity': 0.8, 'Courage': 0.6})
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()