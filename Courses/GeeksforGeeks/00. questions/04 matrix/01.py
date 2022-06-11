# add two matrices

matrix1=[[1,2,3],[4,5,6],[7,8,9]]
matrix2=[[9,8,7],[6,5,4],[3,2,1]]

ziplistsum=[map(sum,zip(*t)) for t in zip(matrix1,matrix2)]
print(ziplistsum)