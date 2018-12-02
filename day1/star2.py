from utils import load_input

freq = 0
freqs = []
freq_changes = load_input()
found_twice = False

while not found_twice:
    for change in freq_changes.split():
        op, *num = change
        num = int("".join(num))

        if op == "+":
            freq += num
        else:
            freq -= num

        if freq in freqs:
            found_twice = True
            print("--- MATCH FOUND ---")
            print(f"FREQUENCY REPEATS AT: {freq}")
            break
        else:
            print(freq)
            freqs.append(freq)
