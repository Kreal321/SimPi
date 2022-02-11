from multiprocessing.dummy import Array
import time

from numpy import array

class Option:
    def __init__(self) -> None:
        pass

    def suspend(self):
        while(True):
            time.sleep(1)
    
    def resume(self):
        pass

    def sleep(self, min:int):
        time.sleep(min)

def simpiProcess(data, signals):
    
    option = Option()

    for i in range(data):
        print(f"Simpi is running: {i}, Signals: {signals[0]}")
        option.sleep(1)

