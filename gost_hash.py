# gost_hash.py

def xor512(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))

def S(data: bytes) -> bytes:
    return bytes((b + 1) % 256 for b in data)

def P(data: bytes) -> bytes:
    return data[::-1]

def L(data: bytes) -> bytes:
    out = bytearray(64)
    for i in range(64):
        out[i] = data[i] ^ ((i * 13) % 256)
    return bytes(out)

def LPS(data: bytes) -> bytes:
    return L(P(S(data)))

def compress(N: bytes, h: bytes, m: bytes) -> bytes:
    K = xor512(h, N)
    K = LPS(K)
    t = m
    for _ in range(12):
        t = LPS(xor512(K, t))
    return xor512(xor512(t, h), m)

def pad(data: bytes) -> bytes:
    pad_len = 64 - (len(data) % 64)
    return data + b'\x00' * pad_len

def gost_hash_256(message: bytes) -> bytes:
    h = bytes([1] * 64)
    N = b'\x00' * 64
    Sigma = b'\x00' * 64

    message = pad(message)
    for i in range(0, len(message), 64):
        m = message[i:i+64]
        h = compress(N, h, m)
        N = (int.from_bytes(N, 'little') + 512).to_bytes(64, 'little')
        sigma_int = int.from_bytes(Sigma, 'little') + int.from_bytes(m, 'little')
        Sigma = sigma_int.to_bytes((sigma_int.bit_length() + 7) // 8, 'little').ljust(64, b'\x00')

    h = compress(b'\x00' * 64, h, N)
    h = compress(b'\x00' * 64, h, Sigma)
    return h[32:]
