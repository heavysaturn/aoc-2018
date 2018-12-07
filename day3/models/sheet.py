class Sheet:
    """
    The sheet from which all the claims are cut.
    """

    def __init__(self, width, height):
        self.sheet = [[None for _ in range(width)] for _ in range(height)]
        self.claim_overlaps = {}
        self.overlaps = 0

    def find_suitable_claim(self):
        """
        Attempts to locate a claim with
        no overlaps. Otherwise returns None.
        """

        suitable_claim = [claim_id for claim_id, value in self.claim_overlaps.items() if value is False]

        if suitable_claim:
            return suitable_claim[0]

    def add_claim(self, claim):
        """
        Claims part of the sheet for a specific
        claim ID, by adding that ID to the
        correct pixels of the sheet.
        """

        # Parse the claim
        claim_id, rest = claim.split(" @ ")
        claim_id = claim_id[1:]
        left, rest = rest.split(",")
        top, rest = rest.split(": ")
        width, height = rest.split("x")

        # Typecast
        left = int(left)
        top = int(top)
        width = int(width)
        height = int(height)

        # claim the pixels
        for y in range(top, top + height):
            for x in range(left, left + width):

                # Nobody has claimed this pixel.
                if self.sheet[y][x] is None:
                    self.sheet[y][x] = [claim_id]

                    # If it's not in the tracker yet, it has no overlaps.
                    if claim_id not in self.claim_overlaps:
                        self.claim_overlaps[claim_id] = False

                # Pixel has already been claimed!
                else:
                    self.sheet[y][x].append(claim_id)

                    # If this is the first overlap, make a note.
                    if len(self.sheet[y][x]) == 2:
                        self.overlaps += 1

                    # All of these claims are overlapping.
                    for claim in self.sheet[y][x]:
                        self.claim_overlaps[claim] = True
