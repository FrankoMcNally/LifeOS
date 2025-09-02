import json

class Trait:
    def __init__(self, name, base_intensity, triggers, modulation_factors):
        self.name = name
        self.base_intensity = base_intensity
        self.triggers = triggers
        self.modulation_factors = modulation_factors

    @classmethod
    def from_json(cls, file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
        return cls(
            name=data.get("name"),
            base_intensity=data.get("base_intensity", 1.0),
            triggers=data.get("triggers", []),
            modulation_factors=data.get("modulation_factors", {})
        )

    def compile(self, environment_stress=0.0):
        """Compiles the trait into an executable state for the simulation."""
        stress_factor = self.modulation_factors.get('stress', 1.0)
        current_intensity = self.base_intensity * (1 + environment_stress * stress_factor)

        return {
            "name": self.name,
            "current_intensity": max(0.0, min(1.0, current_intensity)),
            "triggers": self.triggers,
            "prime_resonance_threshold": self.modulation_factors.get("prime_resonance_threshold", 0.5)
        }