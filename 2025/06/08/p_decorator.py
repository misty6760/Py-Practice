import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} start time: {end - start:.4f} sec")
        return result
    return wrapper

@timer
def compute():
    return sum(range(1000000))

compute()