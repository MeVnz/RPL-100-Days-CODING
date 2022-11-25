total_belanja = int(input("total belanja anda = "))
hari = input("masukkan hari : ")
if hari == "senin" :
    diskon = 1/100
    
    potongan = total_belanja * diskon
    totalnya = total_belanja - potongan
    print("total harga = ", totalnya)
elif hari == "selasa" :
    diskon = 2/100
  
    potongan = total_belanja * diskon
    totalnya = total_belanja - potongan
    print("total harga = ", totalnya)
elif hari == "rabu" :
    diskon = 3/100
  
    potongan = total_belanja * diskon
    totalnya = total_belanja - potongan
    print("total harga = ", totalnya)
elif hari == "kamis" :
    diskon = 4/100
  
    potongan = total_belanja * diskon
    totalnya = total_belanja - potongan
    print("total harga = ", totalnya)
elif hari == "jum'at" :
    diskon = 5/100
   
    potongan = total_belanja * diskon
    totalnya = total_belanja - potongan
    print("total harga = ", totalnya)
elif hari == "sabtu" :
    diskon = 6/100
    
    potongan = total_belanja * diskon
    totalnya = total_belanja - potongan
    print("total harga = ", totalnya)
elif hari == "minggu" :
    diskon = 7/100
    
    potongan = total_belanja * diskon
    totalnya = total_belanja - potongan
    print("total harga = ", totalnya)
else: 
    print("tidak mendapatkan diskon")