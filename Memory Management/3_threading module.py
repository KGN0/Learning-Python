'''This module is the high level implementation of threading in python and the standard for managing multithreaded applications. 
It provides a wide range of features when compared to the thread module.'''
# Threading functions

# activeCount()
'''Returns the count of Thread objects which are still alive'''
# currentThread()
'''Returns the current object of the Thread class'''
# enumerate()
'''Lists all active Thread objects'''
# isDaemon()
'''Returns true if the thread is a daemon'''
# isAlive()
'''Returns true if the thread is still alive'''

# Thread class methods
# start()
'''Starts the activity of a thread. It must be called only once for each thread because it will throw a runtime error if called multiple times'''
# run()
'''This method denotes the activity of a thread and can be overridden by a class that extends are Thread class'''
# join()
'''It blocks the execution of other code until the thread on which the join() method was called gets terminated'''
# getName()
'''The getName() method returns the name of a thread'''
# setName()
'''The setName() method sets the name of a thread'''

# starting a Thread
'''To start a separate thread, you create a Thread instance and then tell it to .start() '''
import logging
import threading
import time
def thread_function(name):
    logging.info("Thread %s: finishing", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format = format, level = logging.INFO, datefmt = "%H:%M:%S")
    logging.info("Main : before creating thread")
    x = threading.Thread(target = thread_function, args=(1,))
    logging.info("Main : before running thread")
    x.start()
    logging.info("Main : wait for the thread to finish")
    x.join()
    logging.info("Main : all done")