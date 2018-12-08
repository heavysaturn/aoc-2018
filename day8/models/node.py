from utils import next_short_string


class Node:

    total_child_nodes = 0
    total_metadata_entries = 0
    total_metadata_sum = 0
    previous_node_name = None

    def __init__(self, child_nodes: list, metadata: list):
        self.child_nodes = child_nodes
        self.metadata = [int(datum) for datum in metadata]
        self.value = self.calculate_value()

        # Set a name
        self.name = next_short_string(self.previous_node_name)
        Node.previous_node_name = self.name

        # Count totals
        Node.total_child_nodes += len(child_nodes)
        Node.total_metadata_entries += len(self.metadata)
        Node.total_metadata_sum += sum(self.metadata)

    def __repr__(self):
        return f"<Node '{self.name}'>"

    def calculate_value(self):
        """
        Calculates the value of the node.
        """

        # If it doesn't have any children, return the sum of the metadata entries.
        if not self.child_nodes:
            return sum(self.metadata)

        # If it does have children, use metadata as indexes for children
        else:
            value = 0
            for index in self.metadata:
                index = index - 1  # The metadata entries are 1-indexed.

                # Try to add the value of that child.
                try:
                    value += self.child_nodes[index].value
                except IndexError:
                    continue

            return value
