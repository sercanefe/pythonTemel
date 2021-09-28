 # -*- coding: utf-8 -*-

sozluk = {
    "book" : "kitap",
    "table" : "masa",
    }

sozluk2 = dict(kitap = "book", masa = "table")

print(sozluk2)

print(" ")
print(sozluk)
print(sozluk["table"])
sozluk["book"] = "kitap 1" # value değiştirir
sozluk["pencil"] = "kalem" # yeni key ekler
print(sozluk)
print(len(sozluk)) # sözlüğün uzunluğunu belirtir
