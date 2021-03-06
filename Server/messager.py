import websockets

import messages as msg
from config import Config

class Messager:
    clients = set()
    simpiConfigs = Config()
    
    def __init__(self) -> None:
        pass

    async def new(self, ws):
        # Each time a new client connect
        print(f'A client just connected {ws.remote_address}')
        self.clients.add(ws)

    async def send(self, message: str, client = None, debug = False, status = False, type = 0):
        """Send message to clients/client
        Args:
            msg (str): message to send
            client (WebSocketServerProtocol, optional): the client receive message. Defaults to None (send to all clients).
        """
        if debug:
            for c in self.clients:
                await c.send(msg.encoding(message, 4))

        if status:
            for c in self.clients:
                await c.send(msg.encoding(message, 5))

        if client:
            await client.send(msg.encoding(message, type))
        else:
            for c in self.clients:
                await c.send(msg.encoding(message, type))


    async def receiveMsgs(self, ws):
        """Listen to the port and receive messages from client
        Args:
            ws (WebSocketServerProtocol): websocket connection
        """
        try:
            # Welcome message
            await ws.send(msg.encoding(len(self.clients), 3))
            await ws.send(msg.encoding("Server is connected"))
            await ws.send(msg.encoding(self.simpiConfigs.getNames(), 6))

            # Wait for client sending messages
            while True:
                message = await ws.recv()
                await msg.decoding(ws, message)

        except websockets.exceptions.ConnectionClosed as e:
            print(f'A client just disconnected {ws.remote_address}')
            # print(e)

        finally:
            self.clients.remove(ws)


    