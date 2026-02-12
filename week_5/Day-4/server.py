import asyncio
import websockets

async def echo_handler(websocket):
    try:
        async for message in websocket:
            print(f"Received from client:{message}")
            await websocket.send(f"server echoed:{message}")
            
    except websockets.exceptions.ConnectionsClosed as e:
        print(f"Connection closed: {e}")
        
async def main():
    async with websockets.serve(echo_handler, "",8756):
        print("Websocket server started and listening on ws://localhost:8756")
        await asyncio.Future()
        
if __name__ == "__main__":
    asyncio.run(main())