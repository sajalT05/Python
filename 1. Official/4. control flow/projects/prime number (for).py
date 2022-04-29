# find prime number fom 2 to 100
# iterate through the range 2 to 100(101 as higher limit is excluded) 
for n in range(2,101):
    # iterate through all values of the factor from 2 to the number
    for x in range (2,n):
        # check if the number is divisible by the factor
        # create a condition for checkign remainder
        # if remainder is 0, hence x is the factor of n
        if n%x==0:
            # print that number is non-prime
            # n//x retruns floor division value, only integer value when divided
            print(f"{n} is not a prime number, with factor as {x}*{n//x}")
            # break the loop for factor iterations
            break
    # if for loop(n in range 2,100) iterations are exhausted
    # give a default else statement
    else:
        print(f"{n} is a prime number.")