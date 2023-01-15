a = int(input("Masukkan nilai a: "))
b = int(input("Masukkan nilai b: "))

for i in range(a, b+1):
    if i % 2 != 0:
        print(i)
for j in range(b, a+1):
    if j % 2 != 0:
        print(j)