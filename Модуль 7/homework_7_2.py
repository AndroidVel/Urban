def custom_write(file_name, strings):
    dict_ = {}
    number_of_line = 0
    with open(file_name, 'w', encoding='utf-8') as file:
        for line in strings:
            number_of_line += 1
            dict_[(number_of_line, file.tell())] = line
            file.write(line + '\n')
    return dict_


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
