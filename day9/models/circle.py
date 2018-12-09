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
        self.current_marble = None
        self.marbles = deque()
        self.target_marbles = target
        self.players = deque([Elf(self) for _ in range(players)])
        self.marbles_played = 0

    def __repr__(self):
        marbles = ""
        for marble in self.marbles:
            if marble.id == self.current_marble.id:
                marbles += f"({marble.id}) "
            else:
                marbles += f"{marble.id} "

        return marbles

    def place_marble(self, marble):
        """
        Place a marble in the circle.
        """
        if self.current_marble and marble.id > 1:
            current_index = self.marbles.index(self.current_marble)
            new_index = (current_index + 2) % len(self.marbles)

            # If we get new_index = 0, it should insert as the last element.
            if new_index:
                self.marbles.insert(new_index, marble)
            else:
                self.marbles.append(marble)

        # First two marbles can just be slammed down side by side.
        else:
            self.marbles.append(marble)

        self.current_marble = marble

    def get_next_player(self):
        """
        Gets the next player whose
        turn it is.
        """
        player = self.players[0]
        self.players.rotate(-1)  # Get the next player ready
        return player

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

        # Rotate the deque so the current marble is in position 0
        self.marbles.rotate(-self.marbles.index(self.current_marble))

        # Rotate 7 times counter clockwise and then remove that item
        self.marbles.rotate(7)
        marble = self.marbles.popleft()

        # Set next marble to current
        self.current_marble = self.marbles[0]
        return marble

    def play(self):

        # First place a single marble in the circle.
        first_marble = Marble()
        self.place_marble(first_marble)

        if self.log:
            print(self)

        # Play until the target marble number is reached.
        while self.marbles_played != self.target_marbles:
            player = self.get_next_player()
            marble = Marble()

            # If the marble is a multiple of 23, score points!
            if marble.id % 23 == 0:
                removed_marble = self.remove_marble()
                player.score += marble.id
                player.score += removed_marble.id

            else:
                self.place_marble(marble)

            self.marbles_played += 1

            if self.log:
                print(self)
