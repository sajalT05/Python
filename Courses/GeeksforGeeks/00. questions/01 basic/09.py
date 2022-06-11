# nth fibonacci number

def fibonacci(number):
    match number:
        case 0:
            return None
        case 1:
            return 0
        case 2:
            return 1
        case default:
            return fibonacci(number-1) + fibonacci(number-2)
    
# call
print(fibonacci(4))
        

