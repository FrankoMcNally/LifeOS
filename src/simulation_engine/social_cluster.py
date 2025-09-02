from LifeOS.simulation_engine.entity import Entity

class SocialCluster:
    def __init__(self, entities):
        self.entities = entities

    def calculate_group_resonance(self):
        scores = []
        for i, entity_a in enumerate(self.entities):
            for j, entity_b in enumerate(self.entities):
                if i < j:
                    score = entity_a.evaluate_resonance(entity_b)
                    scores.append(score)
        return round(sum(scores) / len(scores), 4) if scores else 0.0