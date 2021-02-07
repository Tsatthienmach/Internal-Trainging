import time
import os
from function_ import *


if __name__ == "__main__":
    start_time = time.time()

    print_cube(num)
    print_square(num)

    duration = time.time() - start_time
    print(f"Duration {duration} seconds")