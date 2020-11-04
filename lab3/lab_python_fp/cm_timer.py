import time
from contextlib import contextmanager


class cm_timer1:
    def __init__(self):
        self.start = time.time()

    def __enter__(self):
        return

    def __exit__(self, *args):
        print('Прошло времени: ', time.time() - self.start)


@contextmanager
def cm_timer2():
    start = time.perf_counter()
    yield lambda: time.perf_counter() - start


if __name__ == '__main__':
    with cm_timer1():
        time.sleep(2)
    with cm_timer2() as t:
        time.sleep(2)
    print('Прошло времени: ', t())
