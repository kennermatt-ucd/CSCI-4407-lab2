# Lab 2 — Modular Arithmetic and XOR-Based Encryption

**Course:** Security & Cryptography
**Date:** [DATE]
**Group Members:** [NAMES]

---

## Task 1 — Build XOR Tool (20 pts)

### Source Code

```python
# [PASTE XOR TOOL SOURCE CODE HERE]
```

### Screenshots

[INSERT SCREENSHOT: Encryption run]

[INSERT SCREENSHOT: Decryption run]

### Verification Evidence

[INSERT SCREENSHOT OR OUTPUT: File comparison showing original and decrypted files match]

```
# [PASTE COMPARISON COMMAND OUTPUT HERE, e.g. diff, md5sum, etc.]
```

### Explanation of XOR Symmetry

[EXPLAIN why XOR encryption and decryption use the same operation, i.e. why (P XOR K) XOR K = P]

---

## Task 2 — Break XOR via Brute Force (25 pts)

### Source Code

```python
# [PASTE BRUTE FORCE SCRIPT HERE]
```

### Recovered Key

**Key:** [HEX VALUE]

### Recovered Plaintext

```
[PASTE RECOVERED PLAINTEXT HERE]
```

### Screenshots

[INSERT SCREENSHOT: Script execution showing brute force results]

[INSERT SCREENSHOT: Recovered plaintext output]

### Explanation of Scoring Logic

[EXPLAIN how your scoring function works — e.g. printable ASCII ratio, English word detection, character frequency analysis, etc.]

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
