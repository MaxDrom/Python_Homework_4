from random import uniform
import math
def hard_job(_):
    x = uniform(1, 0.00001)
    y = uniform(1, 0.00001)
    return math.sqrt(-2*math.log(x))*math.cos(2*math.pi*y)

from multiprocessing import Pool
from datetime import datetime

def get_times(func, count, args):
    cpu_count =0
    while True:
        cpu_count+=1
        total_delta = 0
        for _ in range(count):
            pool = Pool(cpu_count)
            start_time = datetime.now()
            pool.map(func, args)
            total_delta+=(datetime.now() - start_time).total_seconds()**2
        total_delta = math.sqrt(total_delta)
        yield (cpu_count+1, total_delta)

times = get_times(hard_job, 100, range(1, 1024))
last_time = next(times)[-1]
cpu_count, next_time = next(times)
while last_time > next_time:
    last_time = next_time
    cpu_count, next_time = next(times)

print(cpu_count-1)