from Printer import *
from Book import *
from Events import *
from Reader import *
from MatchingEngine import *

import argparse

# This file should NOT be modified
if __name__=="__main__":
    parser =argparse.ArgumentParser(
        prog="run_book",
        description="Construct an order book and invoke callbacks from a given orders file")
    parser.add_argument('-i','--input',required=True) # input orders file
    parser.add_argument('-o','--output',required=True) # output file
    parser.add_argument('-m','--matching',action="store_true") # Test with MatchingEngine
    args = parser.parse_args()

    b = Book()
    p = Printer(args.output)
    r = Reader(args.input)


    def on_inside(symbol : str, side : Side ):
        if side == Side.Bid:
            p.print(b.get_best_bids(symbol))
        elif side == Side.Ask:
            p.print(b.get_best_asks(symbol))
        else:
            raise Exception("Invalid side")

    b.sub_on_inside(on_inside)

    m = None
    if args.matching:
        m = MatchingEngine()
        m.subscribe(b)

    if m:
        r.sub_on_add(m.on_new)
        r.sub_on_update(m.on_update)
        r.sub_on_cancel(m.on_cancel)
    else:
        r.sub_on_add(b.on_add)
        r.sub_on_update(b.on_update)
        r.sub_on_cancel(b.on_cancel)

    r.read()
