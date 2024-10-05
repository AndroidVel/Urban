from aiogram import Bot, Dispatcher, executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import crud_functions


# Bot part
api = '8037489131:AAHD95EFitYTltm2an6IeVlde1Q7MsEMowk'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

crud_functions.initiate_db()
products = crud_functions.get_all_products()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


# Начальное меню
kb = ReplyKeyboardMarkup(resize_keyboard=True)
but_1 = KeyboardButton(text='Рассчитать')
but_2 = KeyboardButton(text='Регистрация')
but_3 = KeyboardButton(text='Купить')
kb.add(but_1)
kb.add(but_2)
kb.add(but_3)


# Кнопки под "Выберите опцию:"
in_kb = InlineKeyboardMarkup(resize_keyboard=True)
button_1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button_2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
in_kb.add(button_1, button_2)

# Кнопки под "Выберите продукт для покупки:"
in_kb_2 = InlineKeyboardMarkup()
for i in range(1, 5):
    in_kb_2.add(InlineKeyboardButton(text=f'Product{i}', callback_data='product_buying'))


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


# Регистрация
@dp.message_handler(text='Регистрация')
async def sign_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if crud_functions.is_included(message.text):
        await message.answer('Пользователь существует, введите другое имя')
        await RegistrationState.username.set()
    else:
        await state.update_data(username=message.text)
        await message.answer('Введите свой email:')
        await RegistrationState.email.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    crud_functions.add_user(data['username'], data['email'], data['age'])
    await message.answer('Регистрация успешно пройдена')
    await state.finish()


# Покупка товара
@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for k in range(1, 5):
        text = f'Название: {products[k - 1][1]} | Описание: {products[k - 1][2]} | Цена: {products[k - 1][3]}'
        with open(f'{k}.jpg', 'rb') as img:
            await message.answer_photo(img, text)
    await message.answer('Выберите продукт для покупки:', reply_markup=in_kb_2)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')


# Расчёт калорий
@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=in_kb)


@dp.callback_query_handler(text='calories')
async def main_menu(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.callback_query_handler(text='formulas')
async def main_menu(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()


@dp.message_handler(text='calories')
async def set_age(message):
    await message.answer('Введите свой возраст.')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def st_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    result = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5
    await message.answer(f'Ваша норма калорий: {result}')
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
