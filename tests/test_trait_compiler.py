
import unittest
from trait_compiler import TraitCompiler

class TestTraitCompiler(unittest.TestCase):
    def setUp(self):
        self.compiler = TraitCompiler()

    def test_compile_loyalty(self):
        trait_data = {
            "name": "loyalty",
            "triggers": ["trust", "bond", "shared_experience"],
            "output_mode": "Protective",
            "resonance_score": 0.89
        }
        compiled = self.compiler.compile(trait_data)
        self.assertIn("trait_hash", compiled)
        self.assertEqual(compiled["name"], "loyalty")
        self.assertEqual(compiled["output_mode"], "Protective")

    def test_compile_invalid_trait(self):
        with self.assertRaises(ValueError):
            self.compiler.compile({})

if __name__ == '__main__':
    unittest.main()
