from day5.polymer import Polymer
from utils import load_input

raw_polymer = load_input()[0]
polymer = Polymer(raw_polymer)

# React the polymer
polymer.react()

# Check the result
print(f"The reactions are complete! It took {polymer.reactions} reactions before the polymer stabilized.")
print(f"The polymer now looks like this:\n{polymer.stable}")
print(f"The number of units remaining is {polymer.length}")
