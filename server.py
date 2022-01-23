# Server Python >= 3.5
# To start the server: run python3 server.py first then run client
from asyncio.windows_events import NULL
import sys
import asyncio
import websockets
import time

import multiprocessing
import psutil

# Connected websocket (clients list)
connected_clients = set()

simpi = NULL

# Send message to clients/client
async def send(msg, client = NULL):
    if(client):
        await client.send(msg)
    else:
        for connected_client in connected_clients:
            await connected_client.send(msg)

# SimpiProcess class for controling simpi child process
class SimpiProcess:
    process = NULL
    processutil = NULL

    def __init__(self):
        self.process = multiprocessing.Process(target=simpi_processing, args=())
        self.process.start()
        self.processutil = psutil.Process(self.process.pid)

    def suspend(self):
        self.processutil.suspend()

    def resume(self):
        self.processutil.resume()

    def kill(self):
        self.process.kill()


class Simpi:
    simpiprocess = NULL

    def __init__(self, process):
        self.simpiprocess = process

    # actions
    def turnOn(self, source):
        # TODO
        send(f"Turn on {source}")

    def turnOff(self, source):
        # TODO
        send(f"Turn off {source}")

    def wait(self, time):
        # TODO
        send(f"Wait {time}")

    async def suspend(self):
        self.simpiprocess.suspend()
        await send(f"Simpi is suspended")
        print(f"Simpi is suspended")

    async def resume(self):
        self.simpiprocess.resume()
        await send(f"Simpi is resumed")
        print(f"Simpi is resumed")

    async def stop(self):
        self.simpiprocess.kill()
        await send(f"Simpi is stoped")
        print(f"Simpi is stoped")



def simpi_processing():
    
    for i in range(100):
        print(f"Simpi is running: {i}")
        time.sleep(1)



# Main process handling message processing
async def process(ws):
    global simpi
    message = await ws.recv()
    print(f'Received from client{ws.remote_address}: {message}')
    await send(f"Server has received a message [{message}]")

    if message == "hello":
        await ws.send("Hello! Nice to meet you")
    elif message == "Suspend Simpi":
        await simpi.suspend()
    elif message == "Resume Simpi":  
        await simpi.resume()

        


# For each WebSocket connection
async def handler(ws, path):
    # Each time a new client connect
    print(f'A client just connected {ws.remote_address}')
    connected_clients.add(ws)
    try:
        # Welcome message
        await ws.send("Server is connected")

        # Wait for client
        while True:
            await process(ws)

    except websockets.exceptions.ConnectionClosed as e:
        print(f'A client just disconnected {ws.remote_address}')
        print(e)

    finally:
        connected_clients.remove(ws)



# Main
if __name__ == '__main__':

    # Set IP
    ip = '127.0.0.1'
    try:
        if sys.argv[1] == "remote":
            ip = sys.argv[2]

    except Exception as e:
        print(e)

    # Start Simpi Process
    simpi = Simpi(SimpiProcess())
 

    # Start server
    server = websockets.serve(handler, ip, 80, ping_timeout=None)
    print(f"Start server on {ip}")

    asyncio.get_event_loop().run_until_complete(server)
    asyncio.get_event_loop().run_forever()
        

