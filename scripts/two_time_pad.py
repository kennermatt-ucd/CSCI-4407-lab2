#!/usr/bin/env python3
"""Task 4 — Two-Time Pad Attack (Key Reuse)"""

import sys


def xor_bytes(a, b):
    """XOR two byte sequences together."""
    # TODO: XOR corresponding bytes from both inputs
    return bytes(x ^ y for x, y in zip(a, b))


def crib_drag(xored_data, crib):
    """Slide a known word (crib) across XORed data to find plaintext segments."""
    # TODO: For each position, XOR crib with xored_data
    # TODO: Check if result looks like readable text
    # TODO: Print position and candidate plaintext
    pass


def main():
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <ciphertext1> <ciphertext2>")
        sys.exit(1)

    # TODO: Read both ciphertext files
    # TODO: XOR them together (cancels out key, leaves P1 XOR P2)
    # TODO: Use crib dragging with common words to recover plaintext
    pass


if __name__ == "__main__":
    main()
