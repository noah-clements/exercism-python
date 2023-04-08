from functools import wraps
from time import time


def measure(func):
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = time() * 1000
        try:
            return func(*args, **kwargs)
        finally:
            end_ = time() * 1000 - start
            print(f"Total execution time: {end_} ms")
    return _time_it

# @measure
def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    # return 2 ** (number - 1)
    return 1 << (number - 1)

# @measure
def total():
    # return 2 ** 64 - 1
    return (1 << 64) - 1

# 1 << n tests faster than 2 ** n, for any n. 
# Does this matter - prolly not.
@measure
def main():
    for _ in range(1_000_000):
        for i in range(1, 30):
            square(i)
        # total()
    
if __name__ == "__main__":
    main()