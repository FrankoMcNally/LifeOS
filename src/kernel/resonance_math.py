def prime_resonance(trait_a, trait_b, time_stimuli, n=2):
    """
    Calculates the Prime Resonance Score (RHS) for two traits.
    Formula: (TraitA + TraitB)^n ÷ (TimeStimuli + 1)
    """
    try:
        denominator = max(time_stimuli, 0.1)
        score = (trait_a + trait_b) ** n / denominator
        return round(score, 4)
    except Exception as e:
        print(f"Error in prime_resonance: {e}")
        return 0.0