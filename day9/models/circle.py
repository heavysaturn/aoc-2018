from collections import deque


class Circle:
    """
    A circle to play a game of marbles
    with the other elves in.
    """

    def __init__(self, players, target, log=False):
        self.log = log
        self.marbles = deque([0])
        self.target_marbles = target
        self.players = [0 for _ in range(players)]
        self.marbles_played = 0

    def __repr__(self):
        marbles = ""
        deq = self.marbles.copy()
        index = deq.index(0)
        deq.rotate(-index)

        for index, marble in enumerate(deq):
            if marble == self.marbles[0]:
                marbles += f"({marble}) "
            else:
                marbles += f"{marble} "
        return marbles

    def get_final_score(self):
        """
        Get the player who has the highest score.
        """
        return max(self.players)

    def play(self):

        if self.log:
            print(self)

        # Play until the target marble number is reached.
        for marble in range(1, self.target_marbles + 1):

            # If the marble is a multiple of 23, score points!
            if marble % 23 == 0:

                # find the player index
                player_index = marble % len(self.players)

                # Rotate 7 times counter clockwise and then remove that item
                self.marbles.rotate(7)
                removed_marble = self.marbles.popleft()

                # Add the score
                self.players[player_index] += marble
                self.players[player_index] += removed_marble

            # Otherwise, just rotate and add the marble to the deque
            else:
                self.marbles.rotate(-2)
                self.marbles.appendleft(marble)

            if self.log:
                print(self)
