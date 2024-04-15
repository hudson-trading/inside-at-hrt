from Book import *

class MatchingEngine:
    def __init__(self):
        self._book = Book() # internal book
        self._subscribed_books = []
        self._on_reject_cbs = []

    # Handles a new order submitted to the matching engine.
    # `refnum` is unpopulated on `order`. If the incoming `order` matches a resting order,
    # both orders are executed. If `order` still needs to be added to the book, a
    # unique, positive refnum is generated and set on the order before the order is 
    # added to the book and downstream callbacks are invoked.
    # Returns the order's refnum if the order was added to the book. Returns -1 if
    # no order was added.
    def on_new(self, order : Order) -> int:
        return -1


    # Handles an order update submitted to the matching engine.
    # Rejects any orders that increase the size.
    def on_update(self, order : Order) -> None:
        pass


    # Handles an order cancellation submitted to the matching engine. 
    # Partial cancels are acceptable.
    # A size of 0 indicates cancelling all shares of an order.
    # Price and Side are not expected to be populated.
    def on_cancel(self, order : Order) -> None:
        pass


    # Invoke downstream callbacks on a new order.
    def _call_on_add(self, order : Order) -> None:
        [book.on_add(order) for book in self._subscribed_books]

    # Invoke downstream callbacks on an update.
    def _call_on_update(self, order : Order) -> None:
        [book.on_update(order) for book in self._subscribed_books]

    # Invoke downstream callbacks on a cancel.
    def _call_on_cancel(self, order :Order) -> None:
        [book.on_cancel(order) for book in self._subscribed_books]

    # Invoke downstream callbacks on an exec.
    def _call_on_exec(self, order :Order) ->None:
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


