import timeit

from day10.models.sky import Sky
from utils import load_input


def star1():
    point_vectors = load_input(input_file="data/input.txt")
    sky = Sky(point_vectors)
    sky.parse()
    sky.gaze()
    print(sky.get_sky())


print(timeit.timeit("star1()", globals=globals(), number=1))
