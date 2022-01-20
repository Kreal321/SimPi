# Server Python >= 3.5
# To start the server: run python3 server.py first then run client

import asyncio
import websockets

# Connected websocket (clients list)
connected_clients = set()

# Main process
async def process(ws):
    message = await ws.recv()
    print(f'Received from client{ws.remote_address}: {message}')
    for client in connected_clients:
        await client.send(f"Server received: {message}")



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
        
start_server = websockets.serve(server, '127.0.0.1', 5678, ping_timeout=None)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
