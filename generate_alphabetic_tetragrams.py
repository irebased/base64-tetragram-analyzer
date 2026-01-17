#!/usr/bin/env python3

import base64
import itertools
import string

# Alphabet: A-Z, a-z, space
ALPHABET = string.ascii_uppercase + string.ascii_lowercase + " "

OUTPUT_FILE = "alpha_base64_tetragrams.txt"

def main():
    with open(OUTPUT_FILE, "w", encoding="ascii") as f:
        for chars in itertools.product(ALPHABET, repeat=3):
            plaintext = "".join(chars).encode("ascii")
            b64 = base64.b64encode(plaintext).decode("ascii")
            f.write(b64 + "\n")

if __name__ == "__main__":
    main()