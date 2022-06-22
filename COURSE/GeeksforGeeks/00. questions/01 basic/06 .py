# check an armstrong number

number1=153
number2=1634

# find order of number
def order(x):
    # order
    n=0
    while x!=0:
        n+=1
        x=x//10
    return n

# power of individual integer in a number
def power(x,y):
    if y==0:
        return 1
    else:
        return x**y


# check if number is armstrong
def armstrong(x):
    # save order
    n=order(x)
    # save number temporarily
    temp=x
    # sum variable
    sum=0
    # find sum of power of individual integer in a number
    while temp!=0:
        sum+=power(temp%10,n)
        temp=temp//10

    # if sum is equal to number, return true
    return(sum==x)

# check created functions
# print(order(25356365)) # working
# print(power(2,2)) # working

print(armstrong(number1))
print(armstrong(number2))

