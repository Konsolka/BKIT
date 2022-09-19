from time import perf_counter
from time import sleep
from contextlib import contextmanager
from unique import Unique

class cm_timer1:
    def __enter__(self):
        self.t = perf_counter()
    def __exit__(self, type, value, tranceback):
        ex_time = perf_counter() - self.t
        print('exec time = ', round(ex_time, 4))
        return ex_time

@contextmanager
def cm_timer2() -> float:
    start = perf_counter()
    try:
        yield perf_counter() - start
    finally:
        print('exec time = ', round(perf_counter() - start, 4))

if __name__ == '__main__':
    with cm_timer1():
        sleep(1)
    with cm_timer2():
        sleep(2)
