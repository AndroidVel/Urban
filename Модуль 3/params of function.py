def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(12, 'string', False)
print_params('str', c={1, 2, 3})
print_params(b='hello')
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [123, 'string', False]
values_dict = {'a': 132435, 'b': 'Kak dela?', 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [123, {1, 2}]
print_params(*values_list_2, 42)
