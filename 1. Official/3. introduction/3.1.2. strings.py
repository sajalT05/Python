# single quotes
print('single "quotes')
# double quotes
print("double 'quotes")
# triple quotes
print('''triple'
"quotes''')
# triple double quotes
print("""triple'
"quotes""")
# new line
print("new line")
print("\n")
# escaping quotes
print('''escaping\'  \"quotes''')

# raw strings --> print (\)
print(r"C:\file\location\backslash\working")

# f strings --> print dynamic variable in strings
variable=65
print(f"\n\nvariable value is, {variable}.\n\n")

# concatenation
print("hello"+"name") #spaces not present
print("hello""name") #spaces not present
print("hello","name") #spaces present
print(3*"hello",2*"name") # mutliple strings
text_variable="hello"
print(text_variable+"name")

# long strings
text=('this is my name,'
'so please note my name.')
print(text)

# operations on string
text="radheshyam"
# indexing
print(text[0]) # first element/character of string
print(text[-1]) # last element/character of string
# slicing
print(text[0:2]) # forward --> lower index position included, higher exluded
print(text[-3:-1]) # backward --> lower index position included, higher exluded
print(text[2:-1]) # forward+backward --> lower index position included, higher exluded
# length of string
print(len(text))