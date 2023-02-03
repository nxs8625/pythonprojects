class City:

    def __init__(self,namep,popup):
        self.name = namep
        self.population = popup
        self.buildinglist = []

    def addBuilding(self,newbuildingp):
        self.buildinglist.append(newbuildingp)

    def map(self):
        print("The buildings in %s are..." % self.name)
        for building in self.buildinglist:
            building.display()

    def countFloors(self):
        total = 0
        for b in self.buildinglist:
            total += b.floors
        return(total)

    def howManyBuildings(self):
        return len(self.buildinglist)

class Skyscraper:
    #class variables
    numSkyscrapers = 0

    #constructor
    # does instantiation
    def __init__(self,floorsp,namep):
        self.floors = floorsp
        self.name = namep
        self.location = "Rochester, NY"
        #self.architect = "Frank Lloyd Wright"
        Skyscraper.numSkyscrapers += 1


    def addfloors(self,howmanyp):
        self.floors += howmanyp # adrian answer: int(input("how many floors to add"))

    def removefloors(self):
        self.floors -= 10


    def remodel(self):
        print("Construction underway")

    def demolish(self):
        print("bye bye")


    def display(self):
        print("The %s has %d floors" % (self.name,self.floors))
    
    @classmethod
    def worldSkyscraperCount(cls):
        return cls.numSkyscrapers

#############################################################################

c1 = City("Chicago",2700000)

# make a new instance of a skyscraper
skyscraper1 = Skyscraper(100,"Sears Tower")
c1.addBuilding(skyscraper1)
skyscraper2 = Skyscraper(163,"Burj Khalifa")
c1.addBuilding(skyscraper2)

c2 = City('Los Angeles', 4000000)
c2.addBuilding(skyscraper1)
c2.addBuilding(skyscraper2)

skyscraper3 = Skyscraper(200,'Disney World')




print(c1.countFloors())
skyscraper1.addfloors(1)
print(c1.countFloors())

c1.map()

print('The total number of Skyscrapers is... %d' % Skyscraper.numSkyscrapers)
#skyscraper2.display()
#skyscraper1.display()