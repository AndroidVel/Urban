import time
from telegram import ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters


async def start(update, context):
    buttons = [['Имя', 'Пользовательское имя'],
               ['Id', 'Язык телеграмма', 'Время']]
    keyboard = ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    await update.message.reply_text('hi', reply_markup=keyboard)


async def get_text(update, context):
    print(update.message.from_user.first_name + ':', update.message.text)
    time_ = time.localtime()
    data = {'имя': 'Вас зовут: ' + update.message.from_user.first_name,
            'id': 'Ваш id: ' + str(update.message.from_user.id),
            'язык телеграмма': 'Язык телеграмма на вашем устройстве: ' + update.message.from_user.language_code,
            'время': ('Время сейчас: ' + str(time_.tm_year) + '/' + str(time_.tm_mon) + '/' + str(time_.tm_mday) + ' ' +
                      str(time_.tm_hour) + ':' + str(time_.tm_min) + ':' + str(time_.tm_sec))}
    answer = data.get(update.message.text.lower())

    if answer:
        await update.message.reply_text(answer)
    elif update.message.text.lower() == 'пользовательское имя':
        if update.message.from_user.username:
            await update.message.reply_text('Ваше пользовательское имя: @' + update.message.from_user.username)
        else:
            await update.message.reply_text('У вас нет имя пользователя (@username)')
    else:
        await update.message.reply_text('Ваш текст не является командой \nВаш текст записан')


app = ApplicationBuilder().token("6763683828:AAHoisk9r_hAce6RMZDeRWpi0Z7C2ft5Cuc").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, get_text))
print('bot has started')
app.run_polling()
