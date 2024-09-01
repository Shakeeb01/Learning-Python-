# Asyncio:-
# asyncio is a Python library used for writing concurrent code using the async and await keywords. It is ideal for I/O-bound and high-level structured network code. To understand asyncio, it's helpful to have a basic understanding of synchronous and asynchronous programming.   

# Synchronous Programming:
# In synchronous programming, tasks are performed one at a time. The next task begins only after the current task finishes. This approach is straightforward but can be inefficient if tasks involve waiting

# Asynchronous Programming: 
# In asynchronous programming, tasks can run independently of each other. If a task involves waiting, the program can switch to another task. This approach allows you to handle multiple tasks at once without blocking the execution flow.

# EVENT LOOP:
# The event loop is the core of asyncio. It manages and executes asynchronous tasks, handles I/O, and provides a mechanism to schedule and run functions at specific times.
import asyncio
# create an event loop
loop = asyncio.get_event_loop()
# run the event loop
loop.run_forever()



# COROUTINES:- 
# Coroutines are special functions defined using async def. They can pause execution with await until the awaited task completes, allowing other tasks to run concurrently.
async def function_1():
    print("hello")
    await asyncio.sleep(2)  # Simulate an asynchronous I/O operation
    print("world!")
    
# Running the coroutine using the event loop    
asyncio.run(function_1())    


# 'await' Keyword:
# The await keyword is used to pause the execution of a coroutine until the awaited task completes. You can only use await inside an async def function.



# TASK:
# Tasks are used to schedule coroutines concurrently in the event loop. When you run a coroutine with asyncio.create_task(), it becomes a Task and runs concurrently with other tasks.
async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

async def main():
    task1 = asyncio.create_task(say_hello())
    task2 = asyncio.create_task(say_hello())
    
    await task1  # Wait for task1 to complete
    await task2  # Wait for task2 to complete

asyncio.run(main())



# GATHERING TASK:
# asyncio.gather() is used to run multiple coroutines concurrently and wait for them to finish.
async def function_1():
    await asyncio.sleep(5)
    print("Function 1")
    
async def function_2():
    await asyncio.sleep(2)
    print("function 2")
    
async def function_3():
    await asyncio.sleep(3)
    print("function 3")
    

# here i gather all three functions into main function.which means that all the three function will start there time. 
async def main():
    await asyncio.gather(
        function_1(),
        function_2(),
        function_3(),
    )
    
asyncio.run(main())    

