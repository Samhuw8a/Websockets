import asyncio
import websockets

async def hello(info):
    uri = "ws://jonas-server.internet-box.ch:7070"
    async with websockets.connect(uri) as websocket:
        await websocket.send(info)
        #  print(f"sent: {info}")

        response = await websocket.recv()
        #  print(f"got {response}")


while True:
    inp=input("> ")
    asyncio.get_event_loop().run_until_complete(hello(inp))
