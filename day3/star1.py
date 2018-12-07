from utils import load_input

from .models import Sheet

claims = load_input()
sheet = Sheet(1000, 1000)

for claim in claims:
    sheet.add_claim(claim)

print(sheet.overlaps)
