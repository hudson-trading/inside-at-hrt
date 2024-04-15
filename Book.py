from Events import *
from typing import Callable



class Book:
    def __init__(self):
        pass

    # Callback to be invoked on a new order.
    def on_add(self, order : Order) -> None:
        pass

    # Callback to be invoked on an update. The Update order contains the refnum
    # of the original order it is updating. An update may only change the price
    # and/or size. It cannot change the symbol or side of the order.
    # Updates must maintain PIQ (place-in-queue).
    def on_update(self, order : Order) -> None:
        pass

    # Callback to be invoked on a Cancel. A Cancel order only contains
    # the symbol and the refnum. A cancelled order should be removed from the book.
    def on_cancel(self, order :Order) -> None:
        pass

    # Returns a list of orders at the best Bid price. The best Ask price is the
    # lowest price of all Ask orders for a symbol.
    def get_best_bids(self, symbol : str) -> list[Order]:
        return []

    # Returns a list of orders at the best Ask price. The best Ask price is the
    # lowest price of all Ask orders for a symbol.
    def get_best_asks(self, symbol : str) -> list[Order]:
        return []


    # Subscribes a callback `cb` that is invoked when the inside changes.
    # The inside refers to the best bid or ask. The inside changes if the 
    # price or size of best bid/ask for the symbol changes.
    def sub_on_inside(self, cb : Callable[[ str, Side],None]) -> None:
        pass

