menu = {'Mango', 'Strawberry', 'Blueberry'
}

def get_order():
    current_order = []
    while True:
        print("What kind of smoothie can I get for you?")
        order = input()
        if order in menu:
            current_order.append(order)
        else:
            print("Sorry, that choice isn't currently on our menu right now.")



def is_order_complete():
    print('Can I get you anything else? Yes/No')
    choice = input()
    if choice == "no" or "No":
        return True
    elif choice == "yes" or "Yes":
        return False
    else:
        raise Exception("invalid input")

def main():
    order = get_order()

if __name__ == "__main__":
    main()