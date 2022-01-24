# Server Python >= 3.5
import sys
import asyncio
import websockets
import time

import multiprocessing
import psutil

# Connected websocket (clients list)
connected_clients = set()

simpi = None

async def send(msg: str, client = None):
    """Send message to clients/client

    Args:
        msg (str): message to send
        client (WebSocketServerProtocol, optional): the client receive message. Defaults to None (send to all clients).
    """
    if(client):
        await client.send(msg)
    else:
        for connected_client in connected_clients:
            await connected_client.send(msg)



class SimpiProcess:
    """SimpiProcess class for controling simpi child process
    """
    process = None
    processutil = None

    def __init__(self, data):
        """create a new simpi process

        Args:
            data (dictionary): 
        """
        self.process = multiprocessing.Process(target=simpi_processing, args=(data,))
        self.process.start()
        self.processutil = psutil.Process(self.process.pid)

    def suspend(self):
        """suspend simpi process
        """
        if(self.processutil.status() == "running"): 
            self.processutil.suspend()
        else:
            print("Warning: the simpi process is already suspended")

    def resume(self):
        """resume simpi process
        """
        if(self.processutil.status() == "stopped"): 
            self.processutil.resume()
        else:
            print("Warning: the simpi process is already running")

    def kill(self):
        """kill simpi process
        """
        self.process.kill()


class Simpi:
    """Simpi class
    """
    simpiprocess = None

    def __init__(self, data):
        """create a new Simpi class (and create a SimpiProcess class)

        Args:
            data (dictionary): 
        """
        self.simpiprocess = SimpiProcess(data)

    def turnOn(self, source):
        # TODO
        send(f"Turn on {source}")

    def turnOff(self, source):
        # TODO
        send(f"Turn off {source}")

    async def wait(self, seconds: int):
        """Simpi wait

        Args:
            seconds (Num): sleep time
        """
        time.sleep(seconds)
        await send(f"Simpi is waiting")
        send(f"Simpi start waiting for {seconds} seconds")

    async def suspend(self):
        """Suspend Simpi
        """
        self.simpiprocess.suspend()
        await send(f"Simpi is suspended")
        print(f"Simpi is suspended")

    async def resume(self):
        """Resume Simpi
        """
        self.simpiprocess.resume()
        await send(f"Simpi is resumed")
        print(f"Simpi is resumed")

    async def stop(self):
        """Stop Simpi
        """
        self.simpiprocess.kill()
        await send(f"Simpi is stoped")
        print(f"Simpi is stoped")



def simpi_processing(data):
    
    for i in range(data):
        print(f"Simpi is running: {i}")
        time.sleep(1)



# Main process monitor incoming message
async def receiveMsgs(ws):
    """Listen to the port and receive messages from client

    Args:
        ws (WebSocketServerProtocol): websocket connection
    """
    global simpi
    message = await ws.recv()
    print(f'Received from client{ws.remote_address}: {message}')
    await send(f"Server has received a message [{message}]")

    if message == "hello":
        await ws.send("Hello! Nice to meet you")
    elif message == "start":
        # Start Simpi Process
        if(simpi):
            print("Warning: simpi process is running")
        else:
            simpi = Simpi(100)
    elif message == "Suspend Simpi":
        await simpi.suspend()
    elif message == "Resume Simpi":  
        await simpi.resume()

        


# For each WebSocket connection
async def handler(ws, path):
    """websocket

    Args:
        ws (WebSocketServerProtocol): [description]
        path (int): [description]
    """
    # Each time a new client connect
    print(f'A client just connected {ws.remote_address}')
    connected_clients.add(ws)

    try:
        # Welcome message
        await ws.send("Server is connected")

        # Wait for client sending messages
        while True:
            await receiveMsgs(ws)

    except websockets.exceptions.ConnectionClosed as e:
        print(f'A client just disconnected {ws.remote_address}')
        print(e)

    finally:
        connected_clients.remove(ws)



# Main
if __name__ == '__main__':
    """Main function

    Args:
        argv[1]: remote or local
        argv[2]: local network ip
    """
    # Set IP
    ip = '127.0.0.1'
    try:
        if sys.argv[1] == "remote":
            ip = sys.argv[2]

    except Exception as e:
        print(f"Warning: {e}")


    # Start server
    server = websockets.serve(handler, ip, 80, ping_timeout=None)
    print(f"Start server on {ip}")

    asyncio.get_event_loop().run_until_complete(server)
    asyncio.get_event_loop().run_forever()
        

