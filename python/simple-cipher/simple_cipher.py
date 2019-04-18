class Cipher(object):
    def __init__(self, key=None):
        pass

    def encode(self, text):
        pass

    def decode(self, text):
        pass


string = 'balls'

shift = -1
alphabet = 'abcdefghijklmnopqrstuvwxyz'

shifted_indices = [alphabet.index(char) + shift for char in string]

encoded_string = ''.join([alphabet[index] for index in shifted_indices])
print(encoded_string)

encoded_string = 'azkkr'

shift = 1

indices = [alphabet.index(char) - shift for char in encoded_string]

decoded_string = ''.join([alphabet[index] for index in indices])
print(decoded_string)