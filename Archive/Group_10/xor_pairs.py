with open("xor_pair_1.bin","rb") as f1, open("xor_pair_2.bin","rb") as f2:
    c1 = f1.read()
    c2 = f2.read()

n = min(len(c1), len(c2))
pair_xor = bytes([c1[i] ^ c2[i] for i in range(n)])

with open("pair_xor.bin","wb") as out:
    out.write(pair_xor)

print("Wrote pair_xor.bin bytes:", n)
