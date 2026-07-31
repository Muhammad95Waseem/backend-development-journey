import asyncio

# Define an asynchronous coroutine function
async def hello_1():
    print("Hello 1")
    # Gives control back to the event loop for 3 seconds.
    # While waiting here, other scheduled tasks can run on the event loop.
    await asyncio.sleep(3)
    print("Done 1") 

async def hello_2():
    print("Hello 2")
    # Yield control back to the event loop for 3 seconds.
    await asyncio.sleep(3)
    print("Done 2")

async def main():
    # asyncio.create_task schedules the coroutines to run on the event loop concurrently.
    # Execution begins immediately when control is passed back to the event loop.
    task_1 = asyncio.create_task(hello_1())
    task_2 = asyncio.create_task(hello_2())

    # Pause 'main' until task_1 finishes.
    # While waiting, task_1 runs, hits asyncio.sleep(3), and control jumps to task_2.
    await task_1
    
    # Pause 'main' until task_2 finishes.
    # Since task_2 was running concurrently with task_1, it will be complete at roughly the same time.
    await task_2

# Entry point: Starts the asyncio event loop and executes the main() coroutine
asyncio.run(main())