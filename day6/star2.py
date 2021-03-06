import timeit
from operator import itemgetter

from day6.models.grid import ChronalGrid
from utils import load_input


def star2():
    chronal_coords = load_input()

    # Convert input to a list of tuples
    tuple_coords = []
    for coord in chronal_coords:
        x, y = coord.split(", ")
        tuple_coords.append((int(x), int(y)))

    # Figure out the necessary height and width
    width = max(tuple_coords, key=itemgetter(0))[0] + 2
    height = max(tuple_coords, key=itemgetter(1))[1] + 1

    print(f"width: {width}")
    print(f"height: {height}")

    # Initiate the grid
    grid = ChronalGrid(width, height)
    grid.process_coords(tuple_coords)

    # Print the largest area for a finite destination
    print(grid.get_largest_safe_area())


print(timeit.timeit("star2()", globals=globals(), number=1))
