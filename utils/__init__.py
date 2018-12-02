def _has_multiples(input_string, n):
    """
    Checks if a string has exactly n
    of any character.
    """
    letters = {}
    for letter in input_string:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

    # Check if we have exactly three of something
    for letter in letters:
        if letters[letter] == n:
            return True

    return False


def has_doubles(input_string):
    """
    Checks if the input_string
    has exactly two of any character.

    >>> has_doubles("aabbcc")
    True
    >>> has_doubles("aabc")
    True
    >>> has_doubles("abcd")
    False
    """
    return _has_multiples(input_string, 2)


def has_triples(input_string):
    """
    Checks if the input_string has exactly
    three of any character.

    >>> has_triples("ababcca")
    True
    >>> has_triples("aabbabc")
    True
    >>> has_triples("abcdddd")
    False
    """

    return _has_multiples(input_string, 3)


def load_input():
    with open("input.txt", "r") as readfile:
        return readfile.read()
