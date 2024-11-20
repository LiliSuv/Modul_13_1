import time
import asyncio

async def start_strongman(name, power):
    print (f'Силач {name} начал соревнования.')
    for i in range (1,6):
        print (f'Силач {name} поднял {i}')

        await asyncio.sleep (1/power)
    print (f'Силач {name} закончил соревнования.')


async def start_tournament():
    print (f"Начало соревнований\n{'-'*20}")

    task1 = asyncio.create_task (start_strongman('Алёша Попович', 3))
    task2 = asyncio.create_task (start_strongman('Добрыня Никитич', 4))
    task3 = asyncio.create_task (start_strongman ('Илья Муромец', 5))
    await task1
    await task2
    await task2
    print (f"\nФиниш\n{'-'*7}")
start = time.time ()
asyncio.run (start_tournament())
finish = time.time ()
