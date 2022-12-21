from queue import Queue
from threading import Thread, enumerate
from random import uniform
from time import sleep
import math


class Sender(Thread):
    def __init__(self, n ,queue: Queue):
        super().__init__()
        self.n = n
        self.queue = queue
    
    def run(self):
        for i in range(self.n):
            t = uniform(0.2, 1)
            sleep(t)
            self.queue.put((self.name ,uniform(0, 2*math.pi)))

class Receiver(Thread):
    def __init__(self, queue: Queue):
        super().__init__()
        self.queue = queue
    
    def run(self):
        while any(th.is_alive() for th in enumerate() if isinstance(th, Sender)) or not self.queue.empty():
            if not self.queue.empty():
                name, x = self.queue.get()
                print(name, math.sin(x))

q = Queue()
for _ in range(10):
    sender = Sender(5,q)
    sender.start()
receiver = Receiver(q)
receiver.start()
