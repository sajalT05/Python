# remove ith character from string

def removecharacter(string,n):
    return string[:n-1]+string[n:]

# test
print(removecharacter("golgappa",2))