from abc import ABC, abstractmethod
from string import ascii_uppercase
from typing import Generic, Optional, Sequence, TypeVar


unencoded_data = TypeVar('unencoded_data')
encoded_data = TypeVar('encoded_data', bound=Sequence[Optional[int]])


class Encoder(ABC, Generic[unencoded_data]):
    @abstractmethod
    def encode(self, data: unencoded_data) -> encoded_data:
        pass

    @abstractmethod
    def decode(self, data: encoded_data) -> unencoded_data:
        pass

    def _assert_none_not_in(self, data: encoded_data) -> None:
        if None in data:
            raise ValueError('Encoded data contains None.')


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

    def decode(self, data: encoded_data) -> str:
        self._assert_none_not_in(data)
        return ''.join(map(lambda i: self.alphabet[i], data))


ascii_uppercase_encoder = TextEncoder(ascii_uppercase)
