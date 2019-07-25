from quickANSImark import mparse
from terminaltools import clear
import websockets
import asyncio
async with websockets.connect("ws://192.186.86.38:6969"):
    await send(input("test: "))
    await recv()