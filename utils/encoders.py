from abc import ABC
from abc import abstractmethod
from string import ascii_uppercase
from typing import Generic
from typing import Sequence
from typing import TypeGuard
from typing import TypeVar


Tp_unencoded_data = TypeVar("Tp_unencoded_data")

Tp_encoded_data_piece_opt = int | None
Tp_encoded_data_piece = int

Tp_encoded_data_opt = Sequence[Tp_encoded_data_piece_opt]
Tp_encoded_data = Sequence[Tp_encoded_data_piece]


class Encoder(ABC, Generic[Tp_unencoded_data]):
    @abstractmethod
    def try_encode(self, data: Tp_unencoded_data, /) -> Tp_encoded_data:
        pass

    @abstractmethod
    def try_decode(self, data: Tp_encoded_data_opt, /) -> Tp_unencoded_data:
        pass

    def _none_not_in(self, data: Tp_encoded_data_opt, /) -> TypeGuard[Tp_encoded_data]:
        return None not in data

    def _raise_if_none_in(self, data: Tp_encoded_data_opt, /) -> Tp_encoded_data:
        if self._none_not_in(data):
            return data
        raise ValueError("contains None")


class TextEncoder(Encoder[str]):
    def __init__(self, *, alphabet: str):
        self.alphabet = alphabet
        self.alphabet_set = set(alphabet)

    def try_encode(self, text: str, /) -> Tp_encoded_data:
        index_list: list[Tp_encoded_data_piece_opt] = []
        for ch in text:
            if ch in self.alphabet_set:
                index_list.append(self.alphabet.index(ch))
            else:
                index_list.append(None)

        return self._raise_if_none_in(tuple(index_list))

    def try_decode(self, data: Tp_encoded_data_opt, /) -> str:
        return "".join(map(lambda i: self.alphabet[i], self._raise_if_none_in(data)))


ascii_uppercase_encoder = TextEncoder(alphabet=ascii_uppercase)
