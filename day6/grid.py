import string


class Coord:
    def __init__(self, coord, letter):
        self.letter = letter
        self.x = coord[0]
        self.y = coord[1]
        self.finite = True
        self.area_size = 1

    def __repr__(self):
        return self.letter

    @property
    def area_letter(self):
        return self.letter.lower()


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
            sheet += "".join(letters) + "\n"
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

    def process_coords(self, coords):
        """
        Claims part of the sheet for a specific
        claim ID, by adding that ID to the
        correct pixels of the sheet.
        """

        # Add all the destinations in
        for letter, coord in zip(string.ascii_uppercase, coords):
            x, y = coord
            destination = Coord(coord, letter)

            # Add to lists
            self.destinations.append(destination)
            self.sheet[y][x] = destination

        # Map up all the destination areas
        for x in range(self.width):
            for y in range(self.height):

                # Which destination is closest?
                closest = None  # type: Tuple[int, Coord]
                for destination in self.destinations:
                    dest_coords = (destination.x, destination.y)
                    post_coords = (x, y)
                    manhattan_distance = self.get_manhattan_distance(post_coords, dest_coords)

                    if closest is None or manhattan_distance < closest[0]:
                        closest = (manhattan_distance, destination)
                    elif manhattan_distance == closest[0]:
                        closest = (manhattan_distance, [destination, closest[1]])

                # Okay, now slam a letter on it.
                if closest:

                    # If this is a list, we've got multiple that are closest.
                    if isinstance(closest[1], list):
                        self.sheet[y][x] = "."
                    else:
                        destination = self.destinations[self.destinations.index(closest[1])]

                        # Determine which ones are infinite
                        if self._is_border_coord(x, y):
                            destination.finite = False

                        # Don't overwrite the actual destination
                        if closest[0] > 0:
                            self.sheet[y][x] = destination.area_letter
                            destination.area_size += 1
