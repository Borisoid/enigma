from typing import Optional


def add(a: int, b: int, mod: Optional[int] = None) -> int:
    return a + b if mod is None else (a + b) % mod


class _ModuloRangeWithPositiveStepIterator:
    def __init__(self, start: int, stop: int, /, *, mod: int, step: int = 1):
        self.start = start
        self.current = start
        self.stop = stop
        self.mod = mod
        self.step = step

    def __next__(self) -> int:
        res = self.current % self.mod
        self.current += self.step

        if self.current > self.stop:
            raise StopIteration

        return res 


class ModuloRangeWithPositiveStep:
    """
    Examples: \n
    (2,  15, mod=10) -> [2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4]\n
    (15,  2, mod=10) -> [5, 6, 7, 8, 9, 0, 1]\n
    (0,  15, mod=10) -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4]\n
    (15,  0, mod=10) -> [5, 6, 7, 8, 9]\n
    (0,  10, mod=10) -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\n
    (10,  0, mod=10) -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\n
    (1,   0, mod=10) -> [1, 2, 3, 4, 5, 6, 7, 8, 9]\n
    (0,   0, mod=10) -> []\n
    (0,   1, mod=10) -> [0]\n
    (3,  40, mod=26) -> [
        3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24, 25, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
    ]\n
    """
    def __init__(self, start: int, stop: int, /, *, mod: int, step: int = 1):
        self.start = start
        # make <self.stop> the lowest n (n % mod == stop % mod) larger than <start>
        self.stop = stop + mod*(1 + (start - stop) // mod) if start > stop else stop

        self.mod = mod
        self.step = step

    def __iter__(self):
        return _ModuloRangeWithPositiveStepIterator(
            self.start, self.stop, mod=self.mod, step=self.step
        )
