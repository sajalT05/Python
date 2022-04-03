# break --> stops further loop iterations

'''
Loop statements may have an else clause; 
    it is executed when the loop terminates through 
    a. exhaustion of the iterable (with for) or 
    b. when the condition becomes false (with while), 
    c. but not when the loop is terminated by a break statement. 
'''
# break is used to break the program loop at first successfull iteration
for i in range(2,10):
    if i%5==0:
        print(f"{i} is divisible by 5")
        break

'''
When used with a loop, 
    the else clause has more in common with the else clause of a 
    try statement than it does with that of if statements: 

a try statement’s else clause runs when no exception occurs, 
    and a loop’s else clause runs when no break occurs. 
'''

# continue --> move on to the next iteration of the loop
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)