import _fix_path

from enigma import EnigmaMachine
from letter import *
from standard_parts import *
from utils.encoders import ascii_uppercase_encoder as codec


with open("data/Lorem.txt") as f:
    init_text = f.read()
init_text = (
    init_text.upper()
    .replace(" ", "")
    .replace(".", "")
    .replace(",", "")
    .replace("\n", "")
)

print("Initial: ", init_text, end="\n\n\n")

e = EnigmaMachine(
    rotors=(
        RotorIII(ring=X),
        RotorII(),
        RotorI(ring=B),
    ),
    rotors_rotate_rules=(1, 0, 0),
    reflector=Reflector_B(),
    plugboard=(
        (A, B),
        (F, K),
        (S, O),
        (P, I),
    ),
)

enc_text = e.encrypt_text(init_text, encoder=codec)
e.reset()
dec_text = e.encrypt_text(enc_text, encoder=codec)

print("Encrypted: ", enc_text, end="\n\n\n")
print("Decrypted: ", dec_text, end="\n\n\n")
print(dec_text == init_text)
