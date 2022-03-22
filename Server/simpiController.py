import time

from simpiProcessController import SimpiProcessController, signals

simpi = None

class SimpiController:
    """Simpi class
    """
    SimpiProcessController = None
    connected_clients = None

    def __init__(self, clients, data):
        """create a new Simpi class (and create a SimpiProcessController class)
        Args:
            data (array): 
        """
        self.connected_clients = clients
        self.SimpiProcessController = SimpiProcessController(data, clients)

    async def start(self):
        """start Simpi
        """
        self.SimpiProcessController.start()
        await self.connected_clients.send(f"Simpi is started")
        print(f"Simpi is started")


    async def wait(self, seconds: int):
        """Simpi wait
        Args:
            seconds (Num): sleep time
        """
        time.sleep(seconds)
        await self.connected_clients.send(f"Simpi is waiting")
        await self.connected_clients.send(f"Simpi start waiting for {seconds} seconds")

    async def suspend(self):
        """Suspend Simpi
        """
        self.SimpiProcessController.suspend()
        await self.connected_clients.send(f"Simpi is suspended")
        print(f"Simpi is suspended")

    async def resume(self):
        """Resume Simpi
        """
        self.SimpiProcessController.resume()
        await self.connected_clients.send(f"Simpi is resumed")
        print(f"Simpi is resumed")

    async def stop(self):
        """Stop Simpi
        """
        self.SimpiProcessController.kill()
        await self.connected_clients.send(f"Simpi is stoped")
        print(f"Simpi is stoped")