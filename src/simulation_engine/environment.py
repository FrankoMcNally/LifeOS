class Environment:
    def __init__(self, temperature=20.0, social_stress=0.0, noise_level=0.0):
        self.temperature = temperature
        self.social_stress = social_stress
        self.noise_level = noise_level

    def get_factors(self):
        return {
            "temperature": self.temperature,
            "social_stress": self.social_stress,
            "noise_level": self.noise_level
        }