import os

def generate_id():
    min_lc = ord(b'a')
    len_lc = 26
    ba = bytearray(os.urandom(16))
    for i, b in enumerate(ba):
        ba[i] = min_lc + b % len_lc # convert 0..255 to 97..122
    return ba
