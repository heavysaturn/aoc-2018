"""
100% stolen from sco1. Thanks ELA!
"""

import re

import matplotlib.pyplot as plt
import networkx as nx
from utils import load_input

steps = load_input(input_file="../data/input.txt")
exp = r"(?<=[Ss]tep\s)(\w)"
puzzle_input = [re.findall(exp, line) for line in steps]

# Make a graph
G = nx.DiGraph()
G.add_edges_from(puzzle_input)
nx.draw(G, with_labels=True, font_weight='bold')
plt.savefig("visualization.png")
