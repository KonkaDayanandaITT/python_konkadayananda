import asyncio
import websockets
import uuid

clients = {}

async def handler(websocket):       
    user_id = uuid.uuid4().hex[:6]
    clients[websocket] = user_id 
    
    await websocket.send(f"Connected as {user_id}")
    print(f"{user_id} joined")
    print("active clients:", len(clients))

    try:
        async for message in websocket:
            broadcast = []
            formatted = f"{user_id}: {message}"
            
            for client in clients:
                broadcast.append(client.send(formatted))
            
            await asyncio.gather(*broadcast, return_exceptions=True)
        
    finally:
        print(f"{user_id} left")
        del clients[websocket]
        print("active clients:", len(clients))
        

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        print("chat server on ws://0.0.0.0://8765")
        await asyncio.Future()
        
if __name__ == "__main__":
    asyncio.run(main())