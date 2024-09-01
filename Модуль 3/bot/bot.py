from telegram import ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from datetime import datetime


class Memory:

    def __init__(self):
        self.elem = 0
        self.elem2 = 0


mem = Memory()


def log(text):
    with open('logs.txt', 'a', encoding='utf-8') as file:
        file.write(text + '\n')


def open_file():
    with open('info.txt', 'r') as file:
        lines = file.readlines()
        data = []
        for line in lines:
            line = ' '.join(line.split('|')).split()
            if line:
                if line[0].isalpha():
                    data.append(line[0] + ' ' + line[1])
                    for i in range(2, len(line)):
                        data.append(line[i])
                else:
                    data.append(line[0])
                    for i in range(1, len(line)):
                        data.append(line[i])
    return data


def write(what):
    keys = list(what.keys())
    values = list(what.values())
    result = [values[0]]
    for i in range(1, len(what)):
        result.append(keys[i] + ' ' + str(values[i]))
    return ' | '.join(result) + '\n'


def write_in_file(nastia, andrey):
    with open('/Модуль 3/info.txt', 'w') as file:
        file.write('Настя:\n')
        file.write(write(nastia.balance))
        file.write(write(nastia.earned))
        file.write(write(nastia.spent))
        file.write('\nАндрей:\n')
        file.write(write(andrey.balance))
        file.write(write(andrey.earned))
        file.write(write(andrey.spent))


class Nastia:
    def __init__(self):
        data = open_file()
        self.balance = {'name': data[1], data[2]: float(data[3]), data[4]: float(data[5]),
                        data[6]: float(data[7]), data[8]: float(data[9])}
        self.earned = {'name': data[10], data[11]: float(data[12]), data[13]: float(data[14]),
                       data[15]: float(data[16]), data[17]: float(data[18])}
        self.spent = {'name': data[19], data[20]: float(data[21]), data[22]: float(data[23]),
                      data[24]: float(data[25]), data[26]: float(data[27])}


class Andrey:
    def __init__(self):
        data = open_file()
        self.balance = {'name': data[29], data[30]: float(data[31]), data[32]: float(data[33]),
                        data[34]: float(data[35]), data[36]: float(data[37])}
        self.earned = {'name': data[38], data[39]: float(data[40]), data[41]: float(data[42]),
                       data[43]: float(data[44]), data[45]: float(data[46])}
        self.spent = {'name': data[47], data[48]: float(data[49]), data[50]: float(data[51]),
                      data[52]: float(data[53]), data[54]: float(data[55])}


n = Nastia()
a = Andrey()


def is_float(string):
    try:
        # float() is a built-in function
        float(string)
        return True
    except ValueError:
        return False


async def start(update, context):
    buttons = [['Информация'],
               ['Потратить', 'Пополнить счёт']]
    keyboard = ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    await update.message.reply_text('бот запущен\nВсе данные сохраняются в текстовый файл', reply_markup=keyboard)


async def get_text(update, context):
    print(update.message.from_user.first_name + ':', update.message.text)
    request = update.message.text.lower()

    # match request:
    #     case 'potato':
    #         pass
    #
    if request == 'информация':
        with open('info.txt', 'r') as file:
            file_content = file.read()
        await update.message.reply_text(file_content)
    elif request == 'пополнить счёт':
        mem.elem = request
        await update.message.reply_text('Введите валюту пополняемых денег\n'
                                        '(CHF, EURO, USD, RUB)')
    elif request == 'потратить':
        mem.elem = request
        await update.message.reply_text('Введите валюту потраченных денег\n'
                                        '(CHF, EURO, USD, RUB)')
    elif request in 'chfeurousdrub':
        mem.elem2 = request.upper()
        await update.message.reply_text('Введите число денег\n'
                                        '(Пример: 123.45)')
    elif is_float(request) or request.isnumeric():
        if mem.elem == 'пополнить счёт':
            if update.message.from_user.username == 'Nobelevskyi_laureat':
                a.earned[f'{mem.elem2}:'] += float(request)
                a.balance[f'{mem.elem2}:'] += float(request)
                await update.message.reply_text(f'Пополнено на {request} {mem.elem2}')
                log(f'[{datetime.now()}]: {update.message.from_user.first_name} заработал {request} {mem.elem2}')
            elif update.message.from_user.username == 'Tcheburachka':
                n.earned[f'{mem.elem2}:'] += float(request)
                n.balance[f'{mem.elem2}:'] += float(request)
                await update.message.reply_text(f'Пополнено на {request} {mem.elem2}')
                log(f'[{datetime.now()}]: {update.message.from_user.first_name} заработал {request} {mem.elem2}')
            else:
                await update.message.reply_text('Вас нет в списке')
        elif mem.elem == 'потратить':
            if update.message.from_user.username == 'Nobelevskyi_laureat':
                a.spent[f'{mem.elem2}:'] += float(request)
                a.balance[f'{mem.elem2}:'] -= float(request)
                await update.message.reply_text(f'Потрачено {request} {mem.elem2}')
                log(f'[{datetime.now()}]: {update.message.from_user.first_name} потратил {request} {mem.elem2}')
            elif update.message.from_user.username == 'Tcheburachka':
                n.spent[f'{mem.elem2}:'] += float(request)
                n.balance[f'{mem.elem2}:'] -= float(request)
                await update.message.reply_text(f'Потрачено {request} {mem.elem2}')
                log(f'[{datetime.now()}]: {update.message.from_user.first_name} потратил {request} {mem.elem2}')
            else:
                await update.message.reply_text('Вас нет в списке')
        write_in_file(nastia=n, andrey=a)
        with open('info.txt', 'r') as file:
            file_content = file.read()
        await update.message.reply_text(file_content)
    else:
        await update.message.reply_text('Ваш текст не является командой \nВаш текст записан')


app = ApplicationBuilder().token("6763683828:AAHoisk9r_hAce6RMZDeRWpi0Z7C2ft5Cuc").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, get_text))
print('bot has started')
app.run_polling()
