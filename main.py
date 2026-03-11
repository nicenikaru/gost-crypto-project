from prng import prng
from gost_hash import gost_hash_256

def main():
    print("--- Хэш от 'Gulidov Nikita' ---")
    message = b"Gulidov Nikita"
    digest = gost_hash_256(message)
    print("Digest:", digest.hex())

    print("\n--- Генерация псевдослучайных чисел ---")
    seed = message.ljust(64, b'\x00')
    numbers = prng(seed, 5)
    for i, num in enumerate(numbers):
        print(f"PRN[{i}] = {num.hex()}")

if __name__ == "__main__":
    main()



    
"""from gost_hash import gost_hash_256

msg = b'test message'
h1 = gost_hash_256(msg)
h2 = gost_hash_256(msg)

print("H1 =", h1.hex())
print("H2 =", h2.hex())
print("Equal:", h1 == h2)
"""