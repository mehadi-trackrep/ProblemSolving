import sys
from functools import wraps
from time import perf_counter

def memoize(func):
    cache = {}
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    
    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

if __name__=='__main__':
    sys.setrecursionlimit(10_000)
    start = perf_counter()
    print(fibonacci(2000))
    end = perf_counter()
    print(f'Time taken to execute the function is {end-start} seconds')