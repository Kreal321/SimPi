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
pause = NULL

# Send message to clients/client
async def send(msg, client = NULL):
    if(client):
        await client.send(msg)
    else:
        for connected_client in connected_clients:
            await connected_client.send(msg)


# actions
def turnOn(source):
    # TODO
    send(f"Turn on {source}")

def turnOff(source):
    # TODO
    send(f"Turn off {source}")

def wait(time):
    # TODO
    send(f"Wait {time}")



def simpi_processing():
    
    for i in range(100):
        print(f"Simpi is running: {i}")
        time.sleep(1)



# Main process handling message processing
async def process(ws):
    global pause
    message = await ws.recv()
    print(f'Received from client{ws.remote_address}: {message}')
    await send(f"Server has received a message [{message}]")

    if message == "hello":
        await ws.send("Hello! Nice to meet you")
    elif message == "Power up GPIO 1":
        await ws.send("GPIO 1 powered up")
        print(pause)
        pause.suspend()
        await ws.send("Simpi suspended") 
    elif message == "Power off GPIO 1":  
        await ws.send("GPIO 1 powered off")
        pause.resume()
        await ws.send("Simpi resumed") 

        


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
    simpi = multiprocessing.Process(target=simpi_processing, args=())
    simpi.start()
    pause = psutil.Process(simpi.pid)

    # Start server
    server = websockets.serve(handler, ip, 80, ping_timeout=None)
    print(f"Start server on {ip}")

    asyncio.get_event_loop().run_until_complete(server)
    asyncio.get_event_loop().run_forever()
        

