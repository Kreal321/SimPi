import time

class Option:
    def __init__(self) -> None:
        pass

    def sleep(self, min:int):
        time.sleep(min)

def simpiProcess(data):
    
    option = Option()

    for i in range(data):
        print(f"Simpi is running: {i}")
        option.sleep(1)

