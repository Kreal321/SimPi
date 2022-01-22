# Server Python >= 3.5
# To start the server: run python3 server.py first then run client
import sys
import asyncio
import websockets

# Connected websocket (clients list)
connected_clients = set()


# Main process
async def process(ws):
    message = await ws.recv()
    print(f'Received from client{ws.remote_address}: {message}')
    for client in connected_clients:
        await client.send(f"Server has received a message [{message}]")
    if message == "hello":
        await ws.send("Hello! Nice to meet you")
    elif message == "Power up GPIO 1":
        await ws.send("GPIO 1 powered up")
    elif message == "Power off GPIO 1":  
        await ws.send("GPIO 1 powered off")


# For each WebSocket connection
async def server(ws:str, path:int):
    # Each time a new client connect
    print(f'A client just connected {ws.remote_address}')
    connected_clients.add(ws)
    try:
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
    ip = '127.0.0.1'
    try:
        if sys.argv[1] == "remote":
            ip = sys.argv[2]

    except Exception as e:
        print(e)


    start_server = websockets.serve(server, ip, 80, ping_timeout=None)
    print(f"Start server on {ip}")

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
        

