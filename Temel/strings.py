#substring
mesaj = "Merhaba D�nya"
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
print(mesaj.replace("�","u")) # gecici degisti
# mesaj = mesaj.replace("�","u") # kal�c� de�i�ti

# split ve strip fonksiyonlar�
bilgi = "Engin Demiro� 33 Ankara"
print(len(bilgi.split()))
print(len(bilgi))
print(bilgi.split()[2])
print("Ad� = " + bilgi.split()[0])
print("Soyad� = " + bilgi.split()[1])
print("Ya�� = " + bilgi.split()[2])
print("�ehri = " + bilgi.split()[3])

print(" ")
print(bilgi.strip())

# input
ad = input("Ad�n�z? = ")
sayi1 = input("Say� 1? = ")
sayi2 = input("Say� 2? = ")
print(int(sayi1)+int(sayi2))