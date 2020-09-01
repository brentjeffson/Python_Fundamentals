import asyncio
import random


async def do_something():
    await asyncio.sleep(1)
    n = random.randint(1, 10)
    if n > 5:
        raise Exception('Custom Raised Exception')
    else:
        print('[RETURN]')
        return 1


async def main():
    # task = asyncio.create_task(do_something())
    # try:
    #     print(await task)
    # except Exception as ex:
    #     print(f'[FIRST EXCEPTION HANDLER] {ex}')

    try:
        tasks = []
        for i in range(10):
            task = asyncio.create_task(do_something())
            tasks.append(task)
        results = (await asyncio.gather(*tasks, return_exceptions=True))
        total = 0

        # for result in results:
        #     if type(result) is not Exception:
        #         total += (result)
        #     else:
        #         print(result)
        #     print(f'[EXCEPTION TITLE] {result}')
        #     print(f'[EXCEPTION TYPE] {type(result)}', end='\n\n')

        print(f'[SUM] {total}')
        # print(f'[SUM] {(results)}')
    except Exception as ex:
        print(f'[SECOND EXCEPTION HANDLER] {ex}')

loop = None
try:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
except Exception as ex:
    print(f'[OUTSIDE EXCEPTION HANDLER] {ex}')
finally:
    if loop is not None:
        loop.close()