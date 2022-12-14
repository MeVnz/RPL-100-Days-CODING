j1 = float(input("Memulai telepon: "))
j2 = float(input("akhir telepon: "))
j = j2 - j1

pulsa = 3665
biayaPulsa = 150

jam = pulsa//3600*j
x = pulsa % 3600*j
menit = x // 60*j
detik = x % 60*j
biaya = j * biayaPulsa

print(jam,"jam",menit,"menit",detik,"detik")
print("Total bayar:",j*jam)

n = int(input("angka: "))
for i in range(n,1):
    
    if(n <= i):
        print(i,end=" ")
    else:
        print(i,"+",end=' ')