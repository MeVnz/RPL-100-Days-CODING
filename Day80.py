modal = int(input("Modal Awal: "))
lamaInvest = int(input("Lama Investasi: "))
total = 0
for i in range(lamaInvest):
    i+=1
    untung = modal * 0.05
    x = untung + modal
    total += x
    print(f"Keuntungan di tahun ke-{i}: {total}")