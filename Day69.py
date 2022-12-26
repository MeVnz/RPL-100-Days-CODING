i = True
while(i):
    opsi = input("Tambah mhs? y/n ")
    print("===============")
    if(opsi == "y"):
        nama = input("Nama mhs: ")
        nim = int(input("Nim mhs: "))
        angkatan = int(input("Angkatan: "))
        print("===============")
    elif(opsi == "n"):
        i = False