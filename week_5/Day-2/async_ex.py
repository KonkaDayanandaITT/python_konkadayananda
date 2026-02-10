import asyncio

async def func():
    print("Hello!")
    await asyncio.sleep(2)
    print("Ram")
    
asyncio.run(func())