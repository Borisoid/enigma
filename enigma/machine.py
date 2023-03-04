from typing import Sequence
from typing import Union

from utils.encoders import Encoder

from .reflector import ReflectorSlot
from .rotor import RotorSlot


class EnigmaMachine:
    __slots__ = (
        "rotors",
        "rotors_rotate_rules",
        "reflector",
        "reflector_rotate_rule",
        "plugboard",
    )

    def __init__(
        self,
        *,
        rotors: Sequence[RotorSlot],
        rotors_rotate_rules: Sequence[Union[int, bool]],
        reflector: ReflectorSlot,
        reflector_rotate_rule: Union[int, bool] = False,
        plugboard: Sequence[tuple[int, int]] | None = None,
    ):
        """
        `rotor_rotate_rules` - how much `i`'th rotor is rotated
        with each key press.
        If `0` then i'th rotor rotates once when `i-1`'th rotor hits a notch.
        If `False` then `i`'th rotor is stationary regardless of anything.

        `reflector_rotate_rule` - how much reflector is rotated
        with each key press.
        If `0` then reflector rotates once when the last rotor hits a notch.
        If `False` then reflector is stationary regardless of anything.
        """

        self.rotors = rotors
        self.rotors_rotate_rules = rotors_rotate_rules

        self.reflector = reflector
        self.reflector_rotate_rule = reflector_rotate_rule

        self.plugboard: dict[int, int] = {}
        if plugboard is not None:
            for l, r in plugboard:
                self.plugboard[l] = r
                self.plugboard[r] = l

    def reset(self) -> None:
        for r in self.rotors:
            r.reset()
        self.reflector.reset()

    def get_plugboard_commutated_index(self, index: int, /) -> int:
        return self.plugboard.get(index, index)

    def rotate_rotors(self) -> None:
        for n, rotor, rotate_rule in zip(
            range(len(self.rotors)),
            self.rotors,
            self.rotors_rotate_rules,
        ):
            if rotate_rule is False or n == 0:
                continue
            rotor.rotate(max(rotate_rule, self.rotors[n - 1]._hit_notches_count()))

    def rotate_reflector(self) -> None:
        if self.reflector_rotate_rule is not False:
            self.reflector.rotate(
                max(self.reflector_rotate_rule, self.rotors[-1]._hit_notches_count())
            )

    def encrypt_index(self, index: int, /) -> int:
        self.rotate_rotors()
        self.rotate_reflector()

        index = self.get_plugboard_commutated_index(index)

        for r in self.rotors:
            index = r.encrypt_forward(index)

        index = self.reflector.reflect(index)

        for r in self.rotors[::-1]:
            index = r.encrypt_backward(index)

        index = self.get_plugboard_commutated_index(index)

        return index

    def encrypt_data(self, encoded_data: Sequence[int], /) -> Sequence[int]:
        return tuple(map(self.encrypt_index, encoded_data))

    def encrypt_text(self, text: str, /, *, encoder: Encoder[str]) -> str:
        char_list = []
        for char_index in encoder.try_encode(text):
            encrypted_char_index = self.encrypt_index(char_index)
            encrypted_char = encoder.try_decode((encrypted_char_index,))[0]
            char_list.append(encrypted_char)
        return "".join(char_list)
