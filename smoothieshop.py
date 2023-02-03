## This is probably broken, but the logic is there. 

## Could prolly set this up into an array 



print("Welcome to the Smoothie Shop!")
print("Type X to exit the shop")

code = input("Enter the option you wish to order. (E.g., S1): ")

file = open('smoothiemenu.txt',)

totalCost = 0
while(code!="X"):
    for line in file:
        data = line.split(';')
        itemCode = data[0]
        itemDescription = data[1]
        itemPrice = float(data[2])
        if itemCode == code:
            print(itemCode + ' - ' + itemDescription + ' - $' + str(itemPrice))
            totalCost = totalCost + itemPrice
            code = input('Enter another code or press X to exit. ')

print('The total cost of your order: $' + str(totalCost))
print('Enjoy your smoothies!')
file.close()


