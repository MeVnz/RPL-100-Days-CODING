hobi = []
i = 0
hobi_baru = input("masukkan hobi: ".format(i))
hobi.append(hobi_baru)
print("Kamu memiliki {} hobi".format(len(hobi)))
for hb in hobi:
    print ("- {}".format(hb))