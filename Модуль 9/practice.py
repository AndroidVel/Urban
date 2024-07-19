animal = 'мишка'
animals = ['зайка', 'мишка', 'бегемотик']


# 1

def gen_repeat(n):

    def repeat(animal):

        return (animal[:2] + '-') * n + animal

    return repeat


test_1 = gen_repeat(1)
test_2 = gen_repeat(3)
print(test_1(animal))
print(test_2(animal))


# 2

repetitions = [gen_repeat(n) for n in range(1, 4)]
print(repetitions)

result = [func(animal) for func in repetitions]
print(result)


# 3
fin_result = [func(x) for func in repetitions for x in animals]
fin_result2 = [func(x) for x in animals for func in repetitions]
print(fin_result)
print(fin_result2)


# 4

def memorise_func(f):
    mem = {}

    def wrapper(*args):
        print(f'Выполнение функции с аргументами={args}, внутренняя память={mem}')
        if args not in mem:
            mem[args] = f(*args)
            return f'Функция выполнилась, ответ = {mem[args]}'
        else:
            return f'Функция уже была выполнена, ответ = {mem[args]}'
    return wrapper


@memorise_func
def func(a, b):
    print(f'Выполняем функцию с аргументами ({a}, {b})')
    return a ** b


print(func(3, 5), '\n')
print(func(3, 4), '\n')
print(func(3, 2), '\n')
print(func(3, 5), '\n')
print(func(3, 4), '\n')
print(func(3, 5), '\n')
