from enigma import Enigma
from letter import *
from standard_parts import *
from utils.encoders import ascii_uppercase_encoder as codec


with open('data/Lorem.txt') as f:
    text = f.read()

text = text.upper()

print('Initial: ', text, end='\n\n\n')

# e = Enigma(
#     rotors=(
#         RotorIII(ring=X),
#         RotorII(),
#         RotorI(ring=B),
#     ),
#     rotors_roll_rules=(1, 0, 0),
#     reflector=Reflector_B(),
#     plugboard=(
#         (A, B),
#         (F, K),
#         (S, O),
#         (P, I),
#     ),
# )
e = Enigma(
    rotors=(
        RotorIII(B, B),
        RotorII(A, A),
        RotorI(E, E),
    ),
    rotors_roll_rules=(1,0,0),
    reflector=Reflector_B(),
)
enc_text = e.encrypt_text(text, codec)
e.reset()
dec_text = e.encrypt_text(enc_text, codec)

print('Encrypted: ', enc_text, end='\n\n\n')
print('Decrypted: ', dec_text, end='\n')
print(dec_text == text)



# text = [0,1,2] * 40

# e =  Enigma(
#     rotors=[
#         Rotor([1,0,2], offset=1, notches=[0]),
#         Rotor([2,1,0], offset=0, notches=[2]),
#         Rotor([2,0,1], offset=2, notches=[1]),
#     ],
#     rotors_roll_rules=[1, 0, 2],
#     reflector=Reflector([2,1,0], offset=1),
# )
# enc_text = e.encrypt_encoded_text(text)
# e.reset()
# dec_text = e.encrypt_encoded_text(enc_text)
# print('Encrypted: ', enc_text)
# print('\n' * 0)
# print('Decrypted: ', dec_text)
