def hitung_bmi(berat,tinggi):
    bmi = berat / (tinggi*tinggi)  

    if (bmi <17.0):
        print("Kurus, kekurangan berat badan berat")
    elif (bmi >17 and bmi <18.4):
        print("kurus, kekurangan berat badan ringan")
    elif (bmi >18.5 and bmi <25.0):
        print("normal")
    elif (bmi >25.1 and bmi <27.0):
        print("gemuk, kelebihan berat badan tingkat ringan")
    elif (bmi >27):
        print("gemuk, kelebihan berat badan tingkat berat")

hitung_bmi(52,1.65)