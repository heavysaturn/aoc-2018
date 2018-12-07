from pprint import pprint


def get_first_step(steps):
    """
    Get the first step from a dict
    of {step: [next_steps]}
    """

    first_step = []
    need_assembly = []
    for step, next_steps in steps.items():

        first_step.append(step)
        need_assembly.extend(next_steps)

        if step in need_assembly:
            first_step.remove(step)

    return sorted(first_step)[0]


def get_next_step(steps, previous_step, list_of_steps):
    """
    Get the next step from a dict
    of {step: [next_steps]}
    using the last step.
    """

    print(f"--- CURRENT STEP: {list_of_steps[-1]} ---")
    pprint(steps)

    # first let's get all potential next steps
    potentials = set()
    for step in list_of_steps:
        if step in steps:
            for item in steps[step]:
                potentials.add(item)

    # We also need any step that has no prereqs
    all_steps_with_prereqs = []
    for next_steps in steps.values():
        all_steps_with_prereqs.append(next_steps)

    steps_without_prereqs = [step for step in steps if step not in all_steps_with_prereqs]
    for step in steps_without_prereqs:
        potentials.add(step)

    # Remove all steps we've already done.
    print(potentials)
    potentials = [p for p in potentials if p not in list_of_steps]
    print(potentials)

    # Remove all steps with unsatisfied prereqs
    unsatisfied = []
    for candidate in potentials:
        prereqs = []

        for step, next_steps in steps.items():
            if candidate in next_steps and step not in list_of_steps:
                prereqs.append(step)

        if prereqs:
            unsatisfied.append(candidate)

    potentials = [p for p in potentials if p not in unsatisfied]

    # If we have a candidate, return that.
    if potentials:
        return sorted(potentials)[0]

    # If there are no candidates, return an unsatisfied prerequisite
    elif not potentials and unsatisfied:
        return sorted(unsatisfied)[0]

    # Otherwise, return the last step.
    else:
        return get_last_step(steps)


def get_next_step_multi(steps, previous_step, list_of_steps):
    """
    Get the next step from a dict
    of {step: [next_steps]}
    using the last step.
    """

    print(f"--- CURRENT STEP: {list_of_steps[-1]} ---")
    pprint(steps)

    # first let's get all potential next steps
    potentials = set()
    for step in list_of_steps:
        if step in steps:
            for item in steps[step]:
                potentials.add(item)

    # We also need any step that has no prereqs
    all_steps_with_prereqs = []
    for next_steps in steps.values():
        all_steps_with_prereqs.append(next_steps)

    steps_without_prereqs = [step for step in steps if step not in all_steps_with_prereqs]
    for step in steps_without_prereqs:
        potentials.add(step)

    # Remove all steps we've already done.
    print(potentials)
    potentials = [p for p in potentials if p not in list_of_steps]
    print(potentials)

    # Remove all steps with unsatisfied prereqs
    unsatisfied = []
    for candidate in potentials:
        prereqs = []

        for step, next_steps in steps.items():
            if candidate in next_steps and step not in list_of_steps:
                prereqs.append(step)

        if prereqs:
            unsatisfied.append(candidate)

    potentials = [p for p in potentials if p not in unsatisfied]

    # If we have a candidate, return that.
    if potentials:
        return get_potential(potentials)

    # If there are no candidates, return an unsatisfied prerequisite
    elif not potentials and unsatisfied:
        return get_unsatisfied(unsatisfied)

    # Otherwise, return the last step.
    else:
        return get_last_step(steps)

def get_potential(potentials):

    # Sort the potentials
    potentials = sorted(potentials)

    #

def get_last_step(steps):
    """
    Get the last step from a dict
    of {step: [next_steps]}
    """

    regular_steps = []
    final_step = []
    for step, next_steps in steps.items():

        regular_steps.append(step)
        final_step.extend(next_steps)

        if step in final_step:
            final_step.remove(step)

    return final_step[0]



