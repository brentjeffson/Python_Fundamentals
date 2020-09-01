import threading
import queue
import time


def plog(title: [], msg: [] = []):
    title = "".join([f"[{t}]" for t in title])
    msg = ".".join([str(m) for m in msg])
    print(f"{title}: {msg}")


class CustomThreading(threading.Thread):

    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, *, daemon=None):
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self.__q = queue.Queue()
        self.__stop = False

    def run(self) -> None:
        plog(["started"], [self.name])
        self.__worker()
        plog(["finished"], [self.name])
        super(CustomThreading, self).run()

    def put(self, item):
        self.__q.put(item)

    def wait(self):
        self.__q.join()

    def stop(self):
        self.__stop = True
        
    def __worker(self):
        while True:
            if self.__stop:
                break
            item = self.__q.get()
            # plog(["working"], [item])
            time.sleep(1)
            plog(["finished"], [item])
            self.__q.task_done()


if __name__ == "__main__":
    thread = CustomThreading(daemon=True)
    thread.name = "custom-thread"
    thread.start()
    
    while True:
        work = input("\n> ")
        for i in range(10):
            thread.put(f"{work}:{i}")
        if work == "q":
            plog(["done"])
            thread.wait()
            break
        if work == "s":
            plog(["stop"])
            thread.stop()
            break
