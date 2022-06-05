# count matching pairs in string

from collections import Counter

def countpairs(string):
    pairs=Counter(string.split())
    # print(pairs)
    for word,counter in pairs.items():
        if counter>1:
            print(word)

# test
countpairs("this is my name my name sajal is")