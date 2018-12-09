class Marble:
    """
    A marble to use in a
    game of marbles.
    """
    number_of_marbles = 0

    def __init__(self):
        self.id = self.number_of_marbles
        Marble.number_of_marbles += 1

    def __repr__(self):
        return f"<Marble #{self.id}>"


