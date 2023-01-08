gaji = int(input("gaji : "))

if gaji >=10000000 :
    pajak = gaji * (2/100)
    potong = gaji - pajak
    print("wajib pajak")
    print("gaji",potong)   
    golongan = input("pns atau non pns\n")
    if golongan == "pns" :
        pajak = gaji * (2/100 + 3/100) 
        hasil = gaji - pajak
        print("gaji ",hasil)
    elif golongan == "non pns" :
        print("gaji ",potong)
elif gaji >=20000000 :
    pajak = gaji * (5/100)
    potong = gaji - pajak
    print("wajib pajak")
    print("gaji",potong)
    golongan = input("pns atau non pns\n")
    if golongan == "pns" :
        pajak = potong * (5/100 + 3/100)
        hasil = potong - pajak
        print("gaji ",hasil)
    elif golongan == "non pns" :
        print("gaji ",potong)
else:
    print("gaji ",gaji)
    print("tidak ada potongan")