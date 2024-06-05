import asyncio
import websockets

class P2PConnection:
    def __init__(self, uri):
        self.uri = uri

    async def connect(self):
        self.connection = await websockets.connect(self.uri)

    async def send_file(self, file_path):
        with open(file_path, 'rb') as file:
            data = file.read()
            await self.connection.send(data)

    async def receive_file(self, output_path):
        data = await self.connection.recv()
        with open(output_path, 'wb') as file:
            file.write(data)

    async def close(self):
        await self.connection.close()
