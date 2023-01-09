hp = input("Merk hp yang dibeli\n")
harga = int(input("Harga Hp = "))
menu = input("masukkan kode promo\n")
if hp == "oppo" :
    if menu == "DISKONOPPO":
        print("Kode diskon benar")
        potong = harga * 40/100
        total = harga - potong
        print("Harga dipotong 40% = ",total)
elif menu == "DISKONVIVO":
    print("Kode diskon benar")
    potong = harga * 45/100
    total = harga - potong
    print("Harga dipotong 45% = ",total)
elif menu == "DISKONXIAOMI":
    print("Kode diskon benar")
    potong = harga * 60/100
    total = harga - potong
    print("Harga dipotong 60% = ",total)
else:
    print("total harga = ",harga)
    print("Kode salah")