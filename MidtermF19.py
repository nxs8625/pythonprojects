import statistics

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
# The product of my choice for this part of the midterm is SuterSubs
    def displayproduct(self, name, price):
        print('The price for %s is.. %d.' % name, price)
    def computeavg(productprice):
        return sum(productprice) /  len(productprice)

supersub = Product('SuperSub', 3)
minisub = Product('MiniSub', 2)
special = Product('Special', 4.5)

productlist = ['SuperSub', 'MiniSub', 'Special']



productprice = [2, 3, 4.5]

computeavg = statistics.mean(productprice)

#printing the average of the prices

print('The average price of the subs is...$', round(computeavg, 2))

for product in productlist:
    print('The prices for the products in %s are $ %s' % (productlist, productprice ))    






