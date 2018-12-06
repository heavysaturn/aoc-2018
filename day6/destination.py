import os
import binascii


class Destination:
    def __init__(self, coord):
        self.id = str(binascii.b2a_hex(os.urandom(15)))
        self.x = coord[0]
        self.y = coord[1]
        self.finite = True
        self.area_size = 0

    def __repr__(self):
        return self.id