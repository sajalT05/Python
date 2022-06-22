import multiprocessing as mp

def print_records(records):
    """print record(tuples) in records(list)
    """
    for record in records:
        print(f"Name: {record[0]}, Age: {record[1]}")

def insert_record(record,records):
    """
    insert record(tuple) in records(list)
    """
    records.append(record)
    print("new record added!")

if __name__=="__main__":
    with mp.Manager() as manager:
        # create list in serve rprocess memory
        records=manager.list([('John',25),('Mary',30),('Bob',35)])
        # new record to be inserted
        new_record=('Alice',40)

        # create process
        process1=mp.Process(target=print_records,args=(records,))
        process2=mp.Process(target=insert_record,args=(new_record,records))

        # start process
        process1.start()
        process2.start()

        # wait for process to finish
        process1.join()
        process2.join()

        # print result
        print("in main:",records)
