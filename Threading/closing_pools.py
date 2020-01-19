from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import partial
import threading
import time
import sys


closing = False


def task(s):
    global closing
    while s >= 0:
        print(s)
        if closing:
            print("Force Closing")
            return
        time.sleep(1)
        s -= 1

    print('Task Done.')


def close_pool(s):
    global closing
    print(f"Waiting to close pool in {s}s")
    time.sleep(s)
    closing = True
    print(f"Closing pool...")


threading.Thread(target=close_pool, args=[4]).start()

with ThreadPoolExecutor(max_workers=2) as executor:
    secs = [5, 2, 10, 3, 2]
    futures = [executor.submit(task, s) for s in secs]

    for future in as_completed(futures):
        future.result()







