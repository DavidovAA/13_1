import time
import asyncio

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнование')
    t1 = 1/power
    for i in range(1, 6):
        await asyncio.sleep(t1)
        print(f'Силач {name} поднял шар под номером {i}')
    print(f'Силач {name} закончил соревнования')

async def start_tournament():
    part1 = asyncio.create_task(start_strongman('Pasha', 3))
    part2 = asyncio.create_task(start_strongman('Denis', 4))
    part3 = asyncio.create_task(start_strongman('Appolon', 5))
    await part1
    await part2
    await part3

asyncio.run(start_tournament())
