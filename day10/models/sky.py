import re
from operator import attrgetter


class Point:
    """
    A celestial point of light
    to help guide Santa.
    """
    def __init__(self, pos, vel):
        self.x, self.y = pos
        self.vel_x, self.vel_y = vel

    def move(self, multiplier=1, reverse=False):
        if reverse:
            self.x -= (self.vel_x * multiplier)
            self.y -= (self.vel_y * multiplier)
        else:
            self.x += (self.vel_x * multiplier)
            self.y += (self.vel_y * multiplier)


class Sky:
    """
    A bright christmas sky
    filled with celestial points.

    Over time, these will form a
    message.
    """

    def __init__(self, point_vectors):
        self.point_vectors = sorted(point_vectors)
        self.points = []
        self.width = None
        self.height = None
        self.min_x = None
        self.min_y = None
        self.prev_y_diff = None
        self.seconds_elapsed = 0

    def get_sky(self):
        # Build a sky
        sky = []
        for _ in range(self.height + 1):
            row = []
            for _ in range(self.width + 1):
                row.append(".")
            row.append("\n")
            sky.append(row)

        # Fill in all the points
        for point in self.points:
            y = point.y - self.min_y
            x = point.x - self.min_x
            sky[y][x] = "#"

        # Store it all as a string
        output = ""
        for row in sky:
            output += "".join(row)

        return output

    def parse(self):
        for vector in self.point_vectors:
            expression = "(-*\d+)"
            parsed = re.findall(expression, vector)
            pos = (int(parsed[0]), int(parsed[1]))
            vel = (int(parsed[2]), int(parsed[3]))
            self.points.append(Point(pos, vel))

    def gaze(self):
        """
        Gaze upon the sky until a message appears.
        """

        while True:
            # Calculate mins and maxes
            max_y = max(self.points, key=attrgetter("y")).y
            self.min_y = min(self.points, key=attrgetter("y")).y
            max_x = max(self.points, key=attrgetter("x")).x
            self.min_x = min(self.points, key=attrgetter("x")).x

            # If there are any coords in negative space
            # we can skip ahead until that's no longer the case
            if self.min_y < 0 or self.min_x < 0:
                distance = max(abs(self.min_x), abs(self.min_y))
                x_vel_max = max(self.points, key=attrgetter("vel_x")).vel_x
                y_vel_max = max(self.points, key=attrgetter("vel_x")).vel_y
                speed = max(x_vel_max, y_vel_max)
                multiplier = (distance // speed) or 1

                for point in self.points:
                    point.move(multiplier)

            # Store the width and height of the current area
            self.width = max_x - self.min_x
            self.height = max_y - self.min_y

            # Check if we're done
            y_diff = max_y - self.min_y

            # If the y_diff starts to go up, the previous y_diff must've been our target.
            if self.prev_y_diff and y_diff > self.prev_y_diff:
                # Reverse back one vector length
                for point in self.points:
                    point.move(reverse=True)
                break

            # If not, we should continue to move forward.
            else:
                self.prev_y_diff = y_diff

                # Move the points
                for point in self.points:
                    point.move()

                # Count seconds
                self.seconds_elapsed += 1
