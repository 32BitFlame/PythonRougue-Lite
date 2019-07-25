import asyncio
import websockets

async def echo(webs, path):
    async for message in webs:
        await webs.send(message)

asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, 'localhost', 6969))
asyncio.get_event_loop().run_forever()