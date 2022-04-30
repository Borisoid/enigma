import fix_path

from enigma import Enigma, Rotor, Reflector


init_data = (0,1,2) * 40

print('Initial: ', init_data, end='\n\n\n')

e = Enigma(
    rotors=[
        Rotor([1,0,2], offset=1, notches=[0]),
        Rotor([2,1,0], offset=0, notches=[2]),
        Rotor([2,0,1], offset=2, notches=[1]),
    ],
    rotors_roll_rules=[1, 0, 2],
    reflector=Reflector([2,1,0], offset=1),
)

enc_data = e.encrypt_data(init_data)
e.reset()
dec_data = e.encrypt_data(enc_data)

print('Encrypted: ', enc_data, end='\n\n\n')
print('Decrypted: ', dec_data, end='\n\n\n')
print(dec_data == init_data)
