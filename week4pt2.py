employeenames = []
employeeiq = []

def add_one():
    name = input('What is your name? ')
    iq = int(input('What is the IQ that you wish to enter? '))
    employeesnames.append(name)
    employeeiq.append(iq)

def printadd_one():
    for n,i in zip(employeenames,employeeiq):
        print('Your name is %s and \n')
        print('Your IQ is %d' % (n,i))

add_one()
add_one()
printadd_one()

