a = [[2,13,24],
     [20,11,23],
     [34,26,10]]
print(a)

jumlah = 0
for item in a:
    for j in item:
        jumlah += j
print ("Rata-rata :",jumlah)