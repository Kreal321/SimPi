import multiprocessing
import psutil

from simpi import simpiProcess

signals = multiprocessing.Array('i', [True, False])

class SimpiProcessController:
    """SimpiProcessController class for controling simpi child process
    """
    process = None
    processutil = None

    def __init__(self, data):
        """create a new simpi process
        Args:
            data (dictionary): 
        """
        self.process = multiprocessing.Process(target=simpiProcess, args=(data, signals))
        self.process.start()
        self.processutil = psutil.Process(self.process.pid)

    def suspend(self):
        """suspend simpi process
        """
        if(self.processutil.status() == "running" or self.processutil.status() == "sleeping"): 
            self.processutil.suspend()
        else:
            print(self.processutil.status())
            print("Warning: the simpi process is already suspended")

    def resume(self):
        """resume simpi process
        """
        if(self.processutil.status() == "stopped"): 
            self.processutil.resume()
        else:
            print(self.processutil.status())
            print("Warning: the simpi process is already running")

    def kill(self):
        """kill simpi process
        """
        self.process.kill()

