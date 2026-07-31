import asyncio

# Define an asynchronous coroutine function
async def hello():
    print("Hello")
    # Gives control back to the event loop and pause execution for 3 seconds
    await asyncio.sleep(3)
    print("Done") 

# Execute the hello() coroutine inside a newly managed asyncio event loop
asyncio.run(hello())