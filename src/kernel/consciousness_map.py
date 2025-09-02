
# consciousness_map.py

def determine_conscious_response(traits, environment_stress):
    """
    Determines if a conscious override occurs based on traits and environmental pressure.
    Returns level of override and the controlling trait.
    """
    dominant_trait = max(traits, key=lambda t: t['intensity'])
    override_likelihood = dominant_trait['intensity'] * (1 + environment_stress)
    
    if override_likelihood > 1.0:
        return {"override": True, "trait": dominant_trait['name'], "intensity": round(override_likelihood, 2)}
    else:
        return {"override": False, "trait": dominant_trait['name'], "intensity": round(override_likelihood, 2)}
