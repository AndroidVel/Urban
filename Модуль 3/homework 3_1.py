def test():
    a = 12
    b = 'String'
    print(a, b)


def test2 (a=12, b=True, c='abc'):
    print(a, b, c)


test()
test2(23, c='Hello')
