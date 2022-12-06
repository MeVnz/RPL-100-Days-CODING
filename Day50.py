angka = []
b = 0

p = int(input("Masukkan banyak angka: "))
for i in range(p):
    print("Masukkan angka ke-",i+1)
    angka.append(int(input()))
print()

min_angka = angka[0]
for a in range(p):
    if(angka[i] < min_angka):
        min_angka = angka[i]

print('Angka terkecil adalah:', min_angka);
