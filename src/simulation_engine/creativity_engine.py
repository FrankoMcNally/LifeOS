
import random
import json

CREATIVE_DOMAINS = [
    "invention",
    "symbol",
    "melody",
    "philosophy",
    "tool",
    "healing technique",
    "mathematical pattern"
]

def generate_creative_output(entity):
    if not hasattr(entity, "traits") or not hasattr(entity, "harmony_score"):
        return None

    traits = entity.traits
    required_traits = ["curiosity", "love", "focus"]

    if not all(trait in traits for trait in required_traits):
        return None

    if entity.harmony_score < 0.75:
        return None  # Creativity only emerges at high harmony

    domain = random.choice(CREATIVE_DOMAINS)
    title = f"{entity.name}'s {domain.capitalize()} #{random.randint(1000,9999)}"

    creative_entry = {
        "entity": entity.name,
        "domain": domain,
        "title": title,
        "harmony_score": round(entity.harmony_score, 2)
    }

    return creative_entry

def log_creative_event(event, log_path):
    try:
        with open(log_path, "a") as f:
            f.write(json.dumps(event) + "\n")
    except Exception as e:
        print(f"Failed to log creative event: {e}")
