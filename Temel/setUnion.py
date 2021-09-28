# -*- coding: utf-8 -*-

setA = {1,2,3,4,5}
setB = {1,3,4,6,7,8}


print("setA = " + str(setA))
print("setB = " + str(setB))

print(" ")

print("Set Union yani birleşim")
print(setA | setB)
print(setA.union(setB))
print(setB.union(setA))

print(" ")

print("Set Intersection yani kesişim")
print(setA & setB)
print(setA.intersection(setB))
print(setB.intersection(setA))

print(" ")

print("Set Difference yani a fark b")
print(setA - setB)
print(setA.difference(setB))
print(setB.difference(setA))

print(" ")

print("Symmetric Difference yani (a fark b) + (b fark a)")
print(setA ^ setB)
print(setA.symmetric_difference(setB))
print(setB.symmetric_difference(setA))