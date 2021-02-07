import time
import os
from function_ import *


if __name__ == "__main__":
    start_time = time.time()
    for i in range(5): 
        load_(path)
        save_(data)
    
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")