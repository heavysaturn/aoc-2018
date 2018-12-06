class Destination:
    def __init__(self, coord, letter):
        self.id = letter
        self.x = coord[0]
        self.y = coord[1]
        self.finite = True
        self.area_size = 0

    def __repr__(self):
        return self.id

    @property
    def area_id(self):
        return self.id.lower()