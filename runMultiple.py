#!/usr/bin/python
import listener
import os
import time
currentTime = time.time()
while currentTime - time.time() < 600:
    currentTime = time.time()
    counter = 0
    if counter < 2:
        print("running the cloud again")
        os.system('python listener.py')
        print("time is: ", time.time() - currentTime)
        if(time.time() - currentTime > 30):
            os._exit(0)
        counter += 1
