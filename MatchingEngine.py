from Book import *

class MatchingEngine:
    def __init__(self, book : Book):
        self.book = book
        self.subscribedBooks = []

    def onNew(self, order : Order):
        pass

    def onUpdate(self, order : Order):
        # can only make price more aggressive
        pass

    def onCancel(self, order : Order):
        pass


    def _onAdd(self, order : Order):
        [book.onAdd(order) for book in self.subscribedBooks]

    def _onUpdate(self, old : Order, new: Order):
        [book.onUpdate(old, new) for book in self.subscribedBooks]
    def _onCancel(self, order :Order):
        [book.onCancel(order) for book in self.subscribedBooks]

    def _onExec(self, order :Order):
        [book.onExec(order) for book in self.subscribedBooks]

    # call the onAdd, onUpdate, onCancel, onExec
    def subscribe(self, otherBook : Book):
        self.subscribedBooks.append(otherBook)
