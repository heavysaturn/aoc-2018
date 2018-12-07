class Worker:
    def __init__(self, ident):
        self.id = ident
        self.free = True
        self.step = None

    def work(self, step=None):
        if self.free:
            self.free = False

        if step:
            self.step = step

        if self.step:
            self.step.duration -= 1

            if self.step.duration <= 0:
                self.free = True
                return self.step
