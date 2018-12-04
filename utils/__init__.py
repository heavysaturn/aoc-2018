def load_input():
    with open("input.txt", "r") as readfile:
        return readfile.read().strip().split("\n")
