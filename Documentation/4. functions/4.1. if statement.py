# ask input from user, convert string number input into aninteger
x = int(input("Please enter an integer: "))
# check input is > 0
if x < 0:
    # if input > 0 , print 'Negative changed to zero'
    x = 0
    print('Negative changed to zero')
# check input is equal to 0
elif x == 0:
    # if input is = 0, print 'Zero'
    print('Zero')
# check if input is =1
elif x == 1:
    # if input is =1, print 'Single'
    print('Single')
# if no condition is matched
else:
    # print 'More'
    print('More')