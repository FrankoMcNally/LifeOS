
# example_1_high_stress_scenario.py

from LifeOS.src.kernel.trait_compiler import Trait
from LifeOS.simulation_engine.environment import Environment
from LifeOS.simulation_engine.entity import Entity

# 1. Initialize the environment with high-stress factors
env = Environment(temperature=15.0, social_stress=0.9, noise_level=0.8)
environment_factors = env.get_factors()
print(f"Environment Factors: {environment_factors}\n")

# 2. Create trait objects manually (from the core trait structure)
loyalty_trait = Trait(
    name="Loyalty",
    base_intensity=0.8,
    triggers=["betrayal_observed", "ingroup_threat"],
    modulation_factors={'stress': 1.5}
)

courage_trait = Trait(
    name="Courage",
    base_intensity=0.7,
    triggers=["fear_triggered", "moral_duty"],
    modulation_factors={'stress': 0.8}
)

# 3. Create an entity and assign traits
subject_alpha = Entity(
    name="Subject_Alpha",
    traits={"Loyalty": loyalty_trait, "Courage": courage_trait}
)

# 4. Simulate the entity receiving the environment
subject_alpha.receive_environment_input(environment_factors)

# 5. Check for instinct override based on stress
subject_alpha.check_instinct_trigger()
print(f"Instinct Mode Activated: {subject_alpha.instinct_mode}\n")

# 6. Compile traits to observe behavior under stress
print("Compiled Trait Output under High Stress:")
for trait_name, trait_obj in subject_alpha.traits.items():
    compiled_data = trait_obj.compile(environment_stress=env.social_stress)
    print(f"  - {trait_name}:")
    print(f"        Current Intensity: {compiled_data['current_intensity']}")
    print(f"        Triggers: {compiled_data['triggers']}")
