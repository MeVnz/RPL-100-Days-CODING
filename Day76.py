gaji = int(input("Input gaji: "))
pekerjaan = input("Input pekerjaan: ")
if(gaji >= 5000000):
    pajak = 10/100 * gaji
    hasil = gaji - pajak
    print(f"Total gaji non pns:{hasil}")
    if(pekerjaan == "pns"):
        x = 5/100 * hasil
        y = hasil - x
        print(f"Total gaji pns:{y}")
elif(gaji >= 3000000 and gaji <= 5000000):
    pajak = 5/100 * gaji
    hasil = gaji - pajak
    print(f"Total gaji non pns:{hasil}")
    if(pekerjaan == "pns"):
        x = 5/100 * hasil
        y = hasil - x
        print(f"Total gaji pns:{y}")
else:
    print("Total Gaji: ",gaji)
