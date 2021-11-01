import datetime


def decorator(old_function):

    def logger(*args, **kwargs):
        result = old_function(*args, **kwargs)
        with open('loger.txt', 'a') as file:
            file.write(str(f'Дата вызова: {datetime.datetime.now()} '))
            file.write(f'Имя функции {old_function.__name__} ')
            file.write(str(f'Параметры: {args} {kwargs} '))
            file.write(str(f'Значение: {old_function(*args, *kwargs)} '))

        return result

    return logger