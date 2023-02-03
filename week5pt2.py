#we are writing this code to search for a partial terms in lists

inventory = ['watch','ipad','iphone']

search = input('Which product are you looking for? ')
foundit = False
for ind, i in enumerate(inventory):
    if i.find(search) != -1:
        print('Found it at index %d' % ind)
        foundit = True
        break

if foundit == False:
    print('I did not find it!')
