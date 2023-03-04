from string import ascii_uppercase

from enigma import Reflector
from enigma import ReflectorSlot
from enigma import Rotor
from enigma import RotorSlot

# from letter import *
from utils.encoders import ascii_uppercase_encoder as codec


#
def RotorI(offset: int = 0, ring: int = 0) -> RotorSlot:
    return RotorSlot(
        rotor=Rotor(
            wiring=codec.try_encode("EKMFLGDQVZNTOWYHXUSPAIBRCJ"),
            ring=ring,
            notches=codec.try_encode("Q"),
        ),
        offset=offset,
    )


#
def RotorII(offset: int = 0, ring: int = 0) -> RotorSlot:
    return RotorSlot(
        rotor=Rotor(
            wiring=codec.try_encode("AJDKSIRUXBLHWTMCQGZNPYFVOE"),
            ring=ring,
            notches=codec.try_encode("E"),
        ),
        offset=offset,
    )


#
def RotorIII(offset: int = 0, ring: int = 0) -> RotorSlot:
    return RotorSlot(
        rotor=Rotor(
            wiring=codec.try_encode("BDFHJLCPRTXVZNYEIWGAKMUSQO"),
            ring=ring,
            notches=codec.try_encode("V"),
        ),
        offset=offset,
    )


def RotorIV(offset: int = 0, ring: int = 0) -> RotorSlot:
    return RotorSlot(
        rotor=Rotor(
            wiring=codec.try_encode("ESOVPZJAYQUIRHXLNFTGKDCMWB"),
            ring=ring,
            notches=codec.try_encode("J"),
        ),
        offset=offset,
    )


def RotorV(offset: int = 0, ring: int = 0) -> RotorSlot:
    return RotorSlot(
        rotor=Rotor(
            wiring=codec.try_encode("VZBRGITYUPSDNHLXAWMJQOFECK"),
            ring=ring,
            notches=codec.try_encode("Z"),
        ),
        offset=offset,
    )


def RotorVI(offset: int = 0, ring: int = 0) -> RotorSlot:
    return RotorSlot(
        rotor=Rotor(
            wiring=codec.try_encode("JPGVOUMFYQBENHZRDKASXLICTW"),
            ring=ring,
            notches=codec.try_encode("ZM"),
        ),
        offset=offset,
    )


def RotorVII(offset: int = 0, ring: int = 0) -> RotorSlot:
    return RotorSlot(
        rotor=Rotor(
            wiring=codec.try_encode("NZJHGRCXMYSWBOUFAIVLPEKQDT"),
            ring=ring,
            notches=codec.try_encode("ZM"),
        ),
        offset=offset,
    )


def RotorVIII(offset: int = 0, ring: int = 0) -> RotorSlot:
    return RotorSlot(
        rotor=Rotor(
            wiring=codec.try_encode("FKQHTLXOCBJSPDZRAMEWNIUYGV"),
            ring=ring,
            notches=codec.try_encode("ZM"),
        ),
        offset=offset,
    )


def RotorBeta(offset: int = 0, ring: int = 0) -> RotorSlot:
    return RotorSlot(
        rotor=Rotor(
            wiring=codec.try_encode("LEYJVCNIXWPBQMDRTAKZGFUHOS"),
            ring=ring,
        ),
        offset=offset,
    )


def RotorGamma(offset: int = 0, ring: int = 0) -> RotorSlot:
    return RotorSlot(
        rotor=Rotor(
            wiring=codec.try_encode("FSOKANUERHMBTIYCWLQPZXVGJD"),
            ring=ring,
        ),
        offset=offset,
    )


###############################################################################


def Reflector_A(offset: int = 0, ring: int = 0) -> ReflectorSlot:
    return ReflectorSlot(
        reflector=Reflector(
            wiring=codec.try_encode("EJMZALYXVBWFCRQUONTSPIKHGD"),
            ring=ring,
        ),
        offset=offset,
    )


#
def Reflector_B(offset: int = 0, ring: int = 0) -> ReflectorSlot:
    return ReflectorSlot(
        reflector=Reflector(
            wiring=codec.try_encode("YRUHQSLDPXNGOKMIEBFZCWVJAT"),
            ring=ring,
        ),
        offset=offset,
    )


def Reflector_C(offset: int = 0, ring: int = 0) -> ReflectorSlot:
    return ReflectorSlot(
        reflector=Reflector(
            wiring=codec.try_encode("FVPJIAOYEDRZXWGCTKUQSBNMHL"),
            ring=ring,
        ),
        offset=offset,
    )


def Reflector_B_Thin(offset: int = 0, ring: int = 0) -> ReflectorSlot:
    return ReflectorSlot(
        reflector=Reflector(
            wiring=codec.try_encode("ENKQAUYWJICOPBLMDXZVFTHRGS"),
            ring=ring,
        ),
        offset=offset,
    )


def Reflector_C_Thin(offset: int = 0, ring: int = 0) -> ReflectorSlot:
    return ReflectorSlot(
        reflector=Reflector(
            wiring=codec.try_encode("RDOBJNTKVEHMLFCWZAXGYIPSUQ"),
            ring=ring,
        ),
        offset=offset,
    )


def ETW(offset: int = 0, ring: int = 0) -> ReflectorSlot:
    return ReflectorSlot(
        reflector=Reflector(
            wiring=codec.try_encode("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
            ring=ring,
        ),
        offset=offset,
    )


def UTW(offset: int = 0, ring: int = 0) -> ReflectorSlot:
    return ReflectorSlot(
        reflector=Reflector(
            wiring=codec.try_encode("IMETCGFRAYSQBZXWLHKDVUPOJN"),
            ring=ring,
        ),
        offset=offset,
    )
