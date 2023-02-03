def funaverage(funlist):
    total = 0.0
    for item in funlist:
        total += item

    return total / len(funlist)


testlist = [1,2,23.5,0,3,14]
print("Your average is.... %.3f" % funaverage(testlist))