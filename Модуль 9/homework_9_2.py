# Задача 1: Фабрика Функций
def operator(operation):
    if operation.lower() == 'add':
        def add(a, b):
            return a + b
        return add
    elif operation.lower() == 'subtract':
        def subtract(a, b):
            return a - b
        return subtract
    elif operation.lower() == 'multiply':
        def multiply(a, b):
            return a * b
        return multiply
    elif operation.lower() == 'divide':
        def divide(a, b):
            return a / b
        return divide


add_numbers = operator('Add')
print(add_numbers(222, 278))
subtract_numbers = operator('SuBtRACt')
print(subtract_numbers(10356, 356))
multiply_numbers = operator('MULTIPLY')
print(multiply_numbers(12345679, 63))
divide_numbers = operator('divide')
print(divide_numbers(714212835, 7))

# Задача 2: Лямбда-Функции
number_square = lambda a, n: a ** n
print(number_square(5, 3))


def number_square_def(a, n):
    return a ** n


print(number_square_def(2, 10))


# Задача 3: Вызываемые Объекты
class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b


rect_1 = Rect(10, 25)
print(rect_1.__call__())
rect_2 = Rect(25, 20)
print(rect_2.__call__())
