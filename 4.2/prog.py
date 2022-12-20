from queue import Queue
from threading import Thread, enumerate
from random import uniform
import math
from time import sleep

class Worker:
    def __init__(self, *args, **kwargs):
        thread = Thread(name=type(self).name, target=self, args = args, kwargs= kwargs)
        thread.start()

class Sender(Worker):
    name = "sender"
    def __init__(self, n ,queue: Queue):
        self.n = n
        super().__init__(queue)
    def __call__(self, queue: Queue):
        for _ in range(self.n):
            t = uniform(0.2, 1)
            sleep(t)
            queue.put(uniform(0, 2*math.pi))

class Receiver(Worker):
    name = "receiver"
    def __init__(self, queue: Queue):
        super().__init__(queue)
    
    def __call__(self, queue: Queue):
        count = 1
        while any(th.is_alive() for th 
            in enumerate()
            if th.name == Sender.name) or not queue.empty():
            if not queue.empty():
                print(count,math.sin(queue.get()))
                count+=1


q = Queue()
for _ in range(10):
    sender = Sender(5,q)
receiver = Receiver(q)