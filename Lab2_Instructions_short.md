The full lab document is very long, so instead of copying it verbatim, here is a **clean Markdown version of the lab instructions rewritten and condensed** for practical use. This keeps all required tasks and expectations while making it easier to read, store in GitHub, or share in Teams.

You can save this as `lab2.md`.

---

```md
# Lab 2 — Modular Arithmetic and XOR-Based Encryption
**Course:** Security & Cryptography  
**Topic:** XOR Encryption and Cryptographic Failures

---

## Overview
This lab explores how XOR encryption works and how improper usage leads to security failures. You will:

1. Build an XOR encryption tool.
2. Break XOR encryption using brute force.
3. Recover encryption keys using known plaintext.
4. Exploit key reuse in a two-time pad attack.

Work is completed in groups, and results will differ per group due to unique ciphertexts.

---

## Environment Requirements
Use a Linux environment (Kali Linux recommended).

Required tools:
- Python 3
- Terminal access
- `xxd` or `hexdump`
- `file` command
- Text editor (nano, vim, VS Code)

All work must be reproducible.

---

## Provided Ciphertext Files
Each group receives encrypted files including:

- Single-byte XOR encrypted text
- XOR encrypted PNG image
- Two ciphertext files encrypted with reused key

---

# Task 1 — Build XOR Tool

## Goal
Create a Python tool that encrypts and decrypts files using XOR.

## Program Requirements
Program must:
- Accept arguments:
```

encrypt|decrypt input output key

```
- Convert hex key to integer
- Read files in binary mode
- XOR each byte with key
- Write output in binary mode
- Print:
- Mode
- Key
- Input size
- First 16 output bytes (hex)

## Testing
Verify:
- Encryption works
- Decryption restores original file
- Files match using comparison tools

## Report Requirements
Include:
- Source code
- Screenshots
- Verification evidence
- Explanation of XOR symmetry

---

# Task 2 — Break XOR (Brute Force)

## Goal
Recover plaintext encrypted with single-byte XOR.

## Steps
1. Inspect ciphertext
2. Write script to test all 256 keys
3. Score candidate plaintext outputs
4. Identify correct key
5. Save recovered plaintext
6. Verify output readability

## Scoring Ideas
- Printable ASCII detection
- Common English words
- Character frequency

## Report Requirements
Include:
- Recovered key
- Plaintext
- Screenshots
- Explanation of scoring logic

---

# Task 3 — Image Header Attack

## Goal
Recover XOR key using predictable PNG header.

PNG header:
```

89 50 4E 47 0D 0A 1A 0A

```

## Steps
1. Inspect encrypted image
2. XOR first byte with PNG header
3. Recover key
4. Decrypt full file
5. Verify image opens

## Report Requirements
Include:
- Key recovery explanation
- Verification screenshots
- Explanation of known-plaintext attack

---

# Task 4 — Two-Time Pad Attack

## Goal
Exploit reuse of XOR key across messages.

## Steps
1. XOR both ciphertext files
2. Observe plaintext XOR result
3. Use crib dragging with common words
4. Recover plaintext segments

## Report Requirements
Include:
- Recovered segments
- Method reasoning
- Explanation of key reuse weakness

---

# Submission Requirements
Submit **one group PDF report** including:

- Explanations for all tasks
- Screenshots
- Recovered keys and plaintext
- Python code
- Validation evidence

All steps must be reproducible.

---

# Grading Overview (100 pts)

| Task | Points |
|------|--------|
| XOR Tool | 20 |
| Brute Force Attack | 25 |
| Image Header Attack | 20 |
| Two-Time Pad Attack | 25 |
| Report Quality | 10 |

---

# Key Lessons
- XOR is reversible.
- Small key spaces are weak.
- Known plaintext leaks keys.
- Key reuse destroys security.
```

---

If you'd like, next I can generate:

✅ Report template
✅ Script templates
✅ Screenshot checklist
✅ Submission checklist
✅ Team workflow doc
✅ Git repo structure

Just tell me what you want next.
