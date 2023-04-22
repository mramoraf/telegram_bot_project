from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keyboards import *
import urls
from aiogram.dispatcher import FSMContext

import os
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv('TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


async def set_default_commands(dp):
    await bot.set_my_commands(
        [
            types.BotCommand('start', 'Запустити бота'),
            types.BotCommand('sections', 'Обрати секцію'),
            
        ]
    )



# @dp.message_handler(commands='start')
# async def start(message:types.message):
    
#     await message.answer(text='Привіт! Я - бот, який допоможе тобі з практикою англійської мови📝')
    
   


# dp.message_handler(commands='choose_section')
# async def choose(message: types.Message, state:FSMContext):
#     kb = [
#         [types.KeyboardButton('listening'),types.KeyboardButton('reading')],
#         [types.KeyboardButton('grammar'), types.KeyboardButton('use of English')],
#         [types.KeyboardButton('level test')]
#     ]
#     keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, selective=True)
#     await message.answer(text='Обирай секцію, яка тебе цікавить і давай починати!😼', reply_markup=keyboard)
#     await state.set_state('choose_type_of_task')






@dp.message_handler(commands='start')
async def start(message:types.message, state:FSMContext):
    kb = [
        [types.KeyboardButton('listening'),types.KeyboardButton('reading')],
        [types.KeyboardButton('grammar'), types.KeyboardButton('use of English')],
        [types.KeyboardButton('level test')]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, selective=True)
    await message.answer(text='Привіт! Я - бот, який допоможе тобі з практикою англійської мови📝\nОбирай секцію, яка тебе цікавить і давай починати!😼', reply_markup=keyboard)
    await state.set_state('choose_type_of_task')
    
    
    







@dp.message_handler(content_types=['text'], state='choose_type_of_task')
async def choose_section(message:types.message, state=FSMContext):
    if message.text == 'listening':
        kb = [
            [types.KeyboardButton('Відео з субтитрами на різні теми'), types.KeyboardButton('Практичні завдання з темою на вибір')],
            [types.KeyboardButton('Короткі відео з субтитрами для різного рівня'), types.KeyboardButton('Практика на англомовних піснях')]
        ]
        keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, selective=True)
        await message.answer(text='Супер! А тепер обери варіант як би ти хотів практикувати свій лісенінг💪🏿', reply_markup=keyboard)
        await state.set_state('choose_task')
    elif message.text == 'reading':
        url1 = my_urls['reading']['url1']
        url2 = my_urls['reading']['url2']
        my_message = f'Добре! Тримай посилання на сайти з різноманітними завданнями на різні теми та рівні для практики твого рідінгу😎:\n1️⃣{url1}\n2️⃣{url2}'
        await message.answer(text=my_message)
        await message.answer(text='*щоб переобрати секцію або тип завдання, обери команду sections в меню')
        await state.finish()
    elif message.text == 'grammar':
        kb = [
            [types.KeyboardButton('tenses'), types.KeyboardButton('modal verbs'), types.KeyboardButton('prepositions')],
            [types.KeyboardButton('If clauses'), types.KeyboardButton('passive voice'), types.KeyboardButton('gerund - infinitive')]
        ]
        keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, selective=True)
        await message.answer(text='Чудово! Тепер визначись з темою яка тобі потрібна🤝🏿', reply_markup=keyboard)
        await state.set_state('choose_task')
    elif message.text == 'use of English':
        kb = [
            [types.KeyboardButton('general vocabulary exercises'), types.KeyboardButton('word formation'), types.KeyboardButton('various exercises')]
        ]
        keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, selective=True)
        await message.answer(text='Файно! Тепер обери які саме вправи ти хочеш робити👀', reply_markup=keyboard)
        await state.set_state('choose_task')
    elif message.text == 'level test':
        url = my_urls['level_test']['url']
        my_message2 = f'Ще не знаєш свій рівень? Тоді лови посилання на тест для визначення твоїх знань в англійській мові💡\n{url}'
        await message.answer(text=my_message2)
        await message.answer(text='*щоб переобрати секцію або тип завдання, обери команду sections в меню')
        await state.finish()
    else:
        await message.answer(text='Вибач, але такої секції не знайдено😢')








@dp.message_handler(commands='sections')
async def choose_section_again(message: types.message, state:FSMContext):
    kb = [

        [types.KeyboardButton('listening'),types.KeyboardButton('reading')],
        [types.KeyboardButton('grammar'), types.KeyboardButton('use of English')],
        [types.KeyboardButton('level test')]
    
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, selective=True)
    await message.answer(text='Обери секцію, яка тебе цікавить', reply_markup=keyboard)
    await state.set_state('choose_type_of_task')
    








@dp.message_handler(content_types=['text'], state='choose_task')
async def choose_exercise(message: types.message, state:FSMContext):
    if message.text == 'Відео з субтитрами на різні теми':
        the_url = my_urls['listening']['url1']
        my_message = f'Ororo - це ресурс де ти можеш дивитися епізоди різноманітних шоу та програм на не дуже високому рівні знання мови з англійськими субтитрами📰\n{the_url}'
        await message.answer(text=my_message)
        await message.answer(text='*щоб переобрати секцію або тип завдання, обери команду sections в меню')
        await state.finish()
    elif message.text == 'Практичні завдання з темою на вибір':
        the_url = my_urls['listening']['url2']
        my_message = f'Цей сайт допоможе тобі краще розуміти секцію лісенінг та як краще з нею працювати🗃️\n{the_url}'
        await message.answer(text=my_message)
        await message.answer(text='*щоб переобрати секцію або тип завдання, обери команду sections в меню')
        await state.finish()
    elif message.text == 'Короткі відео з субтитрами для різного рівня':
        the_url = my_urls['listening']['url3']
        my_message = f'EnglishCentral - місце де ти зможеш попрактикуватися якщо в тебе не так багато часу, бо відео там зазвичай не довше ніж 2 хв⏱️\n{the_url}'
        await message.answer(text=my_message)
        await message.answer(text='*щоб переобрати секцію або тип завдання, обери команду sections в меню')
        await state.finish()
    elif message.text == 'Практика на англомовних піснях':
        the_url = my_urls['listening']['url4']
        my_message = f'Lyricstraining створений для істинних фанатів музики. Завдяки цьому ресурсу ти маєш можливість слухати улюбленні пісні та одночасно покращувати своє розуміння англійської на слух🎶\n{the_url}'
        await message.answer(text=my_message)
        await message.answer(text='*щоб переобрати секцію або тип завдання, обери команду sections в меню')
        await state.finish()
    elif message.text == 'tenses':
        the_url = my_urls['grammar']['url1']
        my_message = f'Тут зібрані  вправи по всіх часах в англійській 🖇️\n{the_url}'
        await message.answer(text=my_message)
        await message.answer(text='*щоб переобрати секцію або тип завдання, обери команду sections в меню')
        await state.finish()
    elif message.text == 'modal verbs':
        the_url = my_urls['grammar']['url2']
        my_message = f'Ось тут ти знайдеш вправи на будь-які форми модальних дієслів📌\n{the_url}'
        await message.answer(text=my_message)
        await message.answer(text='*щоб переобрати секцію або тип завдання, обери команду sections в меню')
        await state.finish()
    elif message.text == 'prepositions':
        the_url = my_urls['grammar']['url3']
        my_message = f'Перейшовши за цим посиланням ти знайдеш більш ніж достатньо вправ на прийменники📖\n{the_url}'
        await message.answer(text=my_message)
        await message.answer(text='*щоб переобрати секцію або тип завдання, обери команду sections в меню')
        await state.finish()
    elif message.text == 'If clauses':
        the_url = my_urls['grammar']['url4']
        my_message = f'На тебе вже чекають, на перший погляд, такі незрозумілі кондішиналси🫡\n{the_url}'
        await message.answer(text=my_message)
        await message.answer(text='*щоб переобрати секцію або тип завдання, обери команду sections в меню')
        await state.finish()
    elif message.text == 'passive voice':
        the_url = my_urls['grammar']['url5']
        my_message = f'Лови трохи вправ на пасиви✏️\n{the_url}'
        await message.answer(text=my_message)
        await message.answer(text='*щоб переобрати секцію або тип завдання, обери команду sections в меню')
        await state.finish()
    elif message.text == 'gerund - infinitive':
        the_url = my_urls['grammar']['url6']
        my_message = f'Обравши цю тему, я вже можу зрозуміти що ти досить хоробра людина🤔\n{the_url}'
        await message.answer(text=my_message)
        await message.answer(text='*щоб переобрати секцію або тип завдання, обери команду sections в меню')
        await state.finish()
    elif message.text == 'general vocabulary exercises':
        the_url = my_urls['use_of_english']['url3']
        my_message = f'Тримай, тут є досить багато завдань для практики словникового запасу📚\n{the_url}'
        await message.answer(text=my_message)
        await message.answer(text='*щоб переобрати секцію або тип завдання, обери команду sections в меню')
        await state.finish()
    elif message.text == 'word formation':
        the_url = my_urls['use_of_english']['url2']
        my_message = f'Тут знайдеш предостатньо завдань на відточення навичків словотворення✏️\n{the_url}'
        await message.answer(text=my_message)
        await message.answer(text='*щоб переобрати секцію або тип завдання, обери команду sections в меню')
        await state.finish()
    elif message.text == 'various exercises':
        the_url = my_urls['use_of_english']['url1']
        my_message = f'Ось збірка досить різноманітних вправ для практики цієї секції🗂️\n{the_url}'
        await message.answer(text=my_message)
        await message.answer(text='*щоб переобрати секцію або тип завдання, обери команду sections в меню')
        await state.finish()
        
        
        




async def on_startup(dp):
    await set_default_commands(dp)




if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
