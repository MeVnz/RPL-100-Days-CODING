gaji = int(input("Input Gaji: "))
anak = int(input("Input jumlah anak: "))
bonus = 0.05
bonusAnak = 0.05
if(gaji >= 5000000):
    if(anak >= 2):
        x = gaji * bonus
        z = x + bonusAnak
        y = gaji + z
        print("Bonus: ",z)
        print("Gaji bersih: ",y)
    else:
        x = gaji * bonus
        y = gaji + x
        print("Bonus: ",x)
        print("Gaji bersih: ",y)
elif(gaji >= 2000000 and gaji < 5000000):
    if(anak >= 2):
        x = gaji * bonus
        z = x + bonusAnak
        y = gaji + z
        print("Bonus: ",z)
        print("Gaji bersih: ",y)
    else:
        x = gaji * bonus
        y = gaji + x
        print("Bonus: ",x)
        print("Gaji bersih: ",y)
else: 
    print("Gaji bersih: ",gaji)