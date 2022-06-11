'''
Problem Statement
1. book a ticket
2. get fare information
3. get status (no. of seats) 
'''

# create a class
# class --> train
class Train():
    # create methods
    # constructor
    def __init__(self,name,fare,seats):
        # name of train
        self.name=name
        # fare of train
        self.fare=fare
        # seats available
        self.seats=seats
    # print train status
    def getTrainStatus(self):
        print(f"'{self.name}' train has {self.seats} seats availabe. Fare is {self.fare}")
    # book tickets
    def bookTicket(self):
        # check seats availability
        if (self.seats>0):
            # show booking confirmation
            print(f"Your ticket has been booked in {self.name}. Enjoy your ride.")
            # when ticket is booked, decrease total seats available
            # reduce available seats number by 1
            self.seats-=1 
        else:
            print("No seats available, please try later.")
    



# create an instance
# object --> rajdhani
# assign train instance to train class
# assign arguments to the rajdhani objects
rajdhani=Train("Agast Kranti Rajdhani",5000,2)
# call functions related to the train class
    # train status
rajdhani.getTrainStatus()
    # seat booking --> booking 1
rajdhani.bookTicket()
    # show train sttaus again after first ticket booking
rajdhani.getTrainStatus()
    # again book a ticket --> booking 2
rajdhani.bookTicket()
    # show train sttaus again after first ticket booking
rajdhani.getTrainStatus()