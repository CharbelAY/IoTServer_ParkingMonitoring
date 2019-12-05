from threading import Thread
import time
from threading import Thread

def f1():
    print("f1")

def f2():
    print("f2")

    
t1 = Thread(target=f1)
t2 = Thread(target=f2)
t1.start()
t2.start()