angka = int(input("Masukkan batas angka: "))
x = 0
for i in range(1, angka+1):
    if i % 3 == 0:
      x += 1
print("Jumlah angka yang habis dibagi 3:",x)