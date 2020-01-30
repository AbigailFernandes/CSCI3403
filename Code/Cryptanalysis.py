#!/usr/bin/env python

from collections import Counter
from pycipher import Caesar

probs = {'a': 0.08, 'b': 0.015, 'c': 0.03, 'd': 0.04,
              'e': 0.13, 'f': 0.02, 'g': 0.015, 'h': 0.06,
              'i': 0.065, 'j': 0.005, 'k': 0.005, 'l': 0.035,
              'm': 0.03, 'n': 0.07, 'o': 0.08, 'p': 0.02,
              'q': 0.002, 'r': 0.065, 's': 0.06, 't': 0.09,
              'u': 0.03, 'v': 0.01, 'w': 0.015, 'x': 0.005,
              'y': 0.02, 'z': 0.002}


def get_cipher_frequency(cipher):
    length_cipher = len(cipher)
    freq = Counter(cipher)
    for key, val in freq.items():
        freq[key] = float(val) / length_cipher
    return freq

def compute_phi(cipher, highest):
    cipher = "".join(cipher.split()) 
    result = []
    freq = get_cipher_frequency(cipher)
    for i in range(26):
        total = 0
        for c in list(set(cipher)):
            c_index = ord(c) - 97
            key_index = c_index - i   
            if key_index < 0:
                key_index = (26 + key_index)
            key_char = chr(key_index + 97)
            total += freq[c] * probs[key_char]
        result.append((i, total))
    corrs = sorted(result, key=lambda x: x[1], reverse=True)
    return corrs

corrs = compute_phi('khoor zruog', 9)
for i in range(9):
    print("{}: The key is {} with phi {:03.4f}".format(i + 1, corrs[i][0], corrs[i][1]))

# Brute force finding the key, and eyeball the results
text = "khoor zruog"
for i in range(26):
    cipher = ""
    for item in text.split():
        cipher += Caesar(key=i).decipher(item) + " "
    print(str(i) + "\t" + cipher.upper())





