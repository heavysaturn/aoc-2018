from day7.step import Step
from day7.worker import Worker


class Instructions:
    def __init__(self, steps, workers=0):
        self.steps = {}
        self.workers = [Worker(num) for num in range(workers)]
        self.total_steps = len(steps)
        self._parse_steps(steps)
        self.step_order = []
        self.seconds_spent = 0
        self.active_steps = []

    def get_free_workers(self):
        return [worker for worker in self.workers if worker.free]

    def get_busy_workers(self):
        return [worker for worker in self.workers if not worker.free]

    def _parse_steps(self, steps):
        # First let's just create all the steps.
        all_steps = set()
        for step in steps:
            letter = step.split()[-3]
            prereq = step.split()[1]
            all_steps.add(letter)
            all_steps.add(prereq)

        for step in all_steps:
            self.steps[step] = Step(step)

        # Now let's go through again and add all prereqs
        for step in steps:
            prereq = step.split()[1]
            letter = step.split()[-3]
            self.steps[letter].prereqs.append(self.steps[prereq])

    def _get_steps_without_prereqs(self):
        no_prereqs = [step for step in self.steps.values() if not step.prereqs]
        return sorted(no_prereqs)

    def _get_steps_with_prereqs_satisfied(self):
        satisfied = []
        for step in self.steps.values():
            if all(step_ in self.step_order for step_ in step.prereqs):
                satisfied.append(step)
        return satisfied

    def _get_next_step(self):
        """
        Get the next step from a dict
        of {step: [next_steps]}
        using the last step.

        4. if we have any candidates, sort alphabetically and return
        5. if not, sort and return an unsatisifed prerequisite
        6. if we have neither, this is the last step. return that.
        """

        # get steps with no prereqs
        no_prereqs = self._get_steps_without_prereqs()
        satisfied = self._get_steps_with_prereqs_satisfied()
        candidates = no_prereqs + satisfied

        # All candidates found! Eliminate duplicates and completed steps.
        old_candidates = candidates
        candidates = []
        for candidate in old_candidates:
            if candidate not in self.step_order and candidate not in candidates:
                candidates.append(candidate)

        # The alphabetically first candidate should always be the next step.
        if candidates:
            return sorted(candidates)

    def get_step_order(self):
        """
        Computes the order in which steps must be completed.
        """

        while True:
            print(f"--- SECOND {self.seconds_spent} ---")
            next_steps = self._get_next_step()
            print(f"Current steps: {self.step_order}")
            print(f"Active steps: {self.active_steps}")
            print(f"Available steps: {next_steps}")

            if not next_steps:
                break  # No steps remaining!

            # Handle multiple workers!
            if len(self.workers) > 1:
                free_workers = self.get_free_workers()
                busy_workers = self.get_busy_workers()

                # Workers who are currently busy should keep working.
                for worker in busy_workers:
                    finished_step = worker.work()
                    if finished_step:
                        self.step_order.append(finished_step)

                # Free workers should be put to work!
                for step, worker in zip(next_steps, free_workers):
                    if step not in self.active_steps:
                        finished_step = worker.work(step)

                        if finished_step:
                            self.step_order.append(step)
                        else:
                            self.active_steps.append(step)

                # Remove all new steps from active steps
                for step in self.step_order:
                    if step in self.active_steps:
                        self.active_steps.remove(step)

            else:
                self.step_order.append(next_steps[0])

            self.seconds_spent += 1

        step_order = [step.letter for step in self.step_order]
        return "".join(step_order)
