def square(number):
    return number ** 2


def is_unpair(number):
    return number % 2 == 1


numbers = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
new_data = map(square, filter(is_unpair, numbers))
print(list(new_data))
