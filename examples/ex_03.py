import _fix_path

from enigma import EnigmaMachine
from enigma import Reflector
from enigma import ReflectorSlot
from enigma import Rotor
from enigma import RotorSlot


init_data = (0, 1, 2) * 40

print("Initial: ", init_data, end="\n\n\n")

e = EnigmaMachine(
    rotors=[
        RotorSlot(
            rotor=Rotor(
                wiring=[1, 0, 2],
                notches=[0],
            ),
            offset=1,
        ),
        RotorSlot(
            rotor=Rotor(
                wiring=[2, 1, 0],
                notches=[2],
            ),
            offset=0,
        ),
        RotorSlot(
            rotor=Rotor(
                wiring=[2, 0, 1],
                notches=[1],
            ),
            offset=2,
        ),
    ],
    rotors_rotate_rules=[1, 0, 2],
    reflector=ReflectorSlot(
        reflector=Reflector(
            wiring=[2, 1, 0],
        ),
        offset=1,
    ),
)

enc_data = e.encrypt_data(init_data)
e.reset()
dec_data = e.encrypt_data(enc_data)

print("Encrypted: ", enc_data, end="\n\n\n")
print("Decrypted: ", dec_data, end="\n\n\n")
print(dec_data == init_data)
