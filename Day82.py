pendapatan = int(input("Pendapatan Sales Rp. "))
if(pendapatan == 20000):
    jasa = 10000
    komisi = 0.10 * pendapatan
    total = komisi + jasa
    print("Total: ",total)
elif(pendapatan >= 20000 and pendapatan <=50000):
    jasa = 20000
    komisi = 0.15 * pendapatan
    total = komisi + jasa
    print("Total: ",total)
elif(pendapatan == 20000):
    jasa = 30000
    komisi = 0.20 * pendapatan
    total = komisi + jasa
    print("Total: ",total)