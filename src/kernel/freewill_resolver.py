def is_free_will_decision(trait_intensity, instinct_level, threshold=0.2):
    """
    Determine if action is driven by free will or instinct.
    If trait_intensity differs significantly from instinct, it's likely free will.
    """
    delta = abs(trait_intensity - instinct_level)
    return delta > threshold

__all__ = ['is_free_will_decision']