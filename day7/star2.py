from day7.instructions import Instructions
from utils import load_input

#steps = load_input(input_file="test_input.txt")
steps = load_input()

instructions = Instructions(steps, workers=5)
print(instructions.get_step_order())
print(instructions.seconds_spent)
