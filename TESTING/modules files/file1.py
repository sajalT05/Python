print(f"file name: {__name__}")

def function1():
    print("function1 --> file1")

if __name__=="__main__":
    print("This is file1 running as main file.")
else:
    print("**This is file1 imported.")

function1()