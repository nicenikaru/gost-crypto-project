# block_miner.py
from block_header import mine_block
import os

# Вставь сюда Merkle root из вывода merkle_demo.py
merkle_root = bytes.fromhex("e93969d919f919e919793969092929d92969e939791979e9391919290929c579")

prev_hash = os.urandom(32)
header, digest, nonce = mine_block(prev_hash, merkle_root, difficulty_bits=5)

print("Header nonce:", nonce)
print("Header hash:", digest.hex())
