from time import time
import requests


def decorator_max_2_params(func):
    def inner(*args, **kwargs):
        if len(args) + len(kwargs) > 2:
            raise ValueError("Write fewer than 2 args")
        return func(*args, **kwargs)
    return inner


def decorator_string_params(func):
    def inner(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, str):
                raise TypeError('All arguments must be strings')
        for value in kwargs.values():
            if not isinstance(value, str):
                raise TypeError('All argument values must be strings')
        return func(*args, **kwargs)
    return inner


def decorator_execution_time(func):
    def inner(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()

        print("Function executed in:", end_time - start_time, "seconds")
        return result

    return inner


@decorator_max_2_params
@decorator_string_params
@decorator_execution_time
def my_print(args, kwargs):
    for _ in range(10000000):
        pass
    for x in args, kwargs:
        print(x)


@decorator_execution_time
def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes


@decorator_execution_time
def show_time():
    start_time = time()
    r = requests.get('http://www.cnn.com')
    print(r.status_code)
    end_time = time()
    print(end_time - start_time)


my_print('hello', 'world')
find_primes(1, 10000)
show_time()
