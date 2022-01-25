# Server Python >= 3.5
import sys
import asyncio
import websockets

from messages import connected_clients

# For each WebSocket connection
async def handler(ws, path):
    """websocket
    Args:
        ws (WebSocketServerProtocol): [description]
        path (int): [description]
    """
    await connected_clients.new(ws)
    await connected_clients.receiveMsgs(ws)

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