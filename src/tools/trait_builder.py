
import json
from pathlib import Path

def main():
    print("Welcome to the Trait Builder Tool!")
    trait_set = {
        "name": input("Enter the name of this trait set: "),
        "description": input("Enter a short description: "),
        "traits": []
    }

    while True:
        print("\n--- Add a New Trait ---")
        trait_name = input("Trait name: ")
        trait_desc = input("Trait description: ")
        trait_value = input("Trait default value (e.g. true, 10, etc.): ")

        # Try to convert numeric values, leave strings as-is
        try:
            trait_value = eval(trait_value)
        except:
            pass

        trait = {
            "name": trait_name,
            "description": trait_desc,
            "default": trait_value
        }

        trait_set["traits"].append(trait)

        cont = input("Add another trait? (y/n): ").strip().lower()
        if cont != 'y':
            break

    output_path = Path(__file__).resolve().parent.parent.parent / "community_traits"
    output_path.mkdir(parents=True, exist_ok=True)
    output_file = output_path / f"{trait_set['name'].replace(' ', '_').lower()}_traits.json"

    with open(output_file, "w") as f:
        json.dump(trait_set, f, indent=4)

    print(f"Trait set saved to {output_file}")

if __name__ == "__main__":
    main()
