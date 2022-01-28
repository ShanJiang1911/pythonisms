from functools import wraps
import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Used {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def test_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

print(test_time(10))

