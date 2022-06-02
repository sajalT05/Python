# sum of squares of first n natural numbers

def naturalnumberssum(x):
    sum=0
    for i in range(x+1):
        sum+=i**2
    print(sum)

# call
naturalnumberssum(5)