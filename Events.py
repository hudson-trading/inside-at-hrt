from enum import Enum

class Side(Enum):
    Bid = 1
    Ask = 2
    Invalid = 3

class Order:
    def __init__(self, symbol : str, refnum : int):
        self.symbol = symbol
        self.refnum = refnum

        # defaults
        self.side = Side.Invalid
        self.price = 0.0
        self.size = 0.0
