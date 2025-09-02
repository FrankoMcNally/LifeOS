
import random
import copy

def inherit_traits(parent1, parent2, mutation_rate=0.2, available_traits=None):
    inherited = {}
    parent1_traits = parent1.traits
    parent2_traits = parent2.traits

    # Inherit half traits from each parent
    all_keys = list(set(parent1_traits.keys()) | set(parent2_traits.keys()))
    for key in all_keys:
        source = parent1_traits if random.random() < 0.5 else parent2_traits
        if key in source:
            inherited[key] = copy.deepcopy(source[key])

    # Apply mutation
    if available_traits:
        inherited = mutate_traits(inherited, available_traits, mutation_rate)

    return inherited

def mutate_traits(traits, available_traits, mutation_rate=0.2):
    for key in list(traits.keys()):
        if random.random() < mutation_rate:
            mutation_type = random.choice(["boost", "weaken", "replace"])
            if mutation_type == "boost":
                traits[key]["intensity"] = min(1.0, traits[key].get("intensity", 0.5) + 0.1)
            elif mutation_type == "weaken":
                traits[key]["intensity"] = max(0.0, traits[key].get("intensity", 0.5) - 0.1)
            elif mutation_type == "replace" and available_traits:
                replacement = random.choice(list(available_traits.values()))
                traits[replacement["name"]] = copy.deepcopy(replacement)
                del traits[key]
    return traits

def unlock_hidden_traits(entity, available_traits):
    if entity.harmony_score > 0.8:
        hidden = [t for t in available_traits.values() if t.get("hidden", False)]
        if hidden:
            new_trait = random.choice(hidden)
            if new_trait["name"] not in entity.traits:
                entity.traits[new_trait["name"]] = copy.deepcopy(new_trait)
                return new_trait["name"]
    return None

def evolve_generation(parents, available_traits, mutation_rate=0.2):
    next_gen = []
    for i in range(0, len(parents), 2):
        if i + 1 >= len(parents):
            break
        p1 = parents[i]
        p2 = parents[i + 1]
        child_traits = inherit_traits(p1, p2, mutation_rate, available_traits)
        child = type(p1)(name=f"Gen2_{i//2+1}", traits=child_traits)
        next_gen.append(child)
    return next_gen
