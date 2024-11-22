from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """This is the false king, set and get his eyes and hairs"""
    def set_eyes(self, eyes):
        self.eyes = eyes

    def set_hairs(self, hairs):
        self.hairs = hairs

    def get_eyes(self):
        return self.eyes

    def get_hairs(self):
        return self.hairs
