import time
import os
from function_ import *
from multiprocessing import Process, process


if __name__ == "__main__":
    start_time = time.time()
    

    processes = []

    for i in range(5): 
        p1 = Process(target=load_, args=(path,))
        p2 = Process(target=save_, args=(data,))
        processes.append(p1)
        processes.append(p2)
    
    for p in processes:
        p.start()

    for p in processes:
        p.join()

    duration = time.time() - start_time
    print(f"Duration {duration} seconds")