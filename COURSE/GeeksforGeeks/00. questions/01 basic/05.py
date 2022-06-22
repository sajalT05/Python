# formula for compund interest

def compoundInterest(principal,interest,time):
    amount=principal*(1+(interest/100))**time
    print(amount)

# call
compoundInterest(100,5,5)