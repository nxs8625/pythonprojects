password =  input("Please enter your password. ")

print("The length of your password is...{0}".format(str(len(password))))

if (password == password.lower ()):
    print ("The password is all lowercase.")
else:
    print ("The password is not all lowercase.")
