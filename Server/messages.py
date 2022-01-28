import json

from simpiController import SimpiController, simpi

from messager import Messager

connected_clients = Messager()

async def decoding(ws, message):
    global simpi
    message = json.loads(message)

    if (message["type"] == 1) :
        if message["data"] == "hello":
            await ws.send("Hello! Nice to meet you")
        elif message["data"] == "Start":
            # Start Simpi Process
            if(simpi):
                print("Warning: simpi process is running")
            else:
                simpi = SimpiController(connected_clients, 100)
        elif message["data"] == "Stop":
            # Stop Simpi Process
            if(simpi):
                await simpi.stop()
                simpi = None
            else:
                print("Warning: simpi process is not starting yet")
        elif message["data"] == "Suspend":
            if(simpi):
                await simpi.suspend()
            else:
                print("Warning: simpi process is not starting yet")
        elif message["data"] == "Resume":  
            if(simpi):
                await simpi.resume()
            else:
                print("Warning: simpi process is not starting yet")
        elif (message["type"] == 2):
            pass

    
    print(f'Received from client{ws.remote_address}: {message}')
    await connected_clients.send(f"Server has received a message [{message}]")

def encoding(data, type = 0):
    msg = {"data": data, "type": type}
    return json.dumps(msg)