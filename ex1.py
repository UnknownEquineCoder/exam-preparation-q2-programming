from __future__ import annotations

from typing import Generator


def every_fifth_month(n: int, /) -> Generator[str, None, None]:
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    current: int = 8
    for i in range(n):
        yield months[current]
        current += 5
        current = current % len(months)


if __name__ == '__main__':
    print(*every_fifth_month(10))
