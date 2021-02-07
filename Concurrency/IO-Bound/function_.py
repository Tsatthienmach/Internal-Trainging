
import os
import time
# import cv2


def load_(path):
    for i in range(10):
        with open(path, 'r') as file:
            data = file.read()   
    print(f'Load Finished')
    print('--> Process ID: ', os.getpid())
 
def save_(data):
    
    for i in range(10):
        with open('saved_file.txt', 'w') as file:
            file.write(data)
    print(f'Save Done')
    print('--> Process ID: ', os.getpid())

path = 'IO-Bound/100MB.txt'
with open(path, 'r') as file:
    data = file.read()
















































































































