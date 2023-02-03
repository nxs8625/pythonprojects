mydictionary = {'cutlass':'oldsmobile','pickup':'datsun','celica':'toyota'}

print(mydictionary['celica'])

petionary = {"fluff fluff":12,"swimmy fish":23,"barking dog":34}

print(petionary["swimmy fish"])

petionary2 = {"fluff fluff":(12,"cat"),"swimmy":(23,"fish"),"barking":(34,"dog")}

print(petionary2["swimmy"])

print("barking" in petionary2)
print("frodo" in petionary2)

for pet in petionary2:
    print("%s has age %d" % (pet,petionary2[pet][0]))

for pet in petionary2.items():
    print(pet)
