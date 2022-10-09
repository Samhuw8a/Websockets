import asyncio
import websockets

class Client():
    def __init__(self,uri:str)->None:
        self.uri  = uri

    async def send(self, info:str)->None:
        async with websockets.connect(self.uri) as websocket:
            await websocket.send(info)
            #  print(f"sent :{info}")
            resp:str = await websocket.recv()
            #  print(f"got: {resp}")
            print(f"< {resp}")

def main()->None:
    client=Client("")
    while True:
        inp=input("> ")
        #  client.send(inp)
        asyncio.get_event_loop().run_until_complete(client.send(inp))

if __name__ == "__main__":
    main()


async def hello():
    uri = "ws://jonas-server.internet-box.ch:7070"
    async with websockets.connect(uri) as websocket:
        info ="deez"
        await websocket.send(info)
        print(f"sent: {info}")

        response = await websocket.recv()
        print(f"got {response}")

#  asyncio.get_event_loop().run_until_complete(hello())
