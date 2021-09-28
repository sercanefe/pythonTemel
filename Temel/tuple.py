 # -*- coding: utf-8 -*-

tupleListe = (2,4,6,"Ankara",(3,4,5),[])
liste = [2,4,6,"Ankara",[3,4,5],()]

liste[0] = 6
# tupleListe[0] = 6 # tuplelarda değiştirilemez

tupleDeger = ("Engin",)
print(tupleDeger)

print(tupleListe)
print(type(tupleListe))
print(len(tupleListe))
print(tupleListe[-2])

print(" ")

print(liste)
print(type(liste))
print(len(liste))
print(liste[-2]) 