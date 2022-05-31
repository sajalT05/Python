matrix=[[0, 1, 2, 3, 4],
                [0, 1, 2, 3, 4],
                [0, 1, 2, 3, 4],
                [0, 1, 2, 3, 4],
                [0, 1, 2, 3, 4]]
print("matrix, nested list: ", matrix)

# for loop
flat_matrix=[]
for sublist in matrix:
    for value in sublist:
        flat_matrix.append(value)
print("flat matrix: ", flat_matrix)

# comprehension
# sublist order is importants
flat_matrix_comprehension_sublist=[value for sublist in matrix for value in sublist]
print("flat matrix comprehension, sublist order: ", flat_matrix_comprehension_sublist)
# value order is not important
flat_matrix_comprehension_value=[value for value in sublist for sublist in matrix]
print("flat matrix comprehension, no order: ", flat_matrix_comprehension_value)