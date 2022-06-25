from typing import (
    Dict,
    Iterable,
    Optional,
    Sequence,
    Set,
    Tuple,
    Union,
)

from utils.mod import (
    ModuloRangeWithPositiveStep,
    add,
)
from utils.encoders import Encoder


class Rotor:
    def __init__(
        self,
        wiring: Sequence[int],
        offset: int = 0,
        ring: int = 0,
        notches: Iterable[int] = None
    ):
        self.alphabet_length = len(wiring)
        self.wiring = wiring
        self.offset = int(offset)
        self.ring = int(ring)

        self.notches: Set[int] = set(notches) if notches is not None else set()
        self._visited_positions: Iterable[int] = tuple()

        self.init_offset = int(offset)

    def encrypt_forward(self, machine_entry_ind: int):
        al = self.alphabet_length
        of = self.offset - self.ring

        rotor_entry_ind = add(machine_entry_ind, of, al)
        rotor_exit_ind = self.wiring[rotor_entry_ind]
        machine_exit_ind = add(rotor_exit_ind, -of, al)
        return machine_exit_ind  

    def encrypt_backward(self, machine_entry_ind: int):
        al = self.alphabet_length
        of = self.offset - self.ring

        rotor_entry_ind = add(machine_entry_ind, of, al)
        rotor_exit_ind = self.wiring.index(rotor_entry_ind)
        machine_exit_ind = add(rotor_exit_ind, -of, al)
        return machine_exit_ind

    def roll(self, n=1):
        if n == 0:
            return

        offset_to_be_set = self.offset + n
        self._visited_positions = (
            ModuloRangeWithPositiveStep(self.offset, offset_to_be_set, mod=self.alphabet_length)
        )

        self.offset = offset_to_be_set % self.alphabet_length

    def hit_notches_count(self) -> int:
        hits = 0
        for pos in self._visited_positions:
            if pos in self.notches:
                hits += 1
        return hits

    def reset(self):
        self.offset = self.init_offset
        self._visited_positions = ()


class Reflector:
    def __init__(
        self,
        wiring: Sequence[int],
        offset=0,
        ring=0,
    ):
        self.alphabet_length = len(wiring)
        self.wiring = wiring
        self.offset = offset
        self.ring = ring

        self.init_offset = offset

    def roll(self, n=1):
        self.offset = add(self.offset, n,  self.alphabet_length)

    def reset(self):
        self.offset = self.init_offset

    def reflect(self, machine_entry_ind: int):
        of = self.offset - self.ring
        al = self.alphabet_length

        reflector_entry_ind = add(machine_entry_ind, of, al)
        reflector_exit_ind = self.wiring[reflector_entry_ind]
        machine_exit_ind = add(reflector_exit_ind, -of, al)
        return machine_exit_ind


class Enigma:
    def __init__(
        self,
        rotors: Sequence[Rotor],
        rotors_roll_rules: Sequence[Union[int, bool]],
        reflector: Reflector,
        reflector_roll_rule: Union[int, bool] = False,
        plugboard: Optional[Sequence[Tuple[int, int]]] = None,
    ):
        """
        `rotor_roll_rules` - how much i'th rotor is rotated
        with each key press.
        If `0` then i'th rotor rotates once when i-1'th rotor hits a notch.
        If `False` then i'th rotor is stationary regardless of anything.

        `reflector_roll_rule` - how much reflector is rotated
        with each key press.
        If `0` then reflsector rotates once when the last rotor hits a notch.
        If `False` then reflector is stationary regardless of anything.
        """
        
        self.rotors = rotors
        self.rotors_roll_rules = rotors_roll_rules

        self.reflector = reflector
        self.reflector_roll_rule = reflector_roll_rule

        self.plugboard: Dict[int, int] = {}
        if plugboard is not None:
            for l, r in plugboard:
                self.plugboard[l] = r
                self.plugboard[r] = l

    def reset(self):
        for r in self.rotors:
            r.reset()
        self.reflector.reset()

    def get_plugboard_commutated_ind(self, ind: int) -> int:
        return self.plugboard.get(ind, ind)

    def roll_rotors(self):
        for n, rotor, roll_rule in zip(
            range(len(self.rotors)),
            self.rotors,
            self.rotors_roll_rules
        ):
            if roll_rule is False or n == 0:
                continue
            rotor.roll(max(
                roll_rule,
                self.rotors[n-1].hit_notches_count()
            ))

    def roll_reflector(self):
        if self.reflector_roll_rule is not False:
            self.reflector.roll(max(
                self.reflector_roll_rule,
                self.rotors[-1].hit_notches_count()
            ))

    def encrypt_ind(self, ind: int) -> int:
        self.roll_rotors()
        self.roll_reflector()

        ind = self.get_plugboard_commutated_ind(ind)

        for r in self.rotors:
            ind = r.encrypt_forward(ind)

        ind = self.reflector.reflect(ind)

        for r in self.rotors[::-1]:
            ind = r.encrypt_backward(ind)

        ind = self.get_plugboard_commutated_ind(ind)

        return ind

    def encrypt_data(self, encoded_data: Sequence[int]) -> Sequence[int]:
        return tuple(map(self.encrypt_ind, encoded_data))

    def encrypt_text(self, text: str, encoder: Encoder) -> str:
        char_list = []
        for char, char_ind in zip(text, encoder.encode(text)):
            if char_ind is None:
                char_list.append(char)
            else:
                enc_char_ind = self.encrypt_ind(char_ind)
                enc_char = encoder.decode((enc_char_ind,))[0]
                char_list.append(enc_char)
        return ''.join(char_list)    
