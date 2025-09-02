
import random
import hashlib

# Core symbolic domains
DOMAINS = {
    "emotion": ["🜃", "🜄", "🜁", "🜂"],  # earth, water, air, fire
    "logic": ["∴", "∵", "⟹", "⇔"],
    "spiritual": ["✶", "𓂀", "☯", "∞"],
    "creative": ["🎼", "⚙", "🧩", "🔭"]
}

# Trait-to-symbol map (can be learned over time)
TRAIT_SYMBOL_MAP = {
    "love": "🜄",
    "fear": "🜂",
    "focus": "⇔",
    "intuition": "𓂀",
    "curiosity": "🔭",
    "instinct": "🜃",
    "anger": "🜁",
    "consciousness": "∞"
}

# Generate a symbolic packet from an entity’s traits
def generate_symbolic_output(entity):
    if not hasattr(entity, "traits") or not isinstance(entity.traits, dict):
        return None

    dominant_traits = sorted(
        entity.traits.items(),
        key=lambda item: item[1].get("intensity", 0),
        reverse=True
    )[:3]

    symbols = []
    for trait_name, trait_data in dominant_traits:
        symbol = TRAIT_SYMBOL_MAP.get(trait_name)
        if symbol:
            symbols.append(symbol)

    if not symbols:
        return None

    # Add a checksum-like hash to ensure unique signature
    combined = "".join(symbols)
    seed = entity.name + combined
    hash_id = hashlib.sha1(seed.encode()).hexdigest()[:6]

    output = {
        "entity": entity.name,
        "symbols": symbols,
        "signature": combined,
        "hash_id": hash_id
    }
    return output

# Optional: render as string for hardware routing or display
def render_symbolic_string(output):
    if not output:
        return ""
    return f"{output['entity']} | {''.join(output['symbols'])} | #{output['hash_id']}"
