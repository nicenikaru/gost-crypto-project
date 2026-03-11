import os

os.makedirs("transactions", exist_ok=True)

for i in range(5):
    data = os.urandom(200)
    if i == 2:
        fio = b'Gulidov Nikita'
        data = fio + data[len(fio):]
    with open(f"transactions/tx{i+1}.bin", "wb") as f:
        f.write(data)

print("Файлы tx1.bin — tx5.bin сгенерированы.")
