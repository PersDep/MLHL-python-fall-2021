import random
from time import sleep
import asyncio
import time


def task(pid):
    """Synchronous non-deterministic task.
    """
    sleep(random.randint(0, 2) * 0.2)
    print('Task %s done' % pid)


async def task_coro(pid):
    """Coroutine non-deterministic task
    """
    await asyncio.sleep(random.randint(0, 2) * 0.2)
    print('Task %s done' % pid)


def synchronous():
    for i in range(1, 10):
        task(i)


async def asynchronous():
    tasks = [asyncio.ensure_future(task_coro(i)) for i in range(1, 10)]
    await asyncio.wait(tasks)


print('Synchronous:')
start = time.time()
synchronous()
print(time.time() - start)

ioloop = asyncio.get_event_loop()
print('Asynchronous:')
start = time.time()
ioloop.run_until_complete(asynchronous())
ioloop.close()
print(time.time() - start)
