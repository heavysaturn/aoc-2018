from day8.models import Tree
from utils import load_input

tree_data = load_input(input_file="data/input.txt", raw=True)

tree = Tree(tree_data)
tree.parse_nodes()
print(tree.get_root_node_value())
