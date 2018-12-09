from collections import deque
from operator import attrgetter

from day9.models.elf import Elf
from day9.models.marble import Marble


class Circle:
    """
    A circle to play a game of marbles
    with the other elves in.
    """

    def __init__(self, players, target, log=False):
        self.log = log
        self.marbles = deque()
        self.target_marbles = target
        self.players = deque([Elf(self) for _ in range(players)])
        self.marbles_played = 0

    def __repr__(self):
        marbles = ""
        for index, marble in enumerate(self.marbles):
            marbles += f"{marble.id} "
        return marbles

    def place_marble(self, marble):
        """
        Place a marble in the circle.
        """
        self.marbles.rotate(-1)
        self.marbles.append(marble)

    def get_player(self):
        """
        Gets the next player whose
        turn it is.
        """
        index = (self.marbles_played - 1) % len(self.players)
        return self.players[index]

    def get_final_score(self):
        """
        Get the player who has the highest score.
        """
        player = max(self.players, key=attrgetter("score"))
        return player.score

    def remove_marble(self):
        """
        Removes the marble 7 marbles counter-clockwise
        from the current marble, and returns it.

        Sets the marble clockwise of that one as the
        new current marble.
        """

        # Rotate 7 times counter clockwise and then remove that item
        self.marbles.rotate(7)
        marble = self.marbles.pop()

        # Rotate back so the marble clockwise of the one we removed is the current marble.
        self.marbles.rotate(-1)

        # Return the marble we removed.
        return marble

    def play(self):

        # First place a single marble in the circle.
        first_marble = Marble()
        self.place_marble(first_marble)

        if self.log:
            print(self)

        # Play until the target marble number is reached.
        while self.marbles_played != self.target_marbles:
            marble = Marble()

            # If the marble is a multiple of 23, score points!
            if marble.id % 23 == 0:
                player = self.get_player()
                removed_marble = self.remove_marble()
                player.score += marble.id
                player.score += removed_marble.id

            else:
                self.place_marble(marble)

            self.marbles_played += 1

            if self.log:
                print(self)
