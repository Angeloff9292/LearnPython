# def hello_world():
#     print('Hello world')
# hello_world()

# hello2 = hello_world

# hello2()

# def hello_world1():
#     def internal():
#         print(f'hello world')
#     return internal

# hello2 = hello_world1()

# hello2()

# def say_something(func):
#     func()

# def hello_world2():
#     print('Hello world2')

# say_something(hello_world2)

def log_decorator(func):
    def wrap():
        print(f'Calling {func}')
        func()
        print(f'Func {func} finished its work')
    return wrap

# def hello():
#     print('Hello word')

# wrapped_by_logged = log_decorator(hello)

@log_decorator
def hello1():
    print('hello world 1')

hello1()

from timeit import default_timer as timer
import math
import time

def measure_time(func):
    def inner(*args, **kwargs):
        start = timer()

        func(*args, **kwargs)

        end = timer()

        print(f'Function {func.__name__} took {end-start} for execution')
    return inner

@measure_time
def factorial(num):
    time.sleep(3)
    print(math.factorial(num))

factorial(100)