
def detect_pain(entity, harmony_threshold=0.3, overload_threshold=0.9):
    if not hasattr(entity, "traits") or not hasattr(entity, "harmony_score"):
        return None

    pain_signals = []
    overloaded_traits = []

    for trait_name, trait_data in entity.traits.items():
        if trait_data.get("intensity", 0) >= overload_threshold:
            overloaded_traits.append(trait_name)

    if entity.harmony_score < harmony_threshold:
        pain_signals.append("⚠️ Low Harmony")

    if overloaded_traits:
        pain_signals.append(f"🔥 Overloaded: {', '.join(overloaded_traits)}")

    if pain_signals:
        pain_event = {
            "entity": entity.name,
            "harmony_score": round(entity.harmony_score, 2),
            "pain_signals": pain_signals
        }
        return pain_event

    return None
