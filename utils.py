import time
from functools import wraps


def timeit(func):
    """
    Use this decorator on a method to find it's execution time.
    :param func:
    :return:
    """
    @wraps(func)
    def time_and_log(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"func: {func.__name__} took a total of {end-start} sec to run")
        return result
    return time_and_log
