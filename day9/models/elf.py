class Elf:
    """
    One of santas elves, engaged currently
    in a game of marbled with the other elves.
    """
    number_of_elves = 1

    def __init__(self, circle):
        self.id = self.number_of_elves + 1
        self.circle = circle
        self.score = 0
        Elf.number_of_elves += 1

    def __repr__(self):
        return f"<Elf #{self.id}>"
