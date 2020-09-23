import threading
import time


class Worker:

    def __init__(self, event):
        self.event = event
        self.event_done = threading.Event()
        self.return_item = None
    
    def return_listener(self):
        self.event_done.wait()
        self.event_done.clear()
        return self.return_item

    def start_work(self):
        self.event.wait()
        print("start work")
        time.sleep(1)
        print("work done")
        self.return_item = "Returned item"
        self.event_done.set()

event = threading.Event()
worker = Worker(event)
while True:
    input()
    threading.Thread(target=worker.start_work, daemon=True).start()
    event.set()
    print(worker.return_listener())
    event.clear()








