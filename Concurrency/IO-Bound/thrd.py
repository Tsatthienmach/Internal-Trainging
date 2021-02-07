from threading import Thread
import time
import os
from function_ import *


if __name__ == '__main__':
    start_time = time.time()

    threads = []

    for i in range(5): 
        p1 = Thread(target=load_, args=(path,))
        p2 = Thread(target=save_, args=(data,))
        threads.append(p1)
        threads.append(p2)
    
    for t in threads:
        t.start()

    for t in threads:
        t.join()
    
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")