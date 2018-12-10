import timeit

from day10.models.sky import Sky
from utils import load_input


def star2():
    point_vectors = load_input(input_file="data/input.txt")
    sky = Sky(point_vectors)
    sky.parse()
    sky.gaze()
    print(f"Number of seconds elapsed: {sky.seconds_elapsed}")


print(timeit.timeit("star2()", globals=globals(), number=1))
