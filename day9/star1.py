import timeit

from day9.models import Circle


def star1():
    circle = Circle(players=30, target=5807)
    circle.play()
    print(circle.get_final_score())


print(timeit.timeit("star1()", globals=globals(), number=1))
