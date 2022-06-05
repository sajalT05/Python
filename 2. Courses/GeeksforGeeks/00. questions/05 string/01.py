# check a string is palindrome

def palindrome(string):
    reversestring=string[::-1]
    return reversestring==string

# test
print(palindrome("manam"))