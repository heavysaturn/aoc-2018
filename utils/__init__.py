def load_input(input_file = "input.txt"):
    with open(input_file, "r") as readfile:
        return readfile.read().strip().split("\n")

# TIMEIT #
# timeit.timeit("function(args)", globals=globals(), number=number_of_times_to_test)
