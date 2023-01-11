print("[1].iPhone\n[2].Xiaomi\n[3].Realme")
hp = int(input("Merk hp : "))
if hp == 1:
    print("[1].iPhone 13 pro max\nRp25.000.000\n[2].iPhone 12 pro max\nRp18.000.000")
    menu = int(input("Type hp : "))
    if menu == 1:
        member = input("Kartu member/Tidak\n")
        if member == "kartu member":
            print("mendapatkan diskon 5%")
            harga = 5/100 
            diskon = input("kode diskon : ")
            if diskon == "diskonnatal" :
                print("mendapatkan diskon 5%")
                harga = 25000000 * (5/100+harga)
                potong = 25000000 - harga
                print("total harga = ",potong)
            elif diskon == "diskonlebaran" :
                print("mendapatkan diskon 10%")
                harga = 25000000 * (10/100+harga)
                potong = 25000000 - harga
                print("total harga = ",potong)
            elif diskon == "diskonakhirtahun" :
                print("mendapatkan diskon 20%")
                harga = 25000000 * (20/100+harga)
                potong = 25000000 - harga
                print("total harga = ",potong)
        elif member == "tidak":
            diskon = input("kode diskon : ")
            if diskon == "diskonnatal" :
                print("mendapatkan diskon 5%")
                harga = 25000000 * 5/100
                potong = 25000000 - harga
                print("total harga = ",potong)
            elif diskon == "diskonlebaran" :
                print("mendapatkan diskon 10%")
                harga = 25000000 * 10/100
                potong = 25000000 - harga
                print("total harga = ",potong)
            elif diskon == "diskonakhirtahun" :
                print("mendapatkan diskon 20%")
                harga = 25000000 * 20/100
                potong = 25000000 - harga
                print("total harga = ",potong)
    elif menu == 2:
        member = input("Kartu member/Tidak\n")
        if member == "kartu member":
            print("mendapatkan diskon 5%")
            harga = 5/100 
            diskon = input("kode diskon : ")
            if diskon == "diskonnatal" :
                print("mendapatkan diskon 5%")
                harga = 18000000 * (5/100+harga)
                potong = 18000000 - harga
                print("total harga = ",potong)
            elif diskon == "diskonlebaran" :
                print("mendapatkan diskon 10%")
                harga = 25000000 * (10/100+harga)
                potong = 25000000 - harga
                print("total harga = ",potong)
            elif diskon == "diskonakhirtahun" :
                print("mendapatkan diskon 20%")
                harga = 25000000 * (20/100+harga)
                potong = 25000000 - harga
                print("total harga = ",potong)
        elif member == "tidak":
            diskon = input("kode diskon : ")
            if diskon == "diskonnatal" :
                print("mendapatkan diskon 5%")
                harga = 25000000 * 5/100
                potong = 25000000 - harga
                print("total harga = ",potong)
            elif diskon == "diskonlebaran" :
                print("mendapatkan diskon 10%")
                harga = 25000000 * 10/100
                potong = 25000000 - harga
                print("total harga = ",potong)
            elif diskon == "diskonakhirtahun" :
                print("mendapatkan diskon 20%")
                harga = 25000000 * 20/100
                potong = 25000000 - harga
                print("total harga = ",potong)
elif hp == 2:
     print("[1].Pocophon F3\nRp4.500.000\n[2].Pocophon F3 Pro\nRp5.500.000")
     menu = int(input("Type hp : "))
     if menu == 1:
        member = input("Kartu member/Tidak\n")
        if member == "kartu member":
            print("mendapatkan diskon 5%")
            harga = 5/100 
            diskon = input("kode diskon : ")
            if diskon == "diskonnatal" :
                print("mendapatkan diskon 5%")
                harga = 4500000 * (5/100+harga)
                potong = 4500000 - harga
                print("total harga = ",potong)
            elif diskon == "diskonlebaran" :
                print("mendapatkan diskon 10%")
                harga = 4500000 * (10/100+harga)
                potong = 4500000 - harga
                print("total harga = ",potong)
            elif diskon == "diskonakhirtahun" :
                print("mendapatkan diskon 20%")
                harga = 4500000 * (20/100+harga)
                potong = 4500000 - harga
                print("total harga = ",potong)
        elif member == "tidak":
            diskon = input("kode diskon : ")
            if diskon == "diskonnatal" :
                print("mendapatkan diskon 5%")
                harga = 4500000 * 5/100
                potong = 4500000 - harga
                print("total harga = ",potong)
            elif diskon == "diskonlebaran" :
                print("mendapatkan diskon 10%")
                harga = 4500000 * 10/100
                potong = 4500000 - harga
                print("total harga = ",potong)
            elif diskon == "diskonakhirtahun" :
                print("mendapatkan diskon 20%")
                harga = 4500000 * 20/100
                potong = 4500000 - harga
                print("total harga = ",potong)
     elif menu == 2:
        member = input("Kartu member/Tidak\n")
        if member == "kartu member":
            print("mendapatkan diskon 5%")
            harga = 5/100 
            diskon = input("kode diskon : ")
            if diskon == "diskonnatal" :
                print("mendapatkan diskon 5%")
                harga = 5500000 * (5/100+harga)
                potong = 5500000 - harga
                print("total harga = ",potong)
            elif diskon == "diskonlebaran" :
                print("mendapatkan diskon 10%")
                harga = 5500000 * (10/100+harga)
                potong = 5500000 - harga
                print("total harga = ",potong)
            elif diskon == "diskonakhirtahun" :
                print("mendapatkan diskon 20%")
                harga = 5500000 * (20/100+harga)
                potong = 5500000 - harga
                print("total harga = ",potong)
        elif member == "tidak":
            diskon = input("kode diskon : ")
            if diskon == "diskonnatal" :
                print("mendapatkan diskon 5%")
                harga = 5500000 * 5/100
                potong = 5500000 - harga
                print("total harga = ",potong)
            elif diskon == "diskonlebaran" :
                print("mendapatkan diskon 10%")
                harga = 5500000 * 10/100
                potong = 5500000 - harga
                print("total harga = ",potong)
            elif diskon == "diskonakhirtahun" :
                print("mendapatkan diskon 20%")
                harga = 5500000 * 20/100
                potong = 5500000 - harga
                print("total harga = ",potong)
