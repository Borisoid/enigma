from string import ascii_uppercase

from enigma import (
    Rotor,
    Reflector,
)
# from letter import *
from utils.encoders import ascii_uppercase_encoder as codec


#
def RotorI(offset=0, ring=0):
    return Rotor(
        wiring=codec.encode('EKMFLGDQVZNTOWYHXUSPAIBRCJ'),
        offset=offset,
        ring=ring,
        notches=codec.encode('Q'),
    )
#
def RotorII(offset=0, ring=0):
    return Rotor(
        wiring=codec.encode('AJDKSIRUXBLHWTMCQGZNPYFVOE'),
        offset=offset,
        ring=ring,
        notches=codec.encode('E'),
    )
#
def RotorIII(offset=0, ring=0):
    return Rotor(
        wiring=codec.encode('BDFHJLCPRTXVZNYEIWGAKMUSQO'),
        offset=offset,
        ring=ring,
        notches=codec.encode('V'),
    )

def RotorIV(offset=0, ring=0):
    return Rotor(
        wiring=codec.encode('ESOVPZJAYQUIRHXLNFTGKDCMWB'),
        offset=offset,
        ring=ring,
        notches=codec.encode('J'),
    )

def RotorV(offset=0, ring=0):
    return Rotor(
        wiring=codec.encode('VZBRGITYUPSDNHLXAWMJQOFECK'),
        offset=offset,
        ring=ring,
        notches=codec.encode('Z'),
    )

def RotorVI(offset=0, ring=0):
    return Rotor(
        wiring=codec.encode('JPGVOUMFYQBENHZRDKASXLICTW'),
        offset=offset,
        ring=ring,
        notches=codec.encode('ZM'),
    )

def RotorVII(offset=0, ring=0):
    return Rotor(
        wiring=codec.encode('NZJHGRCXMYSWBOUFAIVLPEKQDT'),
        offset=offset,
        ring=ring,
        notches=codec.encode('ZM'),
    )

def RotorVIII(offset=0, ring=0):
    return Rotor(
        wiring=codec.encode('FKQHTLXOCBJSPDZRAMEWNIUYGV'),
        offset=offset,
        ring=ring,
        notches=codec.encode('ZM'),
    )

def RotorBeta(offset=0, ring=0):
    return Rotor(
        wiring=codec.encode('LEYJVCNIXWPBQMDRTAKZGFUHOS'),
        offset=offset,
        ring=ring,
    )

def RotorGamma(offset=0, ring=0):
    return Rotor(
        wiring=codec.encode('FSOKANUERHMBTIYCWLQPZXVGJD'),
        offset=offset,
        ring=ring,
    )

###############################################################################

def Reflector_A(offset=0, ring=0):
    return Reflector(
        wiring=codec.encode('EJMZALYXVBWFCRQUONTSPIKHGD'),
        offset=offset,
        ring=ring,
    )
#
def Reflector_B(offset=0, ring=0):
    return Reflector(
        wiring=codec.encode('YRUHQSLDPXNGOKMIEBFZCWVJAT'),
        offset=offset,
        ring=ring,
    )

def Reflector_C(offset=0, ring=0):
    return Reflector(
        wiring=codec.encode('FVPJIAOYEDRZXWGCTKUQSBNMHL'),
        offset=offset,
        ring=ring,
    )

def Reflector_B_Thin(offset=0, ring=0):
    return Reflector(
        wiring=codec.encode('ENKQAUYWJICOPBLMDXZVFTHRGS'),
        offset=offset,
        ring=ring,
    )

def Reflector_C_Thin(offset=0, ring=0):
    return Reflector(
        wiring=codec.encode('RDOBJNTKVEHMLFCWZAXGYIPSUQ'),
        offset=offset,
        ring=ring,
    )

def ETW(offset=0, ring=0):
    return Reflector(
        wiring=codec.encode('ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
        offset=offset,
        ring=ring,
    )

def UTW(offset=0, ring=0):
    return Reflector(
        wiring=codec.encode('IMETCGFRAYSQBZXWLHKDVUPOJN'),
        offset=offset,
        ring=ring,
    )
