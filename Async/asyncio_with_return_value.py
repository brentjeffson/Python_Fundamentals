import asyncio
import time

async def do_something(t_start, id):
    print(f'[DOING SOMETHING] {time.time() - t_start}s')
    await asyncio.sleep(1)
    return id, f'[DONE] {time.time() - t_start} s'

async def print_done():
    print('[DONE]')

async def main(t_start):
    print('[STARTING TASKS]')
    tasks = []
    for i in range(1000):
        task = asyncio.create_task(do_something(t_start, i+1))
        tasks.append(task)
    for f in asyncio.as_completed(tasks):
        result = await f
        print(f'[RESULT] {result}')
    # results = await asyncio.gather(*tasks)
    # print(f'[RESULTS] {results}')
    # print(f'[TASKS CREATED] {len(tasks)}')
    # print(f'[TASKS VALUE] {tasks}')

if __name__ == '__main__':
    t_start = time.time()
    loop = None
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main(t_start))
    except Exception as ex:
        print(f'[EXCEPTION] {ex}')
    finally:
        if loop is not None:
            loop.close()
    print(f'[DURATION] {time.time() - t_start:0.2f} s')