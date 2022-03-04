#
# String: Datatype in python
# String is an Array of characters

# print strings
# single line print
print("Namstey") 
print("")
# multiple line print
print('''I'm a happy man. 
Will you be my friend''') 
# escape sequence characters
'''
\n new line
\t tab space
\' singlw quote
\\ backlash
'''
print("this is first line\nthis is second line in a new line \t this is third line after a tab")
print('''
\' this is a single quote
\\ this is backlash
''')

string1='name"sa' #single quotes # use when double quotes are  in string
string2="name's" #double quotes #use when single quotes are in string
string3='''name's"s''' #triple quotes #use when single and double quotes are used in string
story="my name is Sajal Tiwari. I'm a very happy person. Will you be my friend?"

print(string1+string2+string3) #adding strings
string_combination=string1+string2+string3 #adding strings and defining a variable

#print datatype of string
print(type(string1))

# length of string is total number of characters in a string
# first position is 0
# print charcater of a string at a specifiic position
# position from beginning --> 0,1,2,3,4,...,n
# position from end --> -1,-2,-3,...,-n
# 
print(string1[0],string1[1],string1[2],string1[3],string1[4]) #print charcaters at position
# string slicing #getting a part of a string
# print characters in a position range 
# from beginning 
# positive indices
print(string1[1:4])  # 1 to 4 --> second to fifth
print(string1[0:]) # 0 to end --> first to last
print(string1[:4]) # starting to 4 --> first to fifth
# from end 
# negative indices
print(string1[-4:-1]) # last fourth to last
print(string1[:-1]) # starting to last
print(string1[-5:]) # last fifth to last

# slicing with skip value
# skip characters while slicing in a string
# first value is the starting position for slicing
# second value is the ending positing for slicing
# third value is the command to skip charcater at that consecutive and alternate position
print(string1[0::1]) #starting from first position and ending at last position --> skip at first position
print(string1[0::2]) #starting from first position and ending at last position --> skip at second position
print(string1[::1]) #starting from first position and ending at last position --> skip at first position
print(string1[1:4:2]) #starting from second position and ending at fifth position --> skip at second position

# length of a string --> print(len(stringname))
print(len(story))

# check string or characters in a string --> print(stringname.endswith("character_string"))
# returns true or false
# boolean
print(story.endswith("s"))

# count charcaters occurence in a string --> print(stringname.count("character_string"))
print(story.count("a"))

# capitalize first position character in a string --> print(stringname.capitalize("character_string"))
print(story.capitalize())

# find occurence of a string or a character in a string --> print(stringname.find("character_string"))
# returns position of the checking charcater or checking string in a string
print(story.find("is"))

# replace a character or string in a string 
# --> print(stringname.replace("character_string", "new_character_string"))
print(story.replace("happy","strong"))

