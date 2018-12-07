class Step:
    """
    Represents a step in the Instructions
    """
    def __init__(self, letter):
        self.prereqs = []  # Prerequisite steps
        self.letter = letter
        self.duration = 60 + (ord(letter) - 64)

    def __repr__(self):
        return self.letter

    def __lt__(self, other):
        return self.letter < other.letter

    def __gt__(self, other):
        return self.letter > other.letter

    def __eq__(self, other):
        return self.letter == other.letter

    def __ne__(self, other):
        return self.letter != other.letter
