import threading
import time


def worker_one(event: threading.Event):
    event.wait()
    print("worker two one")


def worker_two(event: threading.Event):
    event.wait()
    cycle = False
    anim = [1, 2, 3, 4, 5]
    counter = 0
    while event.is_set():

        if cycle:
            counter -= 1
        else:
            counter += 1
        
        if counter == len(anim) - 1:
            cycle = True

        time.sleep(1)
        print(anim[counter], end="\r")
    print("worker two done")


if __name__ == "__main__":
    event_1 = threading.Event()
    t1 = threading.Thread(target=worker_two, args=(event_1,))
    t1.start()
    
    event_1.set()
    
    time.sleep(20)
    
    event_1.clear()
    
    t1.join()