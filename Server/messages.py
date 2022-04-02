import json

from simpiController import SimpiController, simpi, signals

from messager import Messager

try:
    import RPi.GPIO as GPIO
except ImportError:
    print(f"ERROR: GPIO package is not imported.")

connected_clients = Messager()

async def decoding(ws, message):
    global simpi
    message = json.loads(message)

    if (signals[2] == True):
        await simpi.stop()
        simpi = None
        signals[2] = False


    if (message["type"] == 1) :
        if message["data"] == "hello":
            await ws.send("Hello! Nice to meet you")
        elif message["data"] == "Start":
            # Start Simpi Process
            if(simpi):
                signals[0] = 0
                await simpi.start()
            else:
                print("Warning: simpi process is not initialized")
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
        elif message['data'] == "signal":
            signals[1] = False
        elif message['data'] == "cleanup":
            try:
               GPIO.cleanup()
            except:
                print(f"ERROR: GPIO clean up failed.")
        elif message['data'] == "status":
            await connected_clients.send(f"{signals[0]}", status = True)

            

    elif (message["type"] == 2):
        if(simpi):
            print("Warning: simpi process is running")
        else:
            simpi = SimpiController(connected_clients, message["data"])
            # if(message["data"][0]["type"] == "10"):
            if(simpi):
                signals[0] = 0
                await simpi.start()
            else:
                print("Warning: simpi process is not initialized")

    elif (message["type"] == 8):
        option = message["data"]
        if(option["type"] == "save"):
            connected_clients.simpiConfigs.saveConfig(option["file"], option["data"])
            await connected_clients.send(connected_clients.simpiConfigs.getNames(), type = 6)
        elif (option["type"] == "load"):
            await connected_clients.send(connected_clients.simpiConfigs.loadConfig(option["file"]), type = 7)
        elif (option["type"] == "delete"):
            connected_clients.simpiConfigs.deleteConfig(option["file"])
            await connected_clients.send(connected_clients.simpiConfigs.getNames(), type = 6)
        
    print(f'Received from client{ws.remote_address}: {message}')
    await connected_clients.send(f"Server has received a message [{message}]", debug=True)

def encoding(data, type = 0):
    msg = {"data": data, "type": type}
    return json.dumps(msg)