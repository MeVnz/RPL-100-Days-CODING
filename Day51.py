angka = []
b = 0

p = int(input("Masukkan banyak angka: "))
for i in range(p):
    print("Masukkan angka ke-", i)
    angka.append(int(input()))

a = (int(input("Masukkan nilai yang anda cari: ")))

if (a == angka[i]):
    nilai = a
    print("Angka yang anda cari: ", nilai)
else:
    print("Angka tidak ada")
