from simpiController import SimpiController, simpi

from messager import Messager

connected_clients = Messager()

async def decoding(ws, message):
    global simpi
    
    print(f'Received from client{ws.remote_address}: {message}')
    await connected_clients.send(f"Server has received a message [{message}]")

    if message == "hello":
        await ws.send("Hello! Nice to meet you")
    elif message == "Start":
        # Start Simpi Process
        if(simpi):
            print("Warning: simpi process is running")
        else:
            simpi = SimpiController(connected_clients, 100)
    elif message == "Stop":
        # Stop Simpi Process
        if(simpi):
            await simpi.stop()
            simpi = None
        else:
            print("Warning: simpi process is not starting yet")
    elif message == "Suspend":
        if(simpi):
            await simpi.suspend()
        else:
            print("Warning: simpi process is not starting yet")
    elif message == "Resume":  
        if(simpi):
            await simpi.resume()
        else:
            print("Warning: simpi process is not starting yet")