# check all vowel

from sqlalchemy import false


def checkvowel(string):
    vowels=['a','e','i','o','u']
    # print(vowel)
    updatedstring=string.lower().strip().replace(" ","")
    # print(updatedstring)
    for vowel in vowels:
        if string.find(vowel)==0:
            return False
        else:
            return True



# test
print(checkvowel("hjhh ggjjk "))
# checkvowel("hjhh ggjjk aeiou")
