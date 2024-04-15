from typing import Callable
from Events import Order, Side
import gzip

# This file should NOT be modified
class Reader:
    def __init__(self, fname : str):
        self.fname = fname
        self.on_add_cbs = []
        self.on_update_cbs = []
        self.on_cancel_cbs = []
        self.on_exec_cbs = []

    def read(self):
        if self._is_gz_file():
            with gzip.open(self.fname, 'r') as f:
                lines = f.readlines()
                for line_str in lines:
                    self._process_line(line_str.decode())
                self._read(f)
        else:
            with open(self.fname, 'r') as f:
                lines = f.readlines()
                for line_str in lines:
                    self._process_line(line_str)

    def sub_on_add(self, cb : Callable[[Order], int]):
        self.on_add_cbs.append(cb)

    def sub_on_update(self, cb : Callable[[Order], None]):
        self.on_update_cbs.append(cb)

    def sub_on_cancel(self, cb : Callable[[Order], None]):
        self.on_cancel_cbs.append(cb)

    def sub_on_exec(self, cb : Callable[[Order], None]):
        self.on_exec_cbs.append(cb)

    def _process_line(self, line_str : str):
        line = line_str.split(' ')
        symbol = line[0]
        action = line[1]
        refnum = int(line[2])

        order = Order(symbol, refnum)
        if action == "add":
                order.side = Side[line[3]]
                order.size = float(line[4])
                order.price = float(line[6])
                [cb(order) for cb in self.on_add_cbs]
        elif action == "update":
                order.side = Side[line[3]]
                order.size = float(line[4])
                order.price = float(line[6])
                [cb(order) for cb in self.on_update_cbs]
        elif action == "cancel":
                [cb(order) for cb in self.on_cancel_cbs]
        else:
            raise Exception("Unsupported action ", action)

    def _read(self, f ):
        lines = f.readlines()
        for line_str in lines:
            self._process_line(line_str)
            

    def _is_gz_file(self):
        with open(self.fname, 'rb') as test_f:
            return test_f.read(2) == b'\x1f\x8b'

