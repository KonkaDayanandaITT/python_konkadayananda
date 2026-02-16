import asyncio
import websockets

async def send_msg(ws):
    while True:
        msg = await asyncio.to_thread(input)
        await ws.send(msg)
        
async def recieve_msg(ws):
    while True:
        msg = await ws.recv()
        print(msg)
        
async def main():
    async with websockets.connect("ws://localhost:8765") as ws:
        await asyncio.gather(send_msg(ws), recieve_msg(ws))
        
        
asyncio.run(main())