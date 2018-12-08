import timeit

from day7.models.instructions import Instructions
from utils import load_input


def star2():
    steps = load_input()

    instructions = Instructions(steps, workers=5)
    print(instructions.get_step_order())
    print(instructions.seconds_spent)


print(timeit.timeit("star2()", globals=globals(), number=1))
