#make pet code
petname = input("Please enter pet name (first and last):")
petid = input("Please enter the 9 digit petID number:")

#grab last pet name
petnamelist = petname.split(" ")
petlastname = petnamelist[1]

#grab last four digits
petidlastfour = petid[5:9]

petcode = petlastname + petidlastfour

print("your pet code is.....%s" % petcode)