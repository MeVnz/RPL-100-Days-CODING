saldo = 50000000
pw = int(input("pin anda = "))
if pw == 543221:
    print("[1].Transfer\n[2].Cek Saldo\n[3].Setor Tunai\n[4].Pembayaran")
    menu = int(input("pilih menu "))
    if menu == 1:
        print("[1].BRI\n[2].BCA\n[3].MANDIRI\n[4].BNI")
        bank = int(input("pilih bank "))
        if bank == 1:
            no_rek = int(input("nomor rekening"))
            tf = int(input("nominal transfer"))
            tf = saldo - tf
            print("Transfer berhasil")
            print("sisa saldo =",tf)
        elif bank == 2:
            no_rek = int(input("nomor rekening"))
            tf = int(input("nominal transfer"))
            tf = saldo - tf
            print("Transfer berhasil")
            print("sisa saldo =",tf)
        elif bank == 3:
            no_rek = int(input("nomor rekening"))
            tf = int(input("nominal transfer"))
            tf = saldo - tf
            print("Transfer berhasil")
            print("sisa saldo =",tf)
        elif bank == 4:
            no_rek = int(input("nomor rekening"))
            tf = int(input("nominal transfer"))
            tf = saldo - tf
            print("Transfer berhasil")
            print("sisa saldo =",tf)
        else:
            print("bank tidak termasuk")
    elif menu == 2:
        saldo_anda = saldo
        print("saldo anda =",saldo_anda)
    elif menu == 3:
        setor = int(input("jumlah setoran ="))
        sisa_saldo = saldo + setor
        print("setor berhasil")
        print("Saldo anda",sisa_saldo)
    elif menu == 4:
        print("[1].BRIVA\n[2].TOKEN LISTRIK\n[3].AIR PDAM\n[4].MARKETPLACE")
        bayar = int(input("Pilih metode pembayaran "))
        if bayar == 1:
            va = int(input("nomor VA\n"))
            va = saldo - va
            print("Berhasil")
        elif bayar == 2:
            tl = int(input("nomor token\n"))
            tl = saldo - tl
            print("berhasil")
        elif bayar == 3:
            ap = int(input("nomor air\n"))
            ap = saldo - ap
            print("berhasil")
        elif bayar == 4:
            print("[1].Shopee\n[2].Tokopedia\n[3].Lazada\n[4].Bukalapak")
            mp =  int(input("pilih marketplace "))
            if mp == 1:
                sh = int(input("Nomor Pembelian\n"))
                sh = saldo - sh
                print("Pembayaran Berhasil")
            elif mp == 2:
                tk = int(input("Nomor pembelian"))
                tk = saldo - tk
                print("Pembayaran berhasil")
            elif mp == 3:
                lz = int(input("Nomor pembelian"))
                lz = saldo - lz
                print("Pembayaran berhasil")
            elif mp == 4:
                bl = int(input("Nomor pembelian"))
                bl = saldo - bl
                print("Pembayaran berhasil")
            

else:print("Pin salah")