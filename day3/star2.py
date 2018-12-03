from day3.sheet import Sheet
from utils import load_input

claims = load_input().strip().split("\n")
sheet = Sheet(1500, 1500)

for claim in claims:
    sheet.add_claim(claim)

print(sheet.find_suitable_claim())
