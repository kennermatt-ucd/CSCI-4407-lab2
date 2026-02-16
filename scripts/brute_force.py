#!/usr/bin/env python3
"""Task 2 — Brute Force Single-Byte XOR"""

import sys


def score_plaintext(data):
    """Score candidate plaintext based on printable ASCII / English frequency."""
    # TODO: Implement scoring logic
    # Ideas: printable ASCII ratio, common English words, character frequency
    return 0


def brute_force_xor(input_path):
    """Try all 256 single-byte keys and rank by score."""
    # TODO: Read ciphertext
    # TODO: Loop through keys 0x00–0xFF
    # TODO: XOR, score, track best result
    # TODO: Print top candidates and save best plaintext
    pass


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <ciphertext_file>")
        sys.exit(1)

    brute_force_xor(sys.argv[1])


if __name__ == "__main__":
    main()
