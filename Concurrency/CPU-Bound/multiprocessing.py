import multiprocessing

import time
import os
from function_ import sum_

if __name__ == '__main__':
    numbers = [1000 + i for i in range(30)]
    t1 = time.time()
    for number in numbers:
        p = multiprocessing.Process(target=sum_, args=(number,))
        p.start()
    print('Sequential:',time.time() - t1)
