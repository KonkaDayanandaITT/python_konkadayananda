import asyncio
import websockets

connected_clients = set()

async def echo_handler(websocket):
    connected_clients.add(websocket)
    print(f"Client connected.Total clients:{len(connected_clients)}")

    try:
        async for message in websocket:
            print(f"Received:{message}")
            await websocket.send(f"Echo:{message}")

    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")

    finally:
        connected_clients.remove(websocket)
        print(f"Remaining clients:{len(connected_clients)}")

async def main():
    async with websockets.serve(echo_handler, "localhost", 8756):
        print("Server running...")
        await asyncio.Future()

asyncio.run(main())
