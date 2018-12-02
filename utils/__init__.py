def has_doubles(box_id):
    """
    Checks if a string
    has two of any character.

    >>> has_doubles("aabbcc")
    True
    >>> has_doubles("aabc")
    True
    >>> has_doubles("abcd")
    False
    """
    letters = []
    for letter in box_id:
        if letter in letters:
            return True
        else:
            letters.append(letter)
    return False


def has_triples(input_string):
    """
    Checks if a string
    has three of any character.

    >>> has_triples("ababcca")
    True
    >>> has_triples("aabbabc")
    True
    >>> has_triples("abcd")
    False
    """
    letters = {}
    for letter in input_string:
        if letter in letters:
            letters[letter] += 1

            # Do we have triples yet?
            if letters[letter] >= 3:
                return True
        else:
            letters[letter] = 1
    return False


def load_input():
    with open("input.txt", "r") as readfile:
        return readfile.read()
