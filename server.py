import asyncio
import websockets

async def hello(websocket, path):
    info = await websocket.recv()
    print(f"got: {info}")

    if info.lower() == "deez":
        response = f"{info} Nuts!"
    else:
        #  response = "Guten Morgen herr fring."
        response = info

    await websocket.send(response)
    print(f"sent: {response}")


start_server = websockets.serve(hello, "localhost", 7070)

def main()->None:
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    main()
