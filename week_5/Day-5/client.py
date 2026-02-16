import asyncio
import websockets

async def send(ws):
    while True:
        message = input("You: ")
        await ws.send(message)

async def receive(ws):
    while True:
        msg = await ws.recv()
        print("Broadcast:", msg)

async def run():
    async with websockets.connect("ws://localhost:8765") as ws:
        await asyncio.gather(send(ws), receive(ws))

asyncio.run(run())
