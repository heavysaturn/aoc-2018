import string
from typing import Tuple

from day6.destination import Destination


class ChronalGrid:
    """
    The grid of chronal coordinates.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.sheet = [["." for _ in range(width)] for _ in range(height)]
        self.destinations = []

    def __repr__(self):
        sheet = ""
        for row in self.sheet:
            letters = []
            for letter in row:
                letters.append(str(letter))
            sheet += " ".join(letters) + "\n"
        return sheet

    @staticmethod
    def get_manhattan_distance(a, b):
        """
        Finds the manhattan distance between
        point a and point b
        """

        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def _is_border_coord(self, x, y):
        return (
            x == 0
            or x == self.width - 1
            or y == 0
            or y == self.height - 1
        )

    def get_finite_destinations(self):
        return [dest for dest in self.destinations if dest.finite]

    def get_largest_area(self):
        return max(dest.area_size for dest in self.get_finite_destinations())

    def get_total_distance(self, coordinates: Tuple[int, int]):
        """
        Get the sum of the distances
        to all destinations from the
        given coordinate.
        """

        total_sum = 0
        for dest in self.destinations:
            dest_coords = dest.x, dest.y
            total_sum += self.get_manhattan_distance(dest_coords, coordinates)

        return total_sum

    def get_largest_safe_area(self):

        region_size = 0
        for x in range(self.width):
            for y in range(self.height):
                if self.get_total_distance((x, y)) < 10000:
                    region_size += 1

        return region_size

    def process_coords(self, coords):
        """
        Process all the location coordinates
        mapping them up as Destinations,
        determining which are infinite,
        and marking all coordinates in the
        Grid with the destination they are
        closest to.
        """

        # Make a list of AA->ZZ letter combos to use for cell names.
        letters = (f"{a}{b}" for a in string.ascii_uppercase for b in string.ascii_uppercase)

        # Add all the destinations in
        for coord, letter in zip(coords, letters):
            x, y = coord
            destination = Destination(coord, letter)

            # Add to lists
            self.destinations.append(destination)
            self.sheet[y][x] = destination

        # Map up all the destination areas
        for x in range(self.width):
            for y in range(self.height):

                # Which destination is closest?
                closest = None  # type: Tuple[int, Destination]
                for destination in self.destinations:
                    dest_coords = (destination.x, destination.y)
                    post_coords = (x, y)
                    manhattan_distance = self.get_manhattan_distance(post_coords, dest_coords)

                    if closest is None or manhattan_distance < closest[0]:
                        closest = (manhattan_distance, destination)
                    elif manhattan_distance == closest[0]:
                        closest = (manhattan_distance, [destination, closest[1]])

                if closest:

                    # If this is a list, we've got multiple that are closest.
                    if isinstance(closest[1], list):
                        self.sheet[y][x] = "."

                    # Otherwise, slam an id on it.
                    else:
                        destination = self.destinations[self.destinations.index(closest[1])]

                        # Determine which ones are infinite
                        if self._is_border_coord(x, y):
                            destination.finite = False

                        # Write it!
                        if closest[0] > 0:
                            self.sheet[y][x] = destination.area_id
                            destination.area_size += 1
