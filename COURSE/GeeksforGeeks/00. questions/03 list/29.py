# sum of number digits in list

list=[1,2,3,4,5,6,7,8,9,10,'a','afsd','656']

def sumlistintegers(list):
    sum=0
    for i in list:
        if type(i)==int:
            sum=sum+i
    return sum

print(sumlistintegers(list))