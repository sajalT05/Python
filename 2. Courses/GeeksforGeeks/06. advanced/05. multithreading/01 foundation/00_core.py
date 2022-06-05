import threading as t

def cube(num):
    print(num**3)

def square(num):
    print(num**2)

if __name__=="__main__":
    thread1=t.Thread(target=cube,args=(10,))
    thread2=t.Thread(target=square,args=(10,))

    # start thread
    thread1.start()
    thread2.start()

    # wait untill thread is done
    thread1.join()
    thread2.join()

    # thread completed
    print("Done!")
