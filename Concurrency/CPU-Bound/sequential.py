from threading import main_thread
import time
import os
from function_ import sum_


if __name__ == "__main__":
    numbers = [1000 + i for i in range(30)]
    t1 = time.time()
    for number in numbers:
        sum_(number)
    print('Sequential:',time.time() - t1)