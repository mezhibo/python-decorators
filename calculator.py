from datetime import datetime
from functools import wraps


def logger(path):
    def __logger(old_function):
        @wraps(old_function)
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)

            with open(path, 'a', encoding='utf-8') as log_file:
                log_file.write(
                    f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} | '
                    f'function: {old_function.__name__} | '
                    f'args: {args} | '
                    f'kwargs: {kwargs} | '
                    f'result: {result}\n'
                )

            return result
        return new_function
    return __logger


@logger('calculator.log')
def add(a, b):
    return a + b


@logger('calculator.log')
def sub(a, b):
    return a - b


@logger('calculator.log')
def mul(a, b):
    return a * b


@logger('calculator.log')
def div(a, b):
    return a / b


print(add(2, 3))
print(sub(10, 4))
print(mul(6, 7))
print(div(8, 2))
