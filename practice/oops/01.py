# storing infomration of programmers working at microsoft
# creating programmers class
class Programmers:
    # class attribute
    # all programmers are working at microsoft
    # company is default
    company="Microsoft"
    # methods
    # constrcutor
    # take arguments
    # name and department are attributes/parameters, where information will be stored
    def __init__(self,name,department):
        # programmer name
        self.name=name
        # programmer department
        self.department=department
    # print programmer details
    def getProgrammer(self):
        # usign prorgammer name and department
        print(f"{self.name} department is {self.department}")

# create sajal object with programmer class
sajal=Programmers("Sajal Tiwari", "GitHub")
# sajal name is sajal tiwari
# sajal department is github
sajal.getProgrammer()


