import re

with open("pair_xor.bin","rb") as f:
    x = f.read()

cribs = [
    b" message ",
    b" plaintext ",
    b" stream cipher ",
    b" key reuse ",
    b" two-time pad ",
    b" encryption ",
    b" security ",
    b" attack ",
    b" reused ",
    b" reused key ",
]

def looks_ok(bs: bytes) -> bool:
    try:
        s = bs.decode("ascii")
    except:
        return False
    return re.fullmatch(r"[A-Za-z0-9 ,.'!?-]+", s) is not None

def not_mostly_zero(seg: bytes) -> bool:
    zeros = sum(b == 0 for b in seg)
    return zeros < len(seg) * 0.5

START = 8

for crib in cribs:
    L = len(crib)
    for off in range(START, len(x) - L + 1):
        seg = x[off:off+L]
        if not_mostly_zero(seg):
            other = bytes([seg[i] ^ crib[i] for i in range(L)])
            if looks_ok(other):
                print(f"offset={off:02d}\tcrib={crib.decode('ascii','ignore')!r}\t-> {other.decode('ascii','ignore')!r}")

