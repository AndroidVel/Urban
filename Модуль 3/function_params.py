def test(*num, **dicti):
    print(num)
    print(dicti)


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


test(1, 4, text='string', number=123)


print(factorial(5))
print(factorial(10))
