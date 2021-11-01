import datetime
import os

def decorator(path):
    def _decorator(old_function):
        def logger(*args, **kwargs):
            result = old_function(*args, **kwargs)
            with open(path, 'a', encoding='utf-8') as file:
                file.write(str(f'Дата вызова: {datetime.datetime.now()} '))
                file.write(f'Имя функции {old_function.__name__} ')
                file.write(str(f'Параметры: {args} {kwargs} '))
                file.write(str(f'Значение: {old_function(*args, *kwargs)} '))
                file.write(f'Путь логов: {os.getcwd()}\n')
            return result
        return logger
    return _decorator

