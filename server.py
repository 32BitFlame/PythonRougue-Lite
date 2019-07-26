import asyncio
import websockets
import websocket

async def echo(webs, path):
    async for message in webs:
        await webs.send(f"{path}{message}")
        print(webs)
        print(path)
print("starting")
asyncio.get_event_loop().run_until_complete(websockets.serve(echo, 'localhost', 6969))
asyncio.get_event_loop().run_forever()
