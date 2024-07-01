def calc(line):
    operand_1, operation, operand_2 = line.split(' ')
    operand_1 = int(operand_1)
    operand_2 = int(operand_2)
    if operation == '*':
        print(f'Результат: {operand_1 * operand_2}')
    if operation == '/':
        print(f'Результат: {operand_1 / operand_2}')
    if operation == '+':
        print(f'Результат: {operand_1 + operand_2}')
    if operation == '-':
        print(f'Результат: {operand_1 - operand_2}')
    if operation == '//':
        print(f'Результат: {operand_1 // operand_2}')
    if operation == '%':
        print(f'Результат: {operand_1 % operand_2}')


cnt = 0
file_errors = 'errors.txt'
with open(file_errors, 'w') as reset_file:
    reset_file.write('_______________ОШИБКИ_______________')
with open(file_errors, 'a') as errors:
    with open('calc.txt', mode='r') as file:
        for line in file:
            cnt += 1
            try:
                calc(line)
            except ValueError as exc:
                if 'unpack' in exc.args[0]:
                    print(f'Ошибка в линии {cnt}, не хватает данных для ответа')
                    errors.write(f'\nОшибка в линии {cnt}, не хватает данных для ответа')
                else:
                    print(f'Ошибка в линии {cnt}, нельзя перевести в число')
                    errors.write(f'\nОшибка в линии {cnt}, нельзя перевести в число')
