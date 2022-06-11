"""
create matrix   
                [[0, 1, 2, 3, 4],
                [0, 1, 2, 3, 4],
                [0, 1, 2, 3, 4],
                [0, 1, 2, 3, 4],
                [0, 1, 2, 3, 4]]
"""
# for loops
# simple
matrix_for_loop=[]
for i in range (5):
    matrix_for_loop.append([])
    for j in range (5):
        matrix_for_loop[i].append(j)
print("matrix using for loop:", matrix_for_loop)
# arithmetic
matrix_arithmetic=[]
for i in range (5):
    matrix_arithmetic.append([])
    for j in range (5):
        matrix_arithmetic[i].append(i*j)
print("matrix using for loop using arithmetics:", matrix_arithmetic)
# condition
matrix_condition=[]
for i in range (5):
    matrix_condition.append([])
    for j in range (10):
        if i%2==0:
            matrix_condition[i].append(j)
print("matrix using for loop using conditions:", matrix_condition)



# ṇested list comprehension
# simple
matrix_comprehension=[[j for j in range(5)] for i in range(5)]
print("matrix using nested list comprehension:", matrix_comprehension)
# arithmetics
matrix_arithmetic_comprehension=[[i*j for j in range(5)] for i in range(5)]
print("matrix using nested list comprehension using arithmetics:", matrix_arithmetic_comprehension)
# condition
matrix_condition_comprehension=[[j for j in range(2,5) if i%2==0] for i in range(5)]
print("matrix using nested list comprehension using conditions:", matrix_condition_comprehension)
