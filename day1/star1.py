from utils import load_input

freq = 0
freq_changes = load_input()

for change in freq_changes.split():
    op, *num = change
    num = int("".join(num))

    if op == "+":
        freq += num
    else:
        freq -= num

print("--- FREQUENCY FOUND ---")
print(f"The frequency is {freq}")
