import time
from audio import Audio
try:
    import RPi.GPIO as GPIO
except ImportError:
    print(f"ERROR: GPIO package is not imported.")

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
        "53": "Wait until click button",
        "61": "Open Source ",
        "62": "Close Source ",
        "71": "Play Audio ",
        "72": "Pause Audio ",
        "73": "Resume Audio ",
        "74": "Stop Audio ",
    }
    if(option["type"] == "50"):
        return "Wait " + option["data"][0] + " seconds"
    else:
        return optionList[option["type"]] + option["data"][0]

class SimpiQ:
    queue = []
    idx = 0
    audios = {}
    connected_clients = []

    def __init__(self, data, clients) -> None:
        self.queue = data
        self.connected_clients = clients
        try:
            GPIO.setmode(GPIO.BCM)
        except:
                print(f"ERROR: GPIO set mode failed.")
    
        for i in [2, 3, 4, 17, 27, 22, 10, 9]:
            try:
                GPIO.setup(i, GPIO.OUT)
                GPIO.output(i, GPIO.HIGH)
            except:
                print(f"ERROR: GPIO port {i} setting up failed.")

    def size(self) -> int:
        return len(self.queue)

    def hasNext(self) -> bool:
        return self.size() > self.idx

    def pop(self):
        self.idx += 1
        return self.queue[self.idx - 1]

    def currentIdx(self) -> int:
        return self.idx + 1

    async def waitUntil(self, signals, idx):
        signals[idx] = True
        while(signals[idx]):
            print(f"Simpi is waiting signal")
            await self.connected_clients.send(f"Simpi is waiting signal")
            time.sleep(1)

    def wait(self, sec:int):
        time.sleep(sec)

    def turnOn(self, port):
        try:
            GPIO.output(int(port), GPIO.LOW)
        except:
            print(f"ERROR: GPIO port {port} set low failed.")

    def turnOff(self, port):
        try:
            GPIO.output(int(port), GPIO.HIGH)
        except:
            print(f"ERROR: GPIO port {port} set high failed.")    

    def playAudio(self, file):
        self.audios[file] = Audio(file)
        self.audios[file].start()

    def pauseAudio(self, file):
        self.audios[file].pause()

    def stopAudio(self, file):
        self.audios[file].kill()

def simpiProcess(data, signals, connected_clients):
    
    simpi = SimpiQ(data, connected_clients)

    print(f"Received Simpi Queue:")
    for item in data:
        print(f"{optionToString(item)}")
    print(f"--------------------------")


    while(simpi.hasNext()):
        current = simpi.pop()
        print(f"{simpi.currentIdx() - 1}: {optionToString(current)}")
        if(current["type"] == "10"):
            print("Simpi start running.")
        if(current["type"] == "11"):
            print("Simpi is waiting start buttun signal to start running.")
            simpi.waitUntil(signals, 0)
        if(current["type"] == "53"):
            print("Simpi is waiting buttun signal to continue running.")
            simpi.waitUntil(signals, 0)
        if(current["type"] == "50"):
            simpi.wait(int(current["data"][0]))
        if(current["type"] == "61"):
            simpi.turnOn(current["data"][0])
        if(current["type"] == "62"):
            simpi.turnOff(current["data"][0])
        if(current["type"] == "71"):
            simpi.playAudio(current["data"][0])
        if(current["type"] == "74"):
            simpi.stopAudio(current["data"][0])
        

    print("Simpi finished")

    # option.waitUntil(signals, 0)

    # for i in range(data):
    #     print(f"Simpi is running: {i}, Signals: {signals[0]}")
    #     option.sleep(1)


