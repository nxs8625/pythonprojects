clubs = []
members = []

# design a function that takes input and adds to the lists
def clurb():
    clubname = input('What is your club name? ')
    memcount = int(input('How many members are in ' + clubname ))
    clubs.append(clubname)
    members.append(memcount)
# design a function that loops through all clubs and nicely prints their membership count

def printclurb():
    for c,m in zip(clubs,members):
        print('Your club is %s and has %d members' % (c,m))

clurb()
clurb()
printclurb()