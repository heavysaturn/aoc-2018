from utils import load_input, has_triples, has_doubles

box_ids = load_input().split()
triples = 0
doubles = 0

print(box_ids)

for box_id in box_ids:
    if has_doubles(box_id):
        doubles += 1
    if has_triples(box_id):
        triples += 1

print("--- CHECKSUM CALCULATED ---")
print(f"Checksum is {doubles * triples}")
