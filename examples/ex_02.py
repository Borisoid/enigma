import fix_path

from enigma import Enigma
from letter import *
from standard_parts import *
from utils.encoders import ascii_uppercase_encoder as codec


with open('data/Lorem.txt') as f:
    init_text = f.read()
init_text = init_text.upper()

print('Initial: ', init_text, end='\n\n\n')

e = Enigma(
    rotors=(
        RotorIII(B, B),
        RotorII(A, A),
        RotorI(E, E),
    ),
    rotors_roll_rules=(1,0,0),
    reflector=Reflector_B(),
)

enc_text = e.encrypt_text(init_text, codec)
e.reset()
dec_text = e.encrypt_text(enc_text, codec)

print('Encrypted: ', enc_text, end='\n\n\n')
print('Decrypted: ', dec_text, end='\n\n\n')
print(dec_text == init_text)
