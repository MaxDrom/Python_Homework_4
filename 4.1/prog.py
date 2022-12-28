from random import uniform
from multiprocessing import Pool
from time import time
import math

def hard_job(_):
    x = uniform(1, 0.00001)
    y = uniform(1, 0.00001)
    return math.sqrt(-2*math.log(x))*math.cos(2*math.pi*y)

def get_times(func, count, args):
    cpu_count = 0
    while True:
        cpu_count+=1
        total_delta = 0
        for _ in range(count):
            pool = Pool(cpu_count)
            start_time = time()
            pool.map(func, args)
            total_delta+=(time() - start_time)
        yield (cpu_count+1, total_delta)

times = get_times(hard_job, 10, range(131072))
last_time = next(times)[-1]
cpu_count, next_time = next(times)
while last_time > next_time:
    last_time = next_time
    cpu_count, next_time = next(times)

print(cpu_count-1)
