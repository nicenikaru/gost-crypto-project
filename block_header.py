import time
import os
from gost_hash import gost_hash_256

def mine_block(prev_hash: bytes, merkle_root: bytes, difficulty_bits: int = 5):
    assert len(prev_hash) == 32
    assert len(merkle_root) == 32

    block_size = (123456789).to_bytes(4, 'big')
    timestamp = int(time.time()).to_bytes(4, 'big')
    prefix = block_size + prev_hash + merkle_root + timestamp

    target_prefix = b'\x00' * (difficulty_bits // 8)
    max_nonce = 2 ** 32

    for nonce in range(max_nonce):
        nonce_bytes = nonce.to_bytes(4, 'big')
        header = prefix + nonce_bytes
        hash_val = gost_hash_256(header)
        if hash_val.startswith(target_prefix):
            return header, hash_val, nonce

    raise RuntimeError("Не удалось найти подходящий nonce")
