# ogrenci1 = "engin"
# ogrenci2 = "derin"
# ogrenci3 = "salih"

# print(ogrenci1)
# print(ogrenci2)
# print(ogrenci3)
# yerine şunu yap

ogrenciler = ["engin","derin","salih"]
print(ogrenciler)

ogrenciler.append("ahmet") # ekler
print(ogrenciler)

ogrenciler.remove("derin") # çikarir
print(ogrenciler)

ogrenciler[0] = "veli" # değiştirir

# list constructor
sehirler = list(("ankara","i̇stanbul","ankara")) # liste tanimlar
print(sehirler)

print(len(sehirler)) # uzunluğunu yazar

# diğer fonksiyonlar
# print(sehirler.clear())

print("ankara sayisi = " + str(sehirler.count("ankara"))) # kaç tane olduğunu yazar

print("ankara indexi = " + str(sehirler.index("ankara"))) # kaçinci sirada olduğunu yazar (ayni değişkeni ilk gördüğü yerde birakir)

sehirler.pop(1) # indexe göre çikarir
sehirler.insert(0,"i̇stanbul") # indexe göre ekler

print(sehirler)

sehirler.reverse() # terse çevirir"
print(sehirler)

# diziler referans tiptir

sehirler3 = sehirler.copy()
sehirler2 = sehirler # ikisi de bellekte ayni yere çikar, yukaridaki copyi kullan kopyalamak için
sehirler2[0] = "i̇zmir"
print(sehirler2)
print(sehirler)
print(sehirler3)

sehirler.extend(sehirler3) # elimizdeki iki listeyi (dizi) birleştiriyoruz
print("birleşmiş şehirler = " + str(sehirler))

sehirler.sort() # alfabetik ya da sayisal olarak siralar
sehirler.reverse()
print(sehirler)