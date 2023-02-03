pets = ['cat','fluffers','snake']

search = input('Which pet did you miss the most while you were away? ')
petfound = False

for ind, p in enumerate(pets):
    if p.find(search) != -1:
        print('That is the one. Found at index %d' % ind)
        petfound = True
        break
        
if petfound == False:
    print('You do not own this pet. Sorry')