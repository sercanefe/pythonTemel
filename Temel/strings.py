#substring
mesaj = "Merhaba Dünya"
print(mesaj[2:5])

yeniMesaj = mesaj[12:13]
print(yeniMesaj)

#len = length
print(len(mesaj))

yeniMesaj2 = mesaj[len(mesaj)-1:len(mesaj)]
print(yeniMesaj2)

# lower upper
print(mesaj.upper())
print(mesaj.lower())

# replace fonksiyonu
print(mesaj.replace("ü","u")) # gecici degisti
# mesaj = mesaj.replace("ü","u") # kalıcı değişti

# split ve strip fonksiyonları
bilgi = "Engin Demiroğ 33 Ankara"
print(len(bilgi.split()))
print(len(bilgi))
print(bilgi.split()[2])
print("Adı = " + bilgi.split()[0])
print("Soyadı = " + bilgi.split()[1])
print("Yaşı = " + bilgi.split()[2])
print("Şehri = " + bilgi.split()[3])

print(" ")
print(bilgi.strip())

# input
ad = input("Adınız? = ")
sayi1 = input("Sayı 1? = ")
sayi2 = input("Sayı 2? = ")
print(int(sayi1)+int(sayi2))