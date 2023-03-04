from typing import Sequence

from utils.mod import mod_add


class Reflector:
    __slots__ = (
        "alphabet_length",
        "wiring",
        "ring",
    )

    def __init__(
        self,
        *,
        wiring: Sequence[int],
        ring: int = 0,
    ):
        self.alphabet_length = len(wiring)
        self.wiring = wiring
        self.ring = ring


class ReflectorSlot:
    __slots__ = (
        "reflector",
        "offset",
        "initial_offset",
    )

    def __init__(
        self,
        *,
        reflector: Reflector,
        offset: int = 0,
    ):
        self.reflector = reflector
        self.offset = offset
        self.initial_offset = offset

    def rotate(self, n: int = 1, /) -> None:
        self.offset = mod_add(self.offset, n, mod=self.reflector.alphabet_length)

    def reset(self) -> None:
        self.offset = self.initial_offset

    def reflect(self, machine_entry_index: int, /) -> int:
        of = self.offset - self.reflector.ring
        al = self.reflector.alphabet_length

        reflector_entry_index = mod_add(machine_entry_index, of, mod=al)
        reflector_exit_index = self.reflector.wiring[reflector_entry_index]
        machine_exit_index = mod_add(reflector_exit_index, -of, mod=al)
        return machine_exit_index
