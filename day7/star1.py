from day7.models.instructions import Instructions
from utils import load_input

steps = load_input()

instructions = Instructions(steps)
print(instructions.get_step_order())
