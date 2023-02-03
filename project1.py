import getpass
#import module to get password and hide it 

class client:
    pen1 = 0
    pen2 = 0
    pen3 = 0

    def __init__(self, usr, passw):
        self.username = usr
        self.password = passw

    def print_invoice(self):

        global pen1_price
        global pen2_price
        global pen3_price


        exempt = input("Are you tax exempt? " )
        if exempt == "Yes" or exempt == "yes" or exempt == "y":
            total = (self.pen1 * pen1_exemptPrice) + (self.pen2 * pen2_exemptPrice) + (self.pen3 * pen3_exemptPrice)
            print(f'User: {self.getuser()}\n'
               f'# of Mechanical Pens: {self.pen1}\n'
               f'# of Mechanical Pens With Inscriptions: {self.pen2}\n'
               f'# of Wingback X Lei Melendres Pens: {self.pen3}\n'
               f'Total Cost: ' '${:,.2f}'.format(total))
        else:
            total = (self.pen1 * pen1_price) + (self.pen2 * pen2_price) + (self.pen3 * pen3_price)
            print(f'User: {self.getuser()}\n'
               f'# of Mechanical Pens: {self.pen1}\n'
               f'# of Mechanical Pens With Inscriptions: {self.pen2}\n'
               f'# of Wingback X Lei Melendres Pens: {self.pen3}\n'
               f'Total Cost: ' '${:,.2f}'.format(total))


    def getuser(self):
        return self.username

    def getpass(self):
        return self.password

    def addpen1(self, quan):
        self.pen1 = self.pen1 + quan

    def addpen2(self, quan):
        self.pen2 = self.pen2 + quan

    def addpen3(self, quan):
        self.pen3 = self.pen3 + quan




client_list = [client("", ""), client("", "")]
#list to hold the clients
pen1_exemptPrice = 95 - (.08 * 95)
pen2_exemptPrice = 105 - (.08 * 105)
pen3_exemptPrice = 120 - (.08 * 120)
#when tax exempt this price is applied to the order
pen1_price = 95
pen2_price = 105
pen3_price = 120
#pen prices defined
class Accounts:
    #class for all accounts made in the program
    def create(self):
        print("Please enter these fields...")
        username = input("Username: ")
        password = ""
        while True:
            password = getpass.getpass("Password: ")
            password = getpass.getpass("Password (again): ")
#using password from module and verifying the password
            print()

            if password != password:
                print("Please enter matching passwords.\n")
                #if the passwords do not match it will ask to reenter the same password
            else:
                break
#it will break if incorrect
        print("Account created succesfully!\nYou may now login.\n")
        acc = client(username, password)
        client_list.append(acc)

    def isValidAccount(self, acc):
        return any(
            acc.getuser() == account.getuser() and acc.getpass() == account.getpass()
            for account in client_list
        )

    def login(self):
        print("Enter your credentials...")
        while True:
            username = input("Username: ")
            password = getpass.getpass("Password: ")

            acc = client(username, password)

            print()

            if self.isValidAccount(acc):
                print("Login successful!\n")
                print(f"Welcome {username}!")
                return acc
            else:
                print(
                    "Login error: Incorrect username/password.\n\nPlease try again..."
                )
#the user input will keep being prompted until the correct information is input just as a safeguard

def main():

    print("Welcome!\n")

    curr_user = ""

    while True:
        option = input("Please select an option:\n[1] Login\n[2] Create an account\n> ")
        print()
        if option == "1":
            curr_user = Accounts().login()
            break
        if option == "2":
            Accounts().create()
            curr_user = Accounts().login()
            break
        else:
            print(f"Invalid option: {option}\nTry again...\n")
#the loop is going infinitely until the user inputs the correct information
    while True:
        pen = input(
            "Order a Pen: Mechanical (M), Mechanical with Inscription (MI), or Wingback X Lei Melendres (W). "
            "\nPress I for an invoice or L to logout: "
        )
        #options for pens able to order
        print()
        if pen.lower() == "m" or pen.lower() == "mi" or pen.lower() == "w":
            quan = input("How many would you like? ")
            if pen.lower() == "m":
                curr_user.addpen1(int(quan))
            if pen.lower() == "mi":
                curr_user.addpen2(int(quan))
            if pen.lower() == "w":
                curr_user.addpen3(int(quan))
        elif pen.lower() == "i":
            curr_user.print_invoice()

        elif pen.lower() == "l":
            break
        else:
            print("Invalid Input")
#this print function and everything inside of it allows the user to enter lowercase inputs and still accept the input
#except for asking to print the invoice
        print()


main()
