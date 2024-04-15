from Events import Order, Side
from Book import *

# This file should NOT be modified
class Printer:
    def __init__(self, outfile : str):
        self.outfile = outfile
        open(self.outfile, "w").close() # clear file

    def print(self, orders: list[Order]) -> None:
        if not orders:
            with open(self.outfile, "a") as f:
                f.write("empty side")

            return

        side_str = "Bid" if orders[0].side == Side.Bid else "Ask"
        out = "symbol: {}, side: {}, price: {}\n".format( orders[0].symbol, side_str, orders[0].price)
        out += ''.join([
            " refnum: {}, size: {}\n".format(order.refnum, order.size) for order in orders])

        with open(self.outfile, "a") as f:
            f.write(out)



