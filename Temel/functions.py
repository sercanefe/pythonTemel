# def ile fonksiyon tanımlıyoruz:
# fonksiyon adınını yazdığımızda defin altındaki kod blokları çalışır 
# değişiklik yapılacak olduğunda sadece defin altını değiştiririz
# fonksiyonun yanındaki parantezde parametreler vardır, burada argüman der
# parametrenin yanındaki eşittir, ve eşittirin solundaki yazı eğer parametre gelmezse kullanılacak parametredir

#%%
print("-----")
sehir = "Ankara"
sonuc = sehir.upper()  #tüm harfleri büyük yapar 
print(sehir)
print(sehir.endswith("e")) # fonksiyonda belirttiğiniz son harfi, kelimenin son harfi olup olmadığına bakar (true, false)

#%%
print("-----")
def selamVer(isim = "Dostum"): 
    print("Merhaba " + isim)

kullanici = input("Adınız? : ")

selamVer(str(kullanici)) 

#%%
print("-----")
def dikUcgenAlaniHesapla(a,b):
    return a*b/2

alan = dikUcgenAlaniHesapla(2,3)
print(alan)

#%%
print("-----")
dikUcgenAlaniHesapla2 = lambda a,b : a*b/2 # lambda, defin tek satırlık halini sağlar
print(dikUcgenAlaniHesapla2(3,6))
print(type(dikUcgenAlaniHesapla2))

x = dikUcgenAlaniHesapla2 # burada bir değişkene fonksiyonu atayabileceğimiz gösteriliyor
print(type(x))
print(x(4,5))