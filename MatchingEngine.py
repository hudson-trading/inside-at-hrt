from Book import *

class MatchingEngine:
    def __init__(self):
        self._book = Book() # internal book
        self._subscribed_books = []
        self._on_reject_cbs = []

    # Callback to be invoked when a new order is submitted to the matching engine.
    # `refnum` is unpopulated on `order`. If the incoming `order` matches a resting order,
    # execute both orders. If `order` still needs to be added to the book, generate a
    # unique, positive refnum for the order before adding it to the book and invoking 
    # downstream callbacks. 
    # Return the order's refnum if the order was added to the book. Return -1 if
    # no order was added.
    def on_new(self, order : Order) -> int:
        return -1

    # Callback to be invoked when an update order is submitted to the matching engine.
    # Reject any orders that make the price more aggressive.
    def on_update(self, order : Order) -> None:
        pass


    # Callback to be invoked when an order is cancelled. Partial cancels are acceptable.
    # A size of 0 indicates cancelling all shares of an order.
    # Price and Side are not expected to be populated.
    def on_cancel(self, order : Order) -> None:
        pass


    # Invoke downstream callbacks on a new order.
    def _on_add(self, order : Order) -> None:
        [book.on_add(order) for book in self._subscribed_books]

    # Invoke downstream callbacks on an update.
    def _on_update(self, order : Order) -> None:
        [book.on_update(order) for book in self._subscribed_books]

    # Invoke downstream callbacks on a cancel.
    def _on_cancel(self, order :Order) -> None:
        [book.on_cancel(order) for book in self._subscribed_books]

    # Invoke downstream callbacks on an exec.
    def _on_exec(self, order :Order) ->None:
        [book.on_exec(order) for book in self._subscribed_books]

    # Invoke downstream callbacks on a reject.
    def _on_reject(self, order :Order) ->None:
        [cb[order] for cb in self._on_reject_cbs]

    # Subscribe an `external_book` that subscribes to add, update, cancel, exec
    # messages from matching engine.
    def subscribe(self, external_book : Book):
        self._subscribed_books.append(external_book)

    # Subscribe a callback `cb` to be invoked when an order is rejected by 
    # the matching engine.
    def sub_on_reject(self, cb : Callable[[Order],None]):
        self._on_reject_cbs.append(cb)


