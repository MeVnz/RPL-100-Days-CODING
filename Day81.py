number = []
angka = int(input("Input panjang list = "))

for i in range(0, angka):
    i+=1
    number.append(i)
print(number)
print("========")
while (i > 0):
    i-=1
    print(number[i])