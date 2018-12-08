from collections import deque

from day8.models import Node


class Tree:
    def __init__(self, tree_data):
        self.raw_data = tree_data
        self.tree_data = deque(tree_data.split(" "))
        self.nodes = []

    def get_node(self):
        """
        Gets the next node in the tree_data.

        This assumes that the data to the left in the deque
        is always going to be the number of child nodes for this
        node.
        """

        # First pop the two leftmost elements - the child nodes and the metadata quantities.
        child_nodes = int(self.tree_data.popleft())
        metadata_entries = int(self.tree_data.popleft())

        # Next, fetch all children into a list.
        children = []
        for _ in range(child_nodes):
            children.append(self.get_node())

        # Now fetch the metadata
        metadata = []
        for _ in range(metadata_entries):
            metadata.append(self.tree_data.popleft())

        # Now store all this data in the node, and then add it to the tree.
        node = Node(children, metadata)
        self.nodes.append(node)
        return node

    def parse_nodes(self):
        """
        Parse all the nodes in the dataset.
        """

        while self.tree_data:
            self.get_node()

        print(f"All {Node.total_child_nodes} nodes parsed!")

    @staticmethod
    def get_total_metadata_sum():
        """
        Get the total sum of the metadata of all nodes.
        """
        return Node.total_metadata_sum

    def get_root_node_value(self):
        """
        Get the value of the root node.
        """
        return self.nodes[-1].value

