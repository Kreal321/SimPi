import os

import multiprocessing
import psutil
from playsound import playsound

class Audio:

    process = None
    processutil = None

    def __init__(self, data):

        self.process = multiprocessing.Process(target=audioProcess, args=(data,))

    def start(self):
        if(self.processutil == None): 
            self.process.start()
            self.processutil = psutil.Process(self.process.pid)
        else:
            print(self.processutil.status())
            print("Warning: this audio process is already started")
        

    def pause(self):
        """suspend simpi process
        """
        if(self.processutil.status() == "running" or self.processutil.status() == "sleeping"): 
            self.processutil.suspend()
        else:
            print(self.processutil.status())
            print("Warning: this audio process is already suspended")

    def resume(self):
        """resume simpi process
        """
        if(self.processutil.status() == "stopped"): 
            self.processutil.resume()
        else:
            print(self.processutil.status())
            print("Warning: this audio process is already running")

    def kill(self):
        """kill simpi process
        """
        self.process.kill()

def audioProcess(data):
    # os.system("mpg123 Server/Sources/" + data + ".mp3")
    playsound("Server/Sources/" + data + ".mp3")