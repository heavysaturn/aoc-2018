from operator import itemgetter

from day6.grid import ChronalGrid
from utils import load_input

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

# Figure out the highest number
grid = ChronalGrid(width, height)
grid.process_coords(tuple_coords)
print(grid)
print(grid.get_finite_destinations())
print(grid.get_largest_area())
