import asyncio
import websockets

async def client_conversation():
    uri = "ws://127.0.0.1:8756"
    try:
        async with websockets.connect(uri) as websocket:
            messages_to_send = ["Hello World!", "How are you?", "Goodbye"]

            for message in messages_to_send:
                await websocket.send(message) 
                print(f"Sent: {message}")
                
                response = await websocket.recv()
                print(f"Received: {response}")

    except ConnectionRefusedError as e:
        print(e,"Connection refused. Make sure the server is running.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(client_conversation())

