#1.Timing Function Execution-
#Problem:-Write a decorator that measures the time a function takes to executes

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper

@timer  #here we want eg_time run but should pass from timer
def eg_func(n):
    time.sleep(n)

eg_func(2)