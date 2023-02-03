import getpass
#password hider for users
m1 = 0
m2 = 0
m3 = 0
class Model:
    def __init__(self, name, color, stock, price):
        self.name = name
        self.color = color
        self.stock = stock
        self.price = price

    # Car string format: "%Color %Name x%Stock"for %Price
    def __repr__(self):
        stock = "%-3d" % (self.stock)
        return f"{self.color} {self.name} x{stock} for {self.price}"

# class for storage of each of the models that are available
class Warehouse:
    def __init__(self):
        self.models = {'M3': Model('Model 3','Black',20, 35000), 'MS': Model('Model S','Black',20, 75000), 'MX': Model('Model X','Black',20, 81000)}
    # parameters for the models that are being used for the system
    def __repr__(self):
        return "\n".join(map(str, self.models))
    def addinventory(self, model, stock):
        self.models[model].stock = self.models[model].stock + stock
        return 'Added Sucessfully!'
    def removeinventory(self, model, stock):
        if self.models[model].stock - stock < 0:
            return 'Could not remove! There is no existing stock.'
        self.models[model].stock = self.models[model].stock - stock
        return 'Removed Successfully! You have removed %d models.'

    def print_invoice(self,user):
        model1 = self.models['M3']
        model2 = self.models['MS']
        model3 = self.models['MX']
        global m1
        global m2
        global m3
        #variables defined for the invoice and totals for the remove (purchases) from the user
        total = (m1 * model1.price) + (m2 * model2.price) + (m3 * model3.price)
        print(f'User: {user}\n'
            f'# of Model 3: {m1}\n'
            f'# of Model S: {m2}\n'
            f'# of Model X: {m3}\n'
            f'Total Cost: {total}')
# class for the user to create login information
class client:

    WH = Warehouse() 

    def __init__(self, usr, passw):
        self.username = usr
        self.password = passw
    
    def getuser(self):
        return self.username

    def getpass(self):
        return self.password
    
    def addmodel1(self, quan):
        if self.WH.removeinventory('M3', int(quan)) == 'Could not remove! There is no existing stock.':
            return
        global m1
        m1 += quan

    def addmodel2(self, quan):
        if self.WH.removeinventory('MS', int(quan)) == 'Could not remove! There is no existing stock.':
            return
        global m2
        m2 += quan

    def addmodel3(self, quan):
        if self.WH.removeinventory('MX', int(quan)) == 'Could not remove! There is no existing stock.':
            return
        global m3
        m3 += quan

client_list = [client("",""), client("","")]
#class for the user's account information to be stored as the system is being used
class Accounts:
    def create(self):
        print("Please enter these fields...")
        username = input("Username: ")
        password = ""
        while True:
            password = getpass.getpass("Password: ")
            _password = getpass.getpass("Password (again): ")

            print()

            if password != _password:
                print("Please enter matching passwords.\n")
            else:
                break

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


def main():

    print("Welcome!\n")

    curr_user = ''


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
           
    while True:
        mode = input("Press A to add items back, R to remove items, I for Invoice or L to Logout: "
        )
        if mode.lower() == "l":
            break
        if mode.lower() == "i":
            curr_user.WH.print_invoice(curr_user.getuser())
            continue
        if not (mode.lower() == 'i' or mode.lower() == 'l' or mode.lower() == 'a' or mode.lower() == 'r'):
            print('Invalid Input')
            continue
        model = input(
            "Pick a Model: Model 3 (M3), Model S (MS), or Model X (MX). "
        )
        if not (model.lower() == 'm3' or model.lower() == 'ms' or model.lower() == 'mx'):
            continue
        
        print()
        if mode.lower() == 'r' or mode.upper() == 'R':
            quan = input("How many would you like? ")
            if model.lower() == "m3":
                curr_user.addmodel1(int(quan))
            if model.lower() == "ms":
                curr_user.addmodel2(int(quan))
            if model.lower() == "mx":
                curr_user.addmodel3(int(quan))
        elif mode.lower() == 'a' or mode.upper()== 'A':
            Type = model.lower()
            quan = input("How many would you like? ")
            if Type == 'm3':
                curr_user.WH.addinventory('M3', int(quan))
            if Type == 'ms':
                curr_user.WH.addinventory('MS', int(quan))
            if Type == 'mx':
                curr_user.WH.addinventory('MX', int(quan)) 
        print(curr_user.WH.models)

main()

# main function where that defines what is accepted from the user for the system to go through its processes