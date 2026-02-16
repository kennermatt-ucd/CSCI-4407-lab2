#!/usr/bin/env python3
"""Task 3 — Recover XOR Key Using Known PNG Header"""

import sys

# Standard PNG header bytes
PNG_HEADER = bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])


def recover_key(input_path):
    """XOR first byte(s) of encrypted image with known PNG header to recover key."""
    # TODO: Read first bytes of encrypted file
    # TODO: XOR with PNG_HEADER to recover key
    # TODO: Print recovered key
    pass


def decrypt_image(input_path, output_path, key):
    """Decrypt the full image file with the recovered key."""
    # TODO: XOR entire file with key
    # TODO: Write decrypted PNG to output
    pass


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <encrypted_image> <output.png>")
        sys.exit(1)

    recover_key(sys.argv[1])
    # decrypt_image(sys.argv[1], sys.argv[2], key)


if __name__ == "__main__":
    main()
