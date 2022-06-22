def GCM_substrcation(a,b):
    '''find GCD (Greatest Common Divisor) or HCF (Highest Common Factor)
    1. if one of the number is 0, return another numbre as GCD.
    2. if both numbers are same, return any on number.
    3. continue checking and substraction, till factors are found.
    e.g. 
    GCD of 20 and 28 is 4 and GCD of 98 and 56 is 14. 
        a=98 & b=56  a>b so put a= a-b and b is  remain same so  a=98-56=42  & b= 56.
        Now b>a  so  b=b-a and  a is same b= 56-42 = 14 & a= 42.
        42 is  3 times of 14  so HCF is 14.
    '''
    if (a==0):
        return b
    if (b==0):
        return a
    if (a==b):
        return a
    if (a>b):
        return GCM_substrcation(a-b,b)
    return GCM_substrcation(a,b-a)

def GCM_division(a,b):
    '''find GCD (Greatest Common Divisor) or HCF (Highest Common Factor)
    1. if one of the number is 0, return another numbre as GCD.
    2. if both numbers are same, return any on number.
    3. continue checking and division, till factors are found.
    e.g. 
    GCD of 20 and 28 is 4 and GCD of 98 and 56 is 14. 
        a=98 & b=56  a>b so put a= a-b and b is  remain same so  a=98-56=42  & b= 56.
        Now b>a  so  b=b-a and  a is same b= 56-42 = 14 & a= 42.
        42 is  3 times of 14  so HCF is 14.
    '''
    if (a==0):
        return b
    if (b==0):
        return a
    if (a==b):
        return a
    if (a>b):
        return GCM_substrcation(a%b,b)
    return GCM_substrcation(a,b%a)    

a=256
b=56

print("GCM with substraction method,",GCM_substrcation(a,b)) 
print("GCM with division method,",GCM_division(a,b))

'''
LCM(a,b)= [a*b] / GCD(a,b)
'''

def LCM(a,b):
    return (a*b)//GCM_division(a,b)

print(f"LCM of {a} and {b} is, {LCM(a,b)}")