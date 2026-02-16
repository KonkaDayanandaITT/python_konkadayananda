import asyncio
import time
import random

async def read_file_async(file_name):
    print(f"{file_name} Read start:", time.perf_counter())
    await asyncio.sleep(random.randint(2,5))
    print(f"{file_name} Read end:", time.perf_counter())
    return "content"

async def process_file_async(content, file_name):
    print(f"{file_name} Process start:", time.perf_counter())
    await asyncio.sleep(random.randint(1,3))
    print(f"{file_name} Process end:", time.perf_counter())
    return f"Processed {content}"

async def write_file_async(file_name, content):
    print(f"{file_name} Write start:", time.perf_counter())
    await asyncio.sleep(random.randint(1,2))
    print(f"{file_name} Write end:", time.perf_counter())
    
async def file_process(file_name):
    content = await read_file_async(file_name)
    processed = await process_file_async(content, file_name)
    await write_file_async(file_name, processed)
    
async def asyn_main():
    start = time.perf_counter()
    
    async with asyncio.TaskGroup() as tg:
        for i in range (1, 6):
            tg.create_task(file_process(f"file{i}.txt"))
    end = time.perf_counter()
    
    return end - start
    
# asyncio.run(main())

def file_process_sync(name):
    time.sleep(3)
    time.sleep(2)
    time.sleep(1)
    
def sync_main():
    start = time.perf_counter()

    for i in range(1,6):
        file_process_sync(i)
        
    end =time.perf_counter()
    
    return end - start

async_time = asyncio.run(asyn_main())
sync_time = sync_main()


if __name__ == "__main__":
    print("Async_time:", async_time)
    print("Sync_time:", sync_time)
    print("Total time saved:", sync_time - async_time)