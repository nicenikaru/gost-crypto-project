from gost_hash import gost_hash_256

def prng(seed: bytes, count: int = 10) -> list[bytes]:
    if len(seed) != 64:
        raise ValueError("Seed должен быть 64 байта (512 бит)")

    numbers = []
    h0 = gost_hash_256(seed)
    numbers.append(h0)

    for i in range(1, count):
        i_bytes = i.to_bytes(32, 'big')
        input_block = h0 + i_bytes
        hi = gost_hash_256(input_block)
        numbers.append(hi)

    return numbers
