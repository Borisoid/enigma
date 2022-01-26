from abc import ABC
from string import ascii_uppercase
from typing import TypeVar, Sequence, Generic


unencoded_data = TypeVar('unencoded_data')
encoded_data = TypeVar('encoded_data', bound=Sequence[int])


class Encoder(ABC, Generic[unencoded_data]):
    def encode(self, data: unencoded_data) -> encoded_data:
        pass

    def decode(self, data: encoded_data) -> unencoded_data:
        pass


class TextEncoder(Encoder[str]):
    def __init__(self, alphabet: str):
        self.alphabet = alphabet
        self.alphabet_set = set(alphabet)

    def encode(self, text: str) -> encoded_data:
        ind_list = []
        for ch in text:
            if ch in self.alphabet_set:
                ind_list.append(self.alphabet.index(ch))
            else:
                ind_list.append(None)
        return tuple(ind_list)

    def decode(self, text: encoded_data) -> str:
        return ''.join(map(lambda i: self.alphabet[i], text))


ascii_uppercase_encoder = TextEncoder(ascii_uppercase)
