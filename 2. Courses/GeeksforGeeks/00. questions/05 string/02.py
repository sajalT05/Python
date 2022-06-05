# check a string is palindrome and symnetric

def checkstring(string):
    if string[::-1]==string:
        print("palindrome")
    else:
        print("not palindrome")
    if(len(string)%2==0):
        if string[:len(string)//2]==string[len(string)//2:]:
            print("symnetric")
        else:
            print("not symnetric")

# test
checkstring("khokho")