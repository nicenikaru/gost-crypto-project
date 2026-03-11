from gost_hash import gost_hash_256

def merkle_root(hashes: list[bytes]) -> bytes:
    if len(hashes) == 0:
        return b"\x00" * 32

    while len(hashes) > 1:
        if len(hashes) % 2 != 0:
            hashes.append(hashes[-1])
        new_level = []
        for i in range(0, len(hashes), 2):
            combined = hashes[i] + hashes[i+1]
            new_level.append(gost_hash_256(combined))
        hashes = new_level
    return hashes[0]
