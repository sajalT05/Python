# cube of first n natural numbers

def cubenaturalnumbers(x):
    sum=0
    for i in range(x+1):
        sum+=i**3
    print(sum)

# call
cubenaturalnumbers(5)