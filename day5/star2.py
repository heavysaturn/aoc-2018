import string

from day5.models.polymer import Polymer
from utils import load_input

raw_polymer = load_input()[0]

shortest_polymer = ("?", len(raw_polymer))
for lower, upper in zip(string.ascii_lowercase, string.ascii_uppercase):

    # Remove the current unit from the polymer completely
    split_polymer = raw_polymer.replace(lower, "")
    split_polymer = split_polymer.replace(upper, "")

    # React the split polymer
    polymer = Polymer(split_polymer, silent=True)
    polymer.react()

    # Check the result
    if polymer.length < shortest_polymer[1]:
        shortest_polymer = (lower + upper, polymer.length)
        print(f"Polymer improved! Polymer with {lower + upper} units removed is stable at length {polymer.length}")

print(
    f"Shortest polymer found. Polymer with {shortest_polymer[0]} units "
    f"removed is stable at length {shortest_polymer[1]}"
)
