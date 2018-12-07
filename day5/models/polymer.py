import string


class Polymer:
    def __init__(self, polymer_string, silent=False):
        self.stable = None
        self.raw = polymer_string
        self.reactions = 0
        self.length = len(self.raw)
        self.silent = silent

    def react(self):
        """
        Loop through the polymer and trigger reactions
        until the polymer is no longer reactive.
        """

        reactive = True
        polymer = self.raw
        cycles = 0

        while reactive:
            # Remove all reactive pairs
            reactions = 0
            for lower, upper in zip(string.ascii_lowercase, string.ascii_uppercase):
                units_before_reaction = len(polymer)
                polymer = polymer.replace(lower + upper, "")
                polymer = polymer.replace(upper + lower, "")
                reactions += (units_before_reaction - len(polymer)) // 2

            # Check if the polymer is stable.
            if reactions == 0:
                if not self.silent:
                    print(f"Reaction cycle #{cycles} caused {reactions} reactions. The polymer appears to be stable.")
                reactive = False

            # If it isn't stable, keep going.
            else:
                if not self.silent:
                    print(f"Reaction cycle #{cycles} caused {reactions} reactions.")
                self.reactions += reactions
                cycles += 1

        self.stable = polymer
        self.length = len(polymer)
