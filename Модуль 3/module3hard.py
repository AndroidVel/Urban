data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data):
    res = 0
    if isinstance(data, list) or isinstance(data, tuple) or isinstance(data, set):
        for i in data:
            res += calculate_structure_sum(i)
    elif isinstance(data, dict):
        for i, j in data.items():
            res += calculate_structure_sum(i) + calculate_structure_sum(j)
    elif isinstance(data, str):
        res += len(data)
    elif isinstance(data, int):
        res += data
    return res


result = calculate_structure_sum(data_structure)
print(result)
