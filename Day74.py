luasTanah = int(input("Luas Tanah: "))
permeter = 300000
x = luasTanah * permeter
if(x >= 100000000):
    pajak = 0.05
    total = x - pajak
    print("Uang bersih: ",total)
elif(x >= 50000000 and x < 100000000):
    pajak = 0.03
    total = x - pajak
    print("Uang bersih: ",total)
elif(x < 50000000):
    pajak = 0.01
    total = x - pajak
    print("Uang bersih: ",total)