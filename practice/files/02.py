# generate multiplication table from 2 to 20. write it into defferent files.
# place these files in a folder

# create a loop for starting tables from 
for i in range (1,21):
    with open(f"/laboratory/python/python learning/practice/files/10_tables/multiplicationtable_{i}","w") as file:
        for j in range (0,11):
            file.write(f"{i}*{j}={i*j}\n")

