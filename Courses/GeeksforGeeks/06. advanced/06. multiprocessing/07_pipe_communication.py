# two endpoints

import multiprocessing as mp

def sender(conn,msg):
    conn.send(msg)
    print("sender:",conn.recv())