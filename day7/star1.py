from day7.helpers import get_first_step, get_next_step
from utils import load_input

#steps = load_input(input_file="test_input.txt")
steps = load_input()
steps_to_next = {}

for step in steps:
    # parse the steps
    current = step.split()[1]
    next = step.split()[-3]

    # steps dict
    if current in steps_to_next:
        steps_to_next[current].append(next)
    else:
        steps_to_next[current] = [next]

list_of_steps = [get_first_step(steps_to_next)]

print(steps_to_next)

for _ in steps_to_next:
    previous_step = list_of_steps[-1]
    next_step = get_next_step(steps_to_next, previous_step, list_of_steps)
    list_of_steps.append(next_step)


print(("".join(list_of_steps)))
