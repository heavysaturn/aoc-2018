import timeit

from day8.models import Tree
from utils import load_input


def star1():
    tree_data = load_input(input_file="data/input.txt", raw=True)

    tree = Tree(tree_data)
    tree.parse_nodes()
    print(tree.get_total_metadata_sum())


print(timeit.timeit("star1()", globals=globals(), number=1))
