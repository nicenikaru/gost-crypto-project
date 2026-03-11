import os
from schnorr_signature import keygen, sign, verify
from gost_hash import gost_hash_256
from prng import prng

TRANSACTION_DIR = "transactions"
SEED = b"Gulidov Nikita".ljust(64, b'\x00')

def main():
    print("Генерация ключей Шнорра...")
    x, P = keygen(SEED)
    print(f"Секретный ключ x: {hex(x)}")
    print(f"Открытый ключ P: {hex(P)}\n")

    files = sorted(f for f in os.listdir(TRANSACTION_DIR) if f.endswith(".bin"))
    prns = prng(SEED, len(files) + 2)

    for i, fname in enumerate(files):
        with open(os.path.join(TRANSACTION_DIR, fname), "rb") as f:
            message = f.read()
        r_bytes = prns[i + 1]
        R, s = sign(message, x, r_bytes, P)
        valid = verify(message, R, s, P)

        print(f"{fname}:")
        print(f"  R = {hex(R)}")
        print(f"  s = {hex(s)}")
        print(f"  verify = {'OK' if valid else 'FAIL'}\n")

if __name__ == "__main__":
    main()
