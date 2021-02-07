import time
import os
from function_ import *
from multiprocessing import Process


if __name__ == "__main__":
    start_time = time.time()
    p1 = Process(target=print_cube, args=(num,))
    p2 = Process(target=print_square, args=(num,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    duration = time.time() - start_time
    print(f"Duration {duration} seconds")