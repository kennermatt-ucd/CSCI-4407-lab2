#!/usr/bin/env python3
"""Task 2 — Brute Force Single-Byte XOR"""

import sys

def get_PlainTextScore(data):
    """
    Calculates a score for a byte string based on character frequency.
    Higher score = more likely to be plain text.
    """
    Score = 0
    #ASCII range: space (32) to tilde (126)
    #Whitespace: tab (9), newline (10), carriage return (13)

    for byte in data:
        #Checks if our byte is printable or common whitespace
        if (32 <= byte <= 126) or byte in [9, 10, 13]:
            Score += 1

        #Characters that don't often appear in text (Something like null bytes) will negatively increment the score to filter the data.
        elif byte < 32 or byte > 126:
            Score -= 1

    return Score

def main():
    Filename = 'xor_chal_text.bin'

    #Reads the ciphertext file
    try:
        with open(Filename, 'rb') as f:
            Ciphertext = f.read()
    except FileNotFoundError:
        print(f"Error: Could not find '{Filename}'.")
        print("Make sure the file is in the same directory as this script.")
        sys.exit(1)

    print(f"[*] Loaded {len(Ciphertext)} bytes from {Filename}")
    print("[*] Starting brute-force attack (0x00 - 0xFF)...\n")

    Candidates = []

    #Try every possible key from 0 to 255
    for key in range(256):

        #Decrypt the data with the current key
        DecryptedData = bytes([b ^ key for b in Ciphertext])
        #Scores our result
        Score = get_PlainTextScore(DecryptedData)
        #Stores the data: (Score, key, DecryptedData)
        Candidates.append((Score, key, DecryptedData))

    #Sorts the candidates by their score (highest score is listed first)
    Candidates.sort(key=lambda x: x[0], reverse=True)

    #Print the first 5 results
    print("--- TOP 5 CANDIDATES ---")
    for i in range(5):
        Score, key, Plaintext = Candidates[i]

        #Converts the  bytes to a string for display
        Preview = Plaintext[:60].decode('utf-8', errors='replace').replace('\n', ' ')
        print(f"Rank {i+1}: Key = {hex(key)} ({key}) | Score: {Score}")
        print(f"Preview: {Preview}...")
        print("-" * 40)

if __name__ == "__main__":
    main()
