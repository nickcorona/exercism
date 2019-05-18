from string import ascii_lowercase


class Cipher(object):
    def __init__(self, key=None):
        self.key = key
        self.alphabet = list(ascii_lowercase)

    def encode(self, text):
        encode_lst = []
        for letter in text:
            encode_lst.append(self.alphabet.index(letter) + self.key)
        return ''.join(encode_lst)

    def decode(self, text):
        pass
