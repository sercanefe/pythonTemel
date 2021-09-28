# asallar = [2,3,5,7,11,13]

sayi = int(input("Sayı Giriniz :  "))
asalMi = True

for girilenSayi in range(2,sayi):
    if sayi % girilenSayi == 0:
        asalMi = False
        break
    
if asalMi == True:
    print("Bu sayı asaldır")
else:
    print("Bu sayı asal değildir")
    
    
