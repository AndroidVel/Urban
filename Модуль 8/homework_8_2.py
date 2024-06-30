class InvalidTypeException(Exception):
    def __init__(self, exception, more_info):
        self.exception = exception
        self.more_info = more_info


class ProcessingException(Exception):
    pass


def summ(a, b):
    try:
        if isinstance(a, int) and isinstance(b, int):
            return a + b
        else:
            raise InvalidTypeException('Неверный тип данных', 'Разрешены только целые числа')
    except InvalidTypeException as exc:
        print(f'Произошла ошибка: {exc.exception} - {exc.more_info}')
        raise ProcessingException()


try:
    print(summ(123, 135))
    print(summ(123, 1.5))
    print(summ('123', 135))
except ProcessingException:
    print('Что-то пошло не так')
finally:
    print('программа дошла до конца')
