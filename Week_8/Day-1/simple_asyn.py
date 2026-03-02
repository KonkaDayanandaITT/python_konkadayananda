import asyncio
import time

# async def greet():
#     print("start", time.perf_counter() - start)
#     await asyncio.sleep(3)
#     print("End", time.perf_counter() - start)
    
# start = time.perf_counter()
# asyncio.run(greet())

# async def task1():
#     print("Task 1 started")
#     await asyncio.sleep(3)
#     print("Task 1 ended")
    
# async def task2():
#     print("Task 2 started")
#     await asyncio.sleep(1)
#     print("Task 2 finished")
    
# async def main():
#     print("Started", time.perf_counter() - start)
#     await task1()
#     await task2()
#     print("ended", time.perf_counter() - start)
                                                        #still runs synchronously because we didn't scheduled them using async def means not run concurrently always
# start = time.perf_counter()
# asyncio.run(main())

# async def task1():
#     print("Task 1 started")
#     await asyncio.sleep(3)
#     print("Task 1 ended")
    
# async def task2():
#     print("Task 2 started")
#     await asyncio.sleep(1)
#     print("Task 2 finished")
                                                #using gather to run concurrently
# async def main():
#     print("start", time.perf_counter() - start)
#     await asyncio.gather(task1(), task2())
#     print("ended", time.perf_counter() - start)
    
# start = time.perf_counter()
# asyncio.run(main())

# async def square(n):
#     await asyncio.sleep(1)
#     return n * n

# async def main():
#     print("start", time.perf_counter() - start)
#     results = await asyncio.gather(
#         square(2),
#         square(3), 
#         square(4)
#     )
#     print(results)
#     print("end", time.perf_counter() - start)
    
# start = time.perf_counter()
# asyncio.run(main())

async def worker(name):
    # print(f" worker {name} has started",time.perf_counter() - start)
    await asyncio.sleep(2)
    # print(f" worker {name} has ended", time.perf_counter() - start)
    
async def main():
    t1 =  asyncio.create_task(worker("A"))
    t2 =  asyncio.create_task(worker("B"))
    print("Tasks created")
    await t1
    await t2

start = time.perf_counter()
asyncio.run(main())
 