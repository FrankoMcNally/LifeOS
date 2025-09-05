
class TraitCompiler:
    def __init__(self):
        self.traits = {}

    def compile(self, trait_data):
        """
        Compiles raw trait data into a usable format.
        """
        compiled = {}
        for name, details in trait_data.items():
            compiled[name] = {
                "intensity": details.get("intensity", 1.0),
                "category": details.get("category", "core"),
                "description": details.get("description", "")
            }
        self.traits = compiled
        return compiled

    def get_trait(self, name):
        """
        Returns a specific trait's compiled data.
        """
        return self.traits.get(name, None)

    def list_traits(self):
        """
        Returns a list of all compiled traits.
        """
        return list(self.traits.keys())
