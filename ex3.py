from __future__ import annotations

import random
import time

from typing import Callable


def mytimer(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start} seconds")
        return result

    return wrapper


@mytimer
def func89(min: int, max: int) -> None:
    for x in range(random.randint(min, max)):
        time.sleep(random.random())


@mytimer
def test325(a: int, b: int = 5) -> None:
    for x in range(random.randint(a, b)):
        time.sleep(random.random())


if __name__ == '__main__':
    func89(8, 10)
    test325(3, 5)
