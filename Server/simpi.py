from multiprocessing.dummy import Array
import time

from numpy import array

class Option:
    def __init__(self) -> None:
        pass

    def waitUntil(self, signals, idx):
        signals[idx] = True
        while(signals[idx]):
            print(f"Simpi is waiting signal")
            time.sleep(1)

    def sleep(self, min:int):
        time.sleep(min)

def simpiProcess(data, signals):
    
    option = Option()

    # option.waitUntil(signals, 0)

    for i in range(data):
        print(f"Simpi is running: {i}, Signals: {signals[0]}")
        option.sleep(1)


