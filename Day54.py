n = int(input('Input panjang elemen: '))
a = []
b = []
for j in range(n):
    a.append(int(input()))
print(a)
for i in reversed(a):
    b.append(i)
print(b)
