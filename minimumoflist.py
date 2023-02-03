def calcmin(alist):
    min = 10120101010101001
    for item in alist:
        if item < min:
            min = item
    return min

findminlist = [2,4,45,23,0,-3,555,33.33]
print(calcmin(findminlist))