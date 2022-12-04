angka = []
b = 0

p = int(input("Masukkan banyak angka: "))
for i in range(p):
    angka_baru = int(input("Masukkan angka: ".format(b)))
    angka.append(angka_baru)

print(angka)
