'''
A thread is the smallest unit of a program or process executed independently or scheduled by the Operating System
Multithreading is a threading technique in python programming to run multiple threads concurrently by rapidly switching between threads
with a CPU help (called context switching)

Use or threads
- Parallel computation
- standardization
- parallel I/O (Input/Output)
- asynchronus events
There are two main modules to handle threads in python
- _thread module
- threading module

Syntax: thread.start_new_thread(function_name, args[, kwargs])'''
# Example
import _thread
import time
def cal_sqre(num):
    print("Calculate the square root of the given number")
    for n in num:
        time.sleep(1.3)
    print('Square i:', n * n)
def cal_cube(num):
    print("Calculate the cube of the given number")
    for n in num:
        time.sleep(1.3)
    print('Cube is:', n * n * n)
arr = [4, 5, 8 ,3]
t1 = time.time()
cal_sqre(arr)
cal_cube(arr)
print('Total time taken by threads is:', time.time()-t1)

# Example
import time
import threading
class myThread(threading.Thread):
    def __init__(self, threadID):
        super().__init__()
        self.threadID = threadID
    def run(self):
        for x in range(1, 5):
            print("Thread ID:", self.threadID)
            time.sleep(1)
t1 = myThread(1)
t1.start()
t1 = myThread(2)
t1.start()
t1 = myThread(3)
t1.start()
t1 = myThread(4)
t1.start()