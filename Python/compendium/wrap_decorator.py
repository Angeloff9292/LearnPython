# def log_decorator(func):
#     def wrap():
#         print(f'Calling {func}')
#         func()
#         print(f'Func {func} finished its work')
#     return wrap

# @log_decorator
# def hello():
#     print('Hello, world')

# hello()


from functools import wraps

def log_decorator1(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        print(f'Calling {func}')
        func(*args, **kwargs)
        print(f'Func {func} finished its work')
    return wrap

@log_decorator1
def hello1():
    print('Hello, world')

help(hello1)

