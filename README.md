# inside-at-hrt
Coding workshop for Inside@HRT.

There are many teams at HRT that write code for a variety of use cases. Common to all teams is a focus on correctness, efficiency, and maintainable code.
This workshop will give you a taste of engineering at HRT and introduce you some key concepts in the industry.

When HRT wants to trade any given product on an exchange, the first step is getting market data for the exchange order book. The order book is a list of orders representing all the outstanding interest of buyers and sellers, organized by price level. Whenever a new order arrives that would satisfy an existing order on the book, the exchange will inform the two parties that a trade took place and modify the existing order as necessary (either removing it or reducing its quantity).

In many types of trading that HRT does, it is useful to keep track of the individual orders resting on the exchange's book. So in this workshop exercise, we will build a data structure that maintains the state of the book as it processes order updates. These order updates can include add, deletes, executions, and updates that apply to specific orders. As an optional followup, we will leverage out book builder code to build a matching engine. 

## Quick Start
### Running the Code
We provided a bash script `run_test.sh` with different options to run the script against different inputs, test the output against the expected "golden" output, and time the run.

We recommend making progress in the following order
1. Achieving correctness with a small sample test. `./run_test.sh -c`
1. Improving efficiency and reducing the time to run on the full orders file. `./run_test.sh -t`
1. Achieving correctness with the full orders file. `./run_test.sh -r`
1. Achieving correctness with the matching engine. `./run_test.sh -m`.

## Order Book
An order book keeps track of open orders. 

There are four relevant events that can modify our order book: 
1. Add: A new order added to the book
1. Update: An update (price, size) to a resting order on the book
1. Exec: An execution (full or partial) to a resting or incoming order 
1. Cancel: A cancellation (full or partial) to a resting order on the book

These updates are applied to our book via callbacks. A callback is a function that can be configured to be invoked under specific circumstances.
A class can define and subscribe its callbacks to an upstream object. Conversely, a class can have a list of downstream callbacks that it promises to invoke.
It is common to use callbacks for clean and extendable data flow.

Our order book exposes a couple of functions view or track the state of the orders:
1. get_best_bids(symbol): Returns a list of orders at the best (highest) bid price for the symbol. Orders within this list are sorted by the time they were added to the Book (price-time priority).
1. get_best_asks(symbol): Returns a list of orders at the best (lowest) ask price for the symbol. Orders within this list are sorted by the time they were added to the Book (price-time priority).
1. sub_on_inside(cb): Subscribes a callback to be invoked when the price or size of orders at the best bid/ask changes.


You can find the skeleton code in `Book.py`. 



## Matching Engine (Extension!)
A matching engine is used by exchanges to match orders from prospective buyers and sellers.

A matching engine typically implements a Book to keep track of orders and cancellation. In our case, the matching engine will also keep track of a list of external books that it will update when it sees a new, updated, executed, or cancelled order.


A matching engine behaves similarly to an order book but also performs a couple more checks.
There are three relevant events that can modify the state of the matching engine:
1. New: A new order. The matching engine will attempt to match this incoming order against a resting order on the book using price-time priority. The incoming order may partially or fully executed. If the incoming order is partially executed, it must be added to the book. The resting order may be partially or fully executed. If the resting order is fully executed, it must be removed from the book. Reminder: A trade involves 2 or more executions (at least one per side). 
2. Update. An update to an existing order. If the order does not exist, the matching engine must reject the order. Similarly, if the order attempts to increase the size, the matching engine must reject the order.
3. Cancel: A cancellation of an existing order. If the order does not exist, the matching engine must reject the order.

## Submission
This exercise is not intended to be finished in a few hours so no sweat if you didn't get to all of it. We're mostly interested in seeing your ideas.
Some guidance for your submission
1. Prioritize your work in order of what's listed in [Quick Start](#quick-start)
1. Document your code. If you have ideas you couldn't fully execute, document your intentions
1. Write clean code. Your code doesn't have to be production ready but try to use clear variable names and reduce code repetition


Run the following
```
$ ./run_test.sh -c > submit.txt
$ ./run_test.sh -t 2>> submit.txt
$ zip YOUR_NAME.zip Book.py MatchingEngine.py submit.txt
```

See in-classroom instructions for submitting the zip file.
