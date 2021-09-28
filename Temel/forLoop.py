# for döngüsü (alt alta yazmak içi kullanılır)
# break o şartı sağladığında döngüyü durdurur
# continue o şart sağlandığında sadece o şart için döngünün gerekliliklerini sağlamaz ve diğer şeyler için devam eder

#%% for döngüsü
sehirler = ["Ankara", "İstanbul", "İzmir", "Antalya"]

for sehir in sehirler:
    if sehir != "İstanbul":
        print(sehir + " için kod = " + sehir[0:2])
    elif sehir == "Ankara":
        print(sehir + " için kod = " + sehir[0:3])

print("  ")

#%% break continue 
ToyotaCars = list(("Corolla", "Yaris", "CHR", "Auris", "Hilux"))

for toyotaCar in ToyotaCars:
    if toyotaCar == "Hilux":
        break
    print("Araba Adı = " + "Toyota " + toyotaCar)
    print("*******")
    
    if toyotaCar == "CHR":
        print("Araba Adı = " + "Toyota " + "CHR" + " = " + "Sold Out")
        continue 
    
#%% for range
for x in range(50):
    print(x+1)
    
#%% for range bi yerden bi yere kadar istenen artışta saydırma örnek

for y in range(-2,20,2):
    print(y + 2)