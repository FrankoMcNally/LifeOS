
class FaultPainDetector:
    def __init__(self):
        self.pain_keywords = ["failure", "loss", "rejection", "guilt", "fear"]

    def detect(self, trait_data):
        triggers = trait_data.get("triggers", [])
        base_intensity = trait_data.get("base_intensity", 0)
        pain_score = 0

        for trigger in triggers:
            if trigger.lower() in self.pain_keywords:
                pain_score += 1

        # Normalize and apply intensity
        normalized_pain = min(pain_score / len(self.pain_keywords), 1.0)
        return round(normalized_pain * base_intensity, 3)
