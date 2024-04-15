from Events import *
from typing import Callable


class Book:
    def __init__(self):
        pass

    # Callback to be invoked on a new order.
    def on_add(self, order : Order) -> int:
        # TODO implement
        return order.refnum

    # Callback to be invoked on an update to an existing order
    # The Update order contains the refnum of the order it is updating. An update may 
    # only change the price and/or size. It cannot change the symbol or side of the order.
    # Updates must maintain PIQ (place-in-queue).
    def on_update(self, order : Order) -> None:
        # TODO implement
        pass

    # Callback to be invoked on a Cancel. A Cancel order only contains
    # the symbol and the refnum and size.
    # A size of 0 indicates that the order is to be removed entirely.
    # A size greater than 0 indicates only `size` number of shares should be cancelled.
    # Cancels with non-0 size must maintain PIQ (place-in-queue).
    # NOTE: Assume size 0 cancels until the MatchingEngine followup.
    def on_cancel(self, order :Order) -> None:
        # TODO implement
        pass

    # Callback to be invoked on an execution of an order.
    # NOTE: Can be left unimplemented until the MatchingEngine followup.
    def on_exec(self, order : Order) -> None:
        # TODO implement
        pass

    # Returns a list of orders at the best Bid price. The best Bid price is the
    # highest price of all Bid orders for a symbol. The output must be sorted by
    # price-time priority.
    def get_best_bids(self, symbol : str) -> list[Order]:
        # TODO implement
        return []

    # Returns a list of orders at the best Ask price. The best Ask price is the
    # lowest price of all Ask orders for a symbol. The ouput must be sorted by 
    # price-time priority.
    def get_best_asks(self, symbol : str) -> list[Order]:
        # TODO implement
        return []


    # Subscribes a callback `cb` that is invoked when the inside changes.
    # The inside refers to the best bid or ask. The inside changes if the 
    # price or size of best bid/ask for the symbol changes.
    # The callback is to be invoked with the symbol and Side that changed.
    def sub_on_inside(self, cb : Callable[[ str, Side],None]) -> None:
        # TODO implement
        pass

