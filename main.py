from quickANSImark import mparse
from terminaltools import clear
import websockets
import asyncio
class netclient():
    def __init__(self, uri):
        self.webs = websockets.connect(f"ws://{uri}")

    def update("")


async def main():
    if not websockets.connect("ws://localhost:6969"):
        await asyncio.sleep(5)
    async with websockets.connect("ws://localhost:6969") as webs:
        text = input()
        while text != "q":
            await webs.send(text)
            a = await webs.recv()
            try:
                for x in a:
                    print(x)
            except Exception as e:
                pass
            print(a)
        text = input()

asyncio.get_event_loop().run_until_complete(main())
asyncio.get_event_loop().run_forever()
