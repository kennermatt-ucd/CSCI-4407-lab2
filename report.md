# Lab 2 — Modular Arithmetic and XOR-Based Encryption

**Course:** Security & Cryptography
**Date:** 02/16/2026
**Group Members:** Matthew Kenner, Cassius Kemp, Jonathan Le

---

## Task 1 — Build XOR Tool (20 pts)

### Source Code

```python
#!/usr/bin/env python3
"""Task 1 — XOR Encryption/Decryption Tool"""

import sys


def xor_file(mode, input_path, output_path, key):
    """XOR each byte of input file with key and write to output."""
    with open(input_path, "rb") as f:
        data = f.read()

    result = bytes(b ^ key for b in data)

    with open(output_path, "wb") as f:
        f.write(result)

    first16 = result[:16].hex(" ")
    print(f"Mode:            {mode}")
    print(f"Key:             0x{key:02x} ({key})")
    print(f"Input size:      {len(data)} bytes")
    print(f"First 16 bytes:  {first16}")


def main():
    if len(sys.argv) != 5:
        print(f"Usage: {sys.argv[0]} encrypt|decrypt <input> <output> <hex_key>")
        sys.exit(1)

    mode = sys.argv[1]
    input_path = sys.argv[2]
    output_path = sys.argv[3]
    key = int(sys.argv[4], 16)

    xor_file(mode, input_path, output_path, key)


if __name__ == "__main__":
    main()

```

### Screenshots

![alt text](Screenshots/xor_tool_enc_dec.png)
![alt text](Screenshots/xor_tool_text.png)
![alt text](Screenshots/xor_tool_img_with_typo.png)
![alt text](Screenshots/xor_tool_pairs.png)



### Explanation of XOR Symmetry

XOR encryption and decryption use the same operation because XOR is self-inverse, meaning applying the same XOR operation twice with the same key restores the original data.

```
(P XOR K) XOR K
= P XOR (K XOR K)
= P XOR 0
= P
```
---

## Task 2 — Break XOR via Brute Force (25 pts)

### Source Code

```python
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

    #Print the Highest scoring 3 results
    print("--- TOP 3 CANDIDATES ---")
    for i in range(3):
        Score, key, Plaintext = Candidates[i]

        #Converts the  bytes to a string for display
        Preview = Plaintext[:60].decode('utf-8', errors='replace').replace('\n', ' ')
        print(f"Rank {i+1}: Key = {hex(key)} ({key}) | Score: {Score}")
        print(f"Preview: {Preview}...")
        print("-" * 40)

if __name__ == "__main__":
    main()
```

### Recovered Key

**Key:** [0x4d]

### Recovered Plaintext

```
CSCI/CSCY 4407 - Security & Cryptography (Spring 2026)
Lab 2: XOR Brute Force Challenge

If you can read this message clearly, you recovered the correct XOR key.

Group: 10
Hint: English text + punctuation + spaces should appear normal.

Remember:
- Single-byte XOR keys are weak (only 256 possibilities).
- Validation matters: readable text is not enough; justify why it is correct.
```

### Screenshots

![alt text](Screenshots/bruteforce_xor_py_results.png)

![alt text](Screenshots/bruteforce_xor_py_plaintext.png)

### Explanation of Scoring Logic

The scoring function uses a frequency detection method to score the results of using each encryption key. The file sorts out non-regular characters (like null characters) as it iterates through the encrypted text giving a negative score each time it comes across one. At the same time while iterating through the string, when a character in the ASCII range of 32 - 126 it is considered printable and is give a positive score. This means that when we find the correct key it should have the highest score as it has the most printable characters of the different stings. However, some other keys may provide the same score as the correct key, which is why we include a preview of the decrypted text to let the user find the correct key.

---

## Task 3 — Image Header Attack (20 pts)

### Key Recovery Explanation

**Known PNG header bytes:** `89 50 4E 47 0D 0A 1A 0A`

**First encrypted byte(s):** [HEX VALUE]

**Recovered key:** [HEX VALUE]

[EXPLAIN the XOR operation used to recover the key from the known header]

### Source Code

```python
# [PASTE KEY RECOVERY / DECRYPTION SCRIPT HERE]
```

### Verification Screenshots

[INSERT SCREENSHOT: Encrypted file hex inspection]

[INSERT SCREENSHOT: Decrypted PNG image opened successfully]

### Explanation of Known-Plaintext Attack

[EXPLAIN why knowing part of the plaintext allows recovery of the key, and why this is a fundamental weakness of XOR encryption]

---

## Task 4 — Two-Time Pad Attack (25 pts)

### XOR of Ciphertexts

```python
# [PASTE SCRIPT OR COMMAND USED TO XOR THE TWO CIPHERTEXT FILES]
```

### Recovered Plaintext Segments

| Offset | Crib Used | Recovered Text |
|--------|-----------|----------------|
| [OFFSET] | [WORD] | [RECOVERED SEGMENT] |
| [OFFSET] | [WORD] | [RECOVERED SEGMENT] |
| [OFFSET] | [WORD] | [RECOVERED SEGMENT] |

### Method and Reasoning

[EXPLAIN the crib dragging process — how you chose cribs, how you identified valid plaintext, and how you extended recovered segments]

### Explanation of Key Reuse Weakness

[EXPLAIN why reusing a one-time pad key (two-time pad) breaks security, i.e. C1 XOR C2 = P1 XOR P2, eliminating the key entirely]

---

## Key Lessons Learned

- [SUMMARIZE key takeaway about XOR reversibility]
- [SUMMARIZE key takeaway about small key spaces]
- [SUMMARIZE key takeaway about known-plaintext attacks]
- [SUMMARIZE key takeaway about key reuse]

---

## Appendix

### Full Script Listings

[OPTIONAL: Include complete scripts if not fully shown above]

### Additional Screenshots

[OPTIONAL: Include any additional supporting evidence]
