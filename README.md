# Lab 2 — Modular Arithmetic and XOR-Based Encryption

**Course:** CSCI 4407 — Security & Cryptography
**Group:** 10

## Overview

This lab explores XOR encryption and how improper usage leads to cryptographic failures. We build an XOR tool, then break XOR encryption through brute force, known-plaintext attacks, and two-time pad exploitation.

## Environment

- **VM:** Kali Linux (latest rolling release)
- **Python:** 3.x (pre-installed on Kali)
- **Required tools:** `xxd`, `hexdump`, `file` (all pre-installed on Kali)

### Kali VM Setup

1. Download Kali Linux VM image from https://www.kali.org/get-kali/#kali-virtual-machines
2. Import into VirtualBox or VMware
3. Boot and log in (default creds: `kali` / `kali`)
4. Clone this repo:
   ```bash
   git clone <repo-url>
   cd CSCI_4407
   ```

## Project Structure

```
CSCI_4407/
├── README.md
├── Lab2_Instructions_short.md
├── Archive/
│   └── Group_10/              # Provided ciphertext files
│       ├── xor_chal_text.bin  # Task 2: single-byte XOR encrypted text
│       ├── xor_chal_image.bin # Task 3: XOR encrypted PNG image
│       ├── xor_pair_1.bin     # Task 4: ciphertext 1 (reused key)
│       └── xor_pair_2.bin     # Task 4: ciphertext 2 (reused key)
├── scripts/
│   ├── xor_tool.py            # Task 1: XOR encrypt/decrypt tool
│   ├── brute_force.py         # Task 2: brute force single-byte XOR
│   ├── png_header_attack.py   # Task 3: recover key via PNG header
│   └── two_time_pad.py        # Task 4: two-time pad / crib dragging
└── output/                    # Decrypted files go here
```

## Tasks

### Task 1 — XOR Tool (20 pts)
Build a Python tool that encrypts/decrypts files using XOR.

```bash
python3 scripts/xor_tool.py encrypt <input> <output> <hex_key>
python3 scripts/xor_tool.py decrypt <input> <output> <hex_key>
```

### Task 2 — Brute Force Attack (25 pts)
Break single-byte XOR encryption by trying all 256 keys.

```bash
python3 scripts/brute_force.py Archive/Group_10/xor_chal_text.bin
```

### Task 3 — PNG Header Attack (20 pts)
Recover the XOR key using the known PNG file header (`89 50 4E 47 0D 0A 1A 0A`).

```bash
python3 scripts/png_header_attack.py Archive/Group_10/xor_chal_image.bin output/recovered.png
```

### Task 4 — Two-Time Pad Attack (25 pts)
Exploit key reuse across two ciphertexts using crib dragging.

```bash
python3 scripts/two_time_pad.py Archive/Group_10/xor_pair_1.bin Archive/Group_10/xor_pair_2.bin
```

## Submission

One group PDF report with:
- Source code for all tasks
- Screenshots of execution
- Recovered keys and plaintext
- Explanations of each attack
