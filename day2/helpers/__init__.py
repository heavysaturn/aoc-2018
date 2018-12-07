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


def one_letter_difference(input_string, compare_string):
    """
    Returns a tuple with two values:
    - a bool that is equal to True if there was a one letter difference
    - a normalized input_string, which no longer contains the one letter that was different.

    If there was no one letter difference, it returns False along with the original input string.

    >>> one_letter_difference("abcd", "adcb")
    (False, "abcd")
    >>> one_letter_difference("abcd", "abcd")
    (False, "abcd")
    >>> one_letter_difference("abcd", "abcr")
    (True, "abc")
    """

    difference = 0
    normalized = ""

    for input_letter, compare_letter in zip(input_string, compare_string):
        if input_letter != compare_letter:
            difference += 1
            normalized = input_string.replace(input_letter, "")

    if difference == 1:
        return True, normalized
    return False, input_string
