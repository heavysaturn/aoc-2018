from day2.helpers import one_letter_difference
from utils import load_input

box_ids = load_input()

common_letters = ""
match_found = False

for box_id in box_ids:
    if not match_found:
        for compare_id in box_ids:
            has_diff, normalized = one_letter_difference(box_id, compare_id)

            if has_diff:
                print("--- ONE LETTER DIFFERENCE FOUND ---")
                print(f"The normalized box_id is {normalized}")
                match_found = True
                break
    else:
        break
