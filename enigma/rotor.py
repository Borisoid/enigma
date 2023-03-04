from typing import Iterable
from typing import Sequence

from utils.mod import ModuloRangeWithPositiveStep
from utils.mod import mod_add


class Rotor:
    __slots__ = (
        "alphabet_length",
        "wiring",
        "ring",
        "notches",
    )

    def __init__(
        self,
        *,
        wiring: Sequence[int],
        ring: int = 0,
        notches: Iterable[int] | None = None,
    ):
        self.alphabet_length = len(wiring)
        self.wiring = wiring
        self.ring = ring
        self.notches: set[int] = set(notches) if notches is not None else set()


class RotorSlot:
    __slots__ = (
        "rotor",
        "offset",
        "initial_offset",
        "_visited_positions",
    )

    def __init__(
        self,
        *,
        rotor: Rotor,
        offset: int = 0,
    ):
        self.rotor = rotor
        self.offset = offset
        self.initial_offset = offset

        self._visited_positions: Iterable[int] = tuple()

    def encrypt_forward(self, machine_entry_index: int, /) -> int:
        al = self.rotor.alphabet_length
        of = self.offset - self.rotor.ring

        rotor_entry_index = mod_add(machine_entry_index, of, mod=al)
        rotor_exit_index = self.rotor.wiring[rotor_entry_index]
        machine_exit_index = mod_add(rotor_exit_index, -of, mod=al)
        return machine_exit_index

    def encrypt_backward(self, machine_entry_index: int, /) -> int:
        al = self.rotor.alphabet_length
        of = self.offset - self.rotor.ring

        rotor_entry_index = mod_add(machine_entry_index, of, mod=al)
        rotor_exit_index = self.rotor.wiring.index(rotor_entry_index)
        machine_exit_index = mod_add(rotor_exit_index, -of, mod=al)
        return machine_exit_index

    def rotate(self, n: int = 1, /) -> None:
        if n == 0:
            return

        offset_to_be_set = self.offset + n
        self._visited_positions = ModuloRangeWithPositiveStep(
            self.offset, offset_to_be_set, mod=self.rotor.alphabet_length
        )

        self.offset = offset_to_be_set % self.rotor.alphabet_length

    def _hit_notches_count(self) -> int:
        hits = 0
        for pos in self._visited_positions:
            if pos in self.rotor.notches:
                hits += 1
        return hits

    def reset(self) -> None:
        self.offset = self.initial_offset
        self._visited_positions = tuple()
