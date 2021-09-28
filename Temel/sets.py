studentsSet = {"Engin","Derin","Salih","Ahmet"} # setler süslü parantezle yapılır
# studentsSet2 = set("ali","mehmet") #  başka bir set oluşturma yolu
print(studentsSet)

print(" ")

print(type(studentsSet)) # setin türünü öğrenir

print(" ")

for student in studentsSet: # alt alta sıralar
    print(student)

print(" ")

print("Derin" in studentsSet) # sette varsa true, yoksa false der

print(" ")

if "derin"  in studentsSet: #  sette varsa yoksa if else şeyi
    print("Sette var") 
    
else:
    print("Sette yok")
    
print(" ")    
    
studentsSet.add("Ali") # sete başka bişi ekler
print(studentsSet)

print(" ")

studentsSet.update(["Merve","Mert","Selin"]) # sete bunları ekler
print(studentsSet)

print(" ")

print(len(studentsSet)) # sette kaç şey olduğunu gösterir

print(" ")

studentsSet.remove("Selin") # söylenen veriyi siler
print(len(studentsSet))

print(" ")

studentsSet.discard("Selin") # aynı veri bi daha remove ile silinirse error verir diye discard ile silinir
print(len(studentsSet))

print(" ")

print(studentsSet)

print(" ")

x = studentsSet.pop() # son değişkeni siler ama set olduğu için random siler (algoritmasına göre son)
print(studentsSet)

print(" ")

# studentsSet.clear() #setin içindekileri siler
# print(len(studentsSet))
# print(studentsSet)

# del studentsSet # seti direkt siler
# print(studentsSet)