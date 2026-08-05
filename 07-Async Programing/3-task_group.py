import asyncio

async def hello_1():
    print("Hello 1")
    await asyncio.sleep(3)
    print("Done 1") 

async def hello_2():
    print("Hello 2")
    await asyncio.sleep(3)
    print("Done 2")

async def main():

    async with asyncio.TaskGroup() as task_group:
        task_1 = task_group.create_task(hello_1())
        task_2 = task_group.create_task(hello_2())

    await task_1
    await task_2

asyncio.run(main())