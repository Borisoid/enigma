from typing import Optional


def add(a: int, b: int, mod: Optional[int] = None) -> int:
    return a + b if mod is None else (a + b) % mod


class ModuloRangeBase:
    """Base class for cyclic ranges with positive step
    """
    def __init__(self, start: int, stop: int, mod: int):
        self.current = start

        if start > stop:
            self.stop = stop + mod * (1 + ((start - stop) // mod))
        else:
            self.stop = stop

        self.mod = mod

    def __iter__(self):
        return self


class ModuloRange(ModuloRangeBase):
    """
    ModuloRange(15, 2, 10) -> [5, 6, 7, 8, 9, 0, 1]\n
    ModuloRange(2, 15, 10) - >[2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4]\n
    ModuloRange(1, 0, 10) -> [1, 2, 3, 4, 5, 6, 7, 8, 9]\n
    ModuloRange(0, 0, 10) -> []\n
    ModuloRange(0, 1, 10) -> [0]\n
    ModuloRange(15, 0, 10) -> [5, 6, 7, 8, 9]\n
    ModuloRange(0, 15, 10) -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4]\n
    ModuloRange(10, 0, 10) -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\n
    ModuloRange(3, 40, 26) -> [
        3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24, 25, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
    ]\n
    """
    def __next__(self):
        res = self.current
        self.current += 1

        if self.current > self.stop:
            raise StopIteration

        return res % self.mod
