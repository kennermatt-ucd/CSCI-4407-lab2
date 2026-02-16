#!/usr/bin/env python3
"""Task 1 — XOR Encryption/Decryption Tool"""

import sys


def xor_file(input_path, output_path, key):
    """XOR each byte of input file with key and write to output."""
    # TODO: Read input file in binary mode
    # TODO: XOR each byte with key
    # TODO: Write output in binary mode
    # TODO: Print mode, key, input size, first 16 output bytes (hex)
    pass


def main():
    if len(sys.argv) != 5:
        print(f"Usage: {sys.argv[0]} encrypt|decrypt <input> <output> <hex_key>")
        sys.exit(1)

    mode = sys.argv[1]
    input_path = sys.argv[2]
    output_path = sys.argv[3]
    key = int(sys.argv[4], 16)

    xor_file(input_path, output_path, key)


if __name__ == "__main__":
    main()
