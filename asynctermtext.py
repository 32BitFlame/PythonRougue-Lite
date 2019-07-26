import asyncio
import websockets

async def spam():
    for x in range(100):
        print("text")
        await asyncio.sleep(300)
    return asyncio.sleep(1)
spam()
input()