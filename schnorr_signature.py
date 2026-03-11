# schnorr_signature.py
from prng import prng
from gost_hash import gost_hash_256

p = 30803
q = 15401
g = 2


def H(data: bytes) -> int:
    e = int.from_bytes(gost_hash_256(data), 'big') % q
    if e == 0:
        e = 1
    return e

def keygen(prng_seed: bytes):
    rand = prng(prng_seed, 2)
    x = int.from_bytes(rand[0], 'big') % q
    if x == 0:
        x = 1
    P = pow(g, x, p)
    return x, P

def sign(message: bytes, x: int, r_bytes: bytes, P: int):
    r = int.from_bytes(r_bytes, 'big') % q
    R = pow(g, r, p)
    R_bytes = R.to_bytes((R.bit_length() + 7) // 8, 'big').rjust(64, b'\x00')
    P_bytes = P.to_bytes((P.bit_length() + 7) // 8, 'big').rjust(64, b'\x00')
    e = H(R_bytes + P_bytes + message)
    print("[sign] e:", e)
    print("[sign] R:", hex(R))
    print("[sign] P:", hex(P))
    print("[sign] s:", hex((r + e * x) % q))
    s = (r + e * x) % q
    return (R, s)

def verify(message: bytes, R: int, s: int, P: int):
    R_bytes = R.to_bytes((R.bit_length() + 7) // 8, 'big').rjust(64, b'\x00')
    P_bytes = P.to_bytes((P.bit_length() + 7) // 8, 'big').rjust(64, b'\x00')
    e = H(R_bytes + P_bytes + message)
    lhs = pow(g, s, p)
    rhs = (R * pow(P, e, p)) % p
    print("[verify] e:", e)
    print("[verify] lhs:", lhs)
    print("[verify] rhs:", rhs)
    return lhs == rhs
