# input_name=input("What is your name? ")
# print("Good Afternoon,", input_name)

from unicodedata import name

# strftime()
# formatting date and time
# takes one parameter, format, to specify the format of the returned string


letter='''
Dear <name>,
Congratulations, you are selected.
Regards,

Date: <date>'''


name=input("Your name: ")
letter=letter.replace("<name>", name)
date=input("Today's date: ")
letter=letter.replace("<date>", date)

print(letter)


