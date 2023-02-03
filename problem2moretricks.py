petlist = ["fluff fluff","swimmy fish","barking dog"]
petages = [12,23,34]

# get the max value from the age list
maxage = max(petages)

# find the slot with the maximum value
maxindex = petages.index(maxage)

# find the name in the slot corresponding to the max age
oldestpet = petlist[maxindex]

print("NOTE: %s is the oldest pet!" % oldestpet)

#trick use the tab character to space things out...
for pet,age in zip(petlist,petages):
    print("PET\t%s\tAGE\t%d:" % (pet,age))

# OR the format function allows you to do this even betrer...
for pet,age in zip(petlist,petages):
    print("{0:<5} {1:<15} {2:<5} {3:<5}".format("PET:", pet, "AGE:",age))


