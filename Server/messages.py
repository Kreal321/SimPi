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

    if (message["type"] == 1) :
        if message["data"] == "hello":
            await ws.send("Hello! Nice to meet you")
        elif message["data"] == "Start":
            # Start Simpi Process
            if(simpi):
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
            signals[0] = False
        elif message['data'] == "try":
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
        elif message['data'][0:3] == "low":
            try:
               GPIO.output(int(message['data'][3:4]), GPIO.LOW)
            except:
                print(f"ERROR: GPIO port {message['data'][3:4]} set low failed.")
        elif message['data'][0:4] == "high":
            try:
               GPIO.output(int(message['data'][4:5]), GPIO.HIGH)
            except:
                print(f"ERROR: GPIO port {message['data'][4:5]} set high failed.")

    elif (message["type"] == 2):
        if(simpi):
            print("Warning: simpi process is running")
        else:
            simpi = SimpiController(connected_clients, message["data"])

    
    print(f'Received from client{ws.remote_address}: {message}')
    await connected_clients.send(f"Server has received a message [{message}]")

def encoding(data, type = 0):
    msg = {"data": data, "type": type}
    return json.dumps(msg)