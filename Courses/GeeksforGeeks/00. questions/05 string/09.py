# print even length words in a sentence

def evenlengthwords(string):
    stringlist=string.split()
    for items in stringlist:
        if len(items)%2==0:
            print(items)

# test
evenlengthwords("haello my name is sajal tiwari")