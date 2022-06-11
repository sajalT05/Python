# check substring in string

def checkstring(string,substring):
    if string.count(substring)>0:
        print("found")
    else:
        print("not found")

# test
checkstring("happy","pos")