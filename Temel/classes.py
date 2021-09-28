# -*- coding: utf-8 -*-

# classlar alakalı fonksiyonları gruplamak için kullanılır
# classların adı büyük ile başlar (küçük başlarsa hata olmaz ama yazım düzni açısından büyük tercih edilir)
# oop'de (nesne yönelimli kodlama) kullanılır

class Matematik:
    def topla(self,sayi1,sayi2):
        return sayi1 + sayi2
    
    def cikar(self,sayi1,sayi2):
        return sayi1 - sayi2
    
    def carp(self,sayi1,sayi2):
        return sayi1 * sayi2

    def bol(self,sayi1,sayi2):
        return sayi1 / sayi2
    
matematik = Matematik() 

print(type(matematik))
print("Toplam = " + str(matematik.topla(31,69))