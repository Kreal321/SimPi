import time

def optionToString(option):
    optionList = {
        "10": "Start",
        "11": "Click to start",
        "20": "Suspend",
        "21": "Click to spspend",
        "30": "Resume",
        "31": "Click to resume",
        "40": "Stop",
        "41": "Click to stop",
        "51": "Wait until Sensor input high",
        "52": "Wait until Source 2 is On",
        "52": "Wait until click button",
        "61": "Open Source ",
        "62": "Close Source "
    }
    if(option["type"] == "50"):
        return "Wait " + option["data"][0] + " minutes"
    else:
        return optionList[option["type"]] + option["data"][0]
    


class SimpiQ:
    queue = []

    def __init__(self, data) -> None:
        self.queue = data

    def size(self):
        return len(self.queue)

    def next(self):
        return self.queue.pop(0)

    def waitUntil(self, signals, idx):
        signals[idx] = True
        while(signals[idx]):
            print(f"Simpi is waiting signal")
            time.sleep(1)

    def sleep(self, min:int):
        time.sleep(min)
    

def simpiProcess(data, signals):
    
    simpi = SimpiQ(data)

    while(simpi.size() > 0):
        print(f"{optionToString(simpi.next())}")

    print("Simpi finished")

    # option.waitUntil(signals, 0)

    # for i in range(data):
    #     print(f"Simpi is running: {i}, Signals: {signals[0]}")
    #     option.sleep(1)


