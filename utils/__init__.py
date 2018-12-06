def load_input(input_file = "input.txt"):
    with open(input_file, "r") as readfile:
        return readfile.read().strip().split("\n")
