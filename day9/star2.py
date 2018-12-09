import timeit

from day9.models import Circle


def star2():
    circle = Circle(players=471, target=72026 * 100)
    circle.play()
    print(circle.get_final_score())


print(timeit.timeit("star2()", globals=globals(), number=1))
