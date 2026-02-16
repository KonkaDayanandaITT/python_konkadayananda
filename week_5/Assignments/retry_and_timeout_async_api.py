import asyncio
import httpx
import time


URLS = [
    "https://httpbin.org/delay/3",
    "https://httpbin.org/delay/3",
    "https://httpbin.org/delay/3",
    "https://dummyjson.com/products/1"
]



async def fetch_using_retry(client, url):
    time_out = 2
    retries = 3
    for attempt in range(retries):
        try:
            response = await client.get(url, timeout = time_out)
            print(f"{url} success({response.status_code})")
            return
        except Exception as e:
            if attempt == retries - 1:
                print(f"{url} Failed({e})")
                return
            await asyncio.sleep(2 ** attempt)
            
async def concurrent_fetch():
    async with httpx.AsyncClient() as client:
        tasks = []
        for url in URLS:
            task = fetch_using_retry(client, url)
            tasks.append(task)
            
        await asyncio.gather(*tasks)
        
async def sequential_fetch():
    async with httpx.AsyncClient() as client:
        for url in URLS:
            await fetch_using_retry(client, url)
            

async def main():
    print("\n Concurrent Execution")
    start = time.perf_counter()
    await concurrent_fetch()
    concurrent_time = time.perf_counter() - start
    
    print("\n Sequential Execution")
    start = time.perf_counter()
    await sequential_fetch()
    sequential_time = time.perf_counter() - start
    
    print(f"\nConcurrent time:{concurrent_time:.2f}s")
    print(f"Sequential time:{sequential_time:.2f}s")
    
if __name__ == "__main__":
    asyncio.run(main())
            