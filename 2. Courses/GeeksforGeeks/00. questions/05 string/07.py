# snake case to pascal case

def changecase(string):
    """
    this_is_snake_case
    ThisisPascalCase
    """
    # replace "_" with spaces" "
    # uppercase all title words
    # replace spaces " " with no spaces "" 
    return string.replace("_"," ").title().replace(" ", "")

# test
print(changecase("pascal_case_testing_done"))