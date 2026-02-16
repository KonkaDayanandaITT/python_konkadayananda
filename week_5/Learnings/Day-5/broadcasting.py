import asyncio
import websockets

clients = set()

async def handler(websocket):
   
    clients.add(websocket)
 
    
    try:
        async for message in websocket:
            broadcast = [peer.send(message) for peer in clients]
            await asyncio.gather(*broadcast, return_exceptions=True)
    # except Exception as e:
    #     print("Error occured:", e)
    finally:
        clients.discard(websocket)
        
async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        print("chat server on ws://0.0.0.0://8765")
        await asyncio.Future()
        
if __name__ == "__main__":
    asyncio.run(main())