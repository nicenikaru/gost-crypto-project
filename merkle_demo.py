# merkle_demo.py
from merkle_tree import merkle_root
from gost_hash import gost_hash_256
import os

files = sorted(os.listdir("transactions"))
hashes = []

for name in files:
    with open("transactions/" + name, "rb") as f:
        hashes.append(gost_hash_256(f.read()))

root = merkle_root(hashes)
print("Merkle root:", root.hex())
