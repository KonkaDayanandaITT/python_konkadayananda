# import asyncio
# import websockets


# async def handler(websocket):
#     print("Client has connected:", websocket.remote_address)
#     try:
#         async for message in websocket:
#             print("Nitin:", message)
#             server_message=input()
#             await websocket.send(f"Daya:{server_message}")
#     except websockets.ConnectionClosed:
#         print("Client Disconnected")
        
# async def main():
#     async with websockets.serve(handler, "172.22.0.33", 8765):
#        print("Websocket server is listening on ws://172.22.0.33:8765")
#        await asyncio.Future()
        
        
# asyncio.run(main())
        