import asyncio
import types
from datetime import datetime, timedelta, time
import locale
from gc import callbacks
from mailbox import Message

import telebot

API_KEY = '6993939795:AAEKdJGX4IfWw5S7m-DMUBpEm7QG_Z1CslI'
locale.setlocale(
    category=locale.LC_ALL,
    locale="Russian"  # Note: do not use "de_DE" as it doesn't work
)
keyboard9 = telebot.types.InlineKeyboardMarkup()
keyboard9.row(
    telebot.types.InlineKeyboardButton('← Вернуться', callback_data='vern3')
)
keyboard8 = telebot.types.InlineKeyboardMarkup()
keyboard8.row(
telebot.types.InlineKeyboardButton('Понедельник', callback_data='Poned1'),
              telebot.types.InlineKeyboardButton('Вторник', callback_data='Vtorn1'),
              telebot.types.InlineKeyboardButton('Среда', callback_data='Sreda1'),
              telebot.types.InlineKeyboardButton('Четверг', callback_data='Chetverg1'),
              telebot.types.InlineKeyboardButton('Пятница', callback_data='Pyatnica1')
)
keyboard8.row(
    telebot.types.InlineKeyboardButton('← Вернуться', callback_data='vern2')
)
keyboard7 = telebot.types.InlineKeyboardMarkup()
keyboard7.row(
    telebot.types.InlineKeyboardButton('Расписание уроков', callback_data='lessons')
)
keyboard7.row(
    telebot.types.InlineKeyboardButton('Расписание всех уроков', callback_data='lessonsall')
)
keyboard7.row(
    telebot.types.InlineKeyboardButton('Расписание всех звонков', callback_data='calls')
)
keyboard = telebot.types.InlineKeyboardMarkup()
keyboard2 = telebot.types.InlineKeyboardMarkup()
keyboard2.row(
    telebot.types.InlineKeyboardButton('← Вернуться', callback_data='vern')
)
keyboard3 = telebot.types.InlineKeyboardMarkup()
keyboard3.row(
    telebot.types.InlineKeyboardButton('Перейти в расписание →', callback_data='vern')
)
keyboard5 = telebot.types.InlineKeyboardMarkup()
keyboard5.row(
    telebot.types.InlineKeyboardButton('← Вернуться', callback_data='vern1')
)
keyboard6 = telebot.types.InlineKeyboardMarkup()
keyboard6.row(
    telebot.types.InlineKeyboardButton('Перейти в расписание →', callback_data='vern1')
)
keyboard4 = telebot.types.InlineKeyboardMarkup()
keyboard4.row(
    telebot.types.InlineKeyboardButton('Вчера', callback_data='vchera'),
    telebot.types.InlineKeyboardButton('Сегодня', callback_data='segodnya'),
    telebot.types.InlineKeyboardButton('Завтра', callback_data='zavtra'))
keyboard4.row(
    telebot.types.InlineKeyboardButton('← Вернуться', callback_data='vern2')
)
keyboard.row( telebot.types.InlineKeyboardButton('Понедельник', callback_data='Poned'),
              telebot.types.InlineKeyboardButton('Вторник', callback_data='Vtorn'),
              telebot.types.InlineKeyboardButton('Среда', callback_data='Sreda'),
              telebot.types.InlineKeyboardButton('Четверг', callback_data='Chetverg'),
              telebot.types.InlineKeyboardButton('Пятница', callback_data='Pyatnica')
              )
keyboard.row(
    telebot.types.InlineKeyboardButton('← Вернуться', callback_data='vern2')
)
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start', 'lessons'], )
def start(message):
    day = datetime.today().strftime('%A')
    bot.send_message(message.from_user.id, f'Выбери нужный раздел: 🌎', reply_markup=keyboard7)

@bot.message_handler(commands=['help'], )
def help(message):
    bot.send_message(message.from_user.id, f'Есть вопросы? Обратись к @qwaaantex', reply_markup=keyboard6)
@bot.callback_query_handler(func=lambda call: True)
def callback(callback):
    nextday = datetime.today() - timedelta(days=1)
    nextday1 = nextday.isoweekday()
    lastday = datetime.today() + timedelta(days=1)
    lastday1 = lastday.isoweekday()
    chat_id = callback.message.chat.id
    message_id = callback.message.message_id
    if callback.data == 'Poned':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Расписание на Понедельник:\n---------------------------------\n1. Классный час (38)\n2. Русский язык (34)\n3. Технология (31)\n4. Алгебра (11)\n5. Физика (к/ф)', reply_markup=keyboard2, parse_mode='Markdown')
    elif callback.data == 'vern1':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Выбери нужный день: 🌎', reply_markup=keyboard4, parse_mode='Markdown')
    elif callback.data == 'vern':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Выбери нужный день: 🌎', reply_markup=keyboard, parse_mode='Markdown')
    elif callback.data == 'Vtorn':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Расписание на Вторник:\n---------------------------------\n1. Физкультура (к/ф)\n2. География (36)\n3. Алгебра (11)\n4. Обзр (38)\n5. Литература (26)\n6. Химия (к/х)', reply_markup=keyboard2, parse_mode='Markdown')
    elif callback.data == 'Sreda':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Расписание на Среду:\n---------------------------------\n1. Обществознание (16)\n2. Алгебра (11)\n3. Биология (37)\n4. Английский язык (42/44)\n5. Физика (к/ф)\n6. Русский язык (34)', reply_markup=keyboard2, parse_mode='Markdown')
    elif callback.data == 'Chetverg':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Расписание на Четверг:\n---------------------------------\n1. Классный час (38)\n2. Геометрия (11)\n3. Физкультура (к/ф)\n4. Вис (11)\n5. Английский язык (42/44)\n6. Русский язык (34)', reply_markup=keyboard2, parse_mode='Markdown')
    elif callback.data == 'Pyatnica':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Расписание на Пятницу:\n---------------------------------\n1. География (36)\n2. Геометрия (11)\n3. Литература (15)\n4. Биология (37)', reply_markup=keyboard2, parse_mode='Markdown')
    elif callback.data == 'vchera' and nextday1 == 1:
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Расписание на Понедельник:\n---------------------------------\n1. Классный час (38)\n2. Русский язык (34)\n3. Технология (31)\n4. Алгебра (11)\n5. Физика (к/ф)', reply_markup=keyboard5, parse_mode='Markdown')
    elif callback.data == 'vchera' and nextday1 == 2:
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Расписание на Вторник:\n---------------------------------\n1. Физкультура (к/ф)\n2. География (36)\n3. Алгебра (11)\n4. Обзр (38)\n5. Литература (26)\n6. Химия (к/х)', reply_markup=keyboard5, parse_mode='Markdown')
    elif callback.data == 'vchera' and nextday1 == 3:
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Расписание на Среду:\n---------------------------------\n1. Обществознание (16)\n2. Алгебра (11)\n3. Биология (37)\n4. Английский язык (42/44)\n5. Физика (к/ф)\n6. Русский язык (34)', reply_markup=keyboard5, parse_mode='Markdown')
    elif callback.data == 'vchera' and nextday1 == 4:
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Расписание на Четверг:\n---------------------------------\n1. Классный час (38)\n2. Геометрия (11)\n3. Физкультура (к/ф)\n4. Вис (11)\n5. Английский язык (42/44)\n6. Русский язык (34)', reply_markup=keyboard5, parse_mode='Markdown')
    elif callback.data == 'vchera' and nextday1 == 5:
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Расписание на Пятницу:\n---------------------------------\n1. География (36)\n2. Геометрия (11)\n3. Литература (15)\n4. Биология (37)', reply_markup=keyboard5, parse_mode='Markdown')
    elif callback.data == 'vchera' and nextday1 == 6:
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Расписание на Субботу:\n---------------------------------\nНету!', reply_markup=keyboard5, parse_mode='Markdown')
    elif callback.data == 'vchera' and nextday1 == 7:
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Расписание на Воскресенье:\n---------------------------------\nНету!', reply_markup=keyboard5, parse_mode='Markdown')
    elif callback.data == 'segodnya' and datetime.today().isoweekday() == 1:
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Расписание на Понедельник:\n---------------------------------\n1. Классный час (38)\n2. Русский язык (34)\n3. Технология (31)\n4. Алгебра (11)\n5. Физика (к/ф)', reply_markup=keyboard5, parse_mode='Markdown')
    elif callback.data == 'segodnya' and datetime.today().isoweekday() == 2:
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Расписание на Вторник:\n---------------------------------\n1. Физкультура (к/ф)\n2. География (36)\n3. Алгебра (11)\n4. Обзр (38)\n5. Литература (26)\n6. Химия (к/х)', reply_markup=keyboard5, parse_mode='Markdown')
    elif callback.data == 'segodnya' and datetime.today().isoweekday() == 3:
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Расписание на Среду:\n---------------------------------\n1. Обществознание (16)\n2. Алгебра (11)\n3. Биология (37)\n4. Английский язык (42/44)\n5. Физика (к/ф)\n6. Русский язык (34)', reply_markup=keyboard5, parse_mode='Markdown')
    elif callback.data == 'segodnya' and datetime.today().isoweekday() == 4:
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Расписание на Четверг:\n---------------------------------\n1. Классный час (38)\n2. Геометрия (11)\n3. Физкультура (к/ф)\n4. Вис (11)\n5. Английский язык (42/44)\n6. Русский язык (34)', reply_markup=keyboard5, parse_mode='Markdown')
    elif callback.data == 'segodnya' and datetime.today().isoweekday() == 5:
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Расписание на Пятницу:\n---------------------------------\n1. География (36)\n2. Геометрия (11)\n3. Литература (15)\n4. Биология (37)', reply_markup=keyboard5, parse_mode='Markdown')
    elif callback.data == 'segodnya' and datetime.today().isoweekday() == 6:
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Расписание на Субботу:\n---------------------------------\nНету!', reply_markup=keyboard5, parse_mode='Markdown')
    elif callback.data == 'segodnya' and datetime.today().isoweekday() == 7:
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Расписание на Воскресенье:\n---------------------------------\nНету!', reply_markup=keyboard5, parse_mode='Markdown')
    elif callback.data == 'zavtra' and lastday1 == 1:
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Расписание на Понедельник:\n---------------------------------\n1. Классный час (38)\n2. Русский язык (34)\n3. Технология (31)\n4. Алгебра (11)\n5. Физика (к/ф)', reply_markup=keyboard5, parse_mode='Markdown')
    elif callback.data == 'zavtra' and lastday1 == 2:
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Расписание на Вторник:\n---------------------------------\n1. Физкультура (к/ф)\n2. География (36)\n3. Алгебра (11)\n4. Обзр (38)\n5. Литература (26)\n6. Химия (к/х)', reply_markup=keyboard5, parse_mode='Markdown')
    elif callback.data == 'zavtra' and lastday1 == 3:
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Расписание на Среду:\n---------------------------------\n1. Обществознание (16)\n2. Алгебра (11)\n3. Биология (37)\n4. Английский язык (42/44)\n5. Физика (к/ф)\n6. Русский язык (34)', reply_markup=keyboard5, parse_mode='Markdown')
    elif callback.data == 'zavtra' and lastday1 == 4:
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Расписание на Четверг:\n---------------------------------\n1. Классный час (38)\n2. Геометрия (11)\n3. Физкультура (к/ф)\n4. Вис (11)\n5. Английский язык (42/44)\n6. Русский язык (34)', reply_markup=keyboard5, parse_mode='Markdown')
    elif callback.data == 'zavtra' and lastday1 == 5:
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Расписание на Пятницу:\n---------------------------------\n1. География (36)\n2. Геометрия (11)\n3. Литература (15)\n4. Биология (37)', reply_markup=keyboard5, parse_mode='Markdown')
    elif callback.data == 'zavtra' and lastday1 == 6:
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Расписание на Субботу:\n---------------------------------\nНету!', reply_markup=keyboard5, parse_mode='Markdown')
    elif callback.data == 'zavtra' and lastday1 == 7:
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Расписание на Воскресенье:\n---------------------------------\nНету!', reply_markup=keyboard5, parse_mode='Markdown')
    elif callback.data == 'lessons':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Выбери нужный день: 🌎', reply_markup=keyboard4, parse_mode='Markdown')
    elif callback.data == 'lessonsall':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Выбери нужный день: 🌎', reply_markup=keyboard, parse_mode='Markdown')
    elif callback.data == 'calls':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Выбери нужный день: 🌎', reply_markup=keyboard8, parse_mode='Markdown')
    elif callback.data == 'vern2':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Выбери нужный раздел: 🌎', reply_markup=keyboard7, parse_mode='Markdown')
    elif callback.data == 'vern3':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Выбери нужный день: 🌎', reply_markup=keyboard8, parse_mode='Markdown')
    elif callback.data == 'Poned1':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Расписание на Понедельник:\n---------------------------------\n1. 08:30-9:00\n2. 09:05-09:45\n3. 10:00-10:40\n4. 10:55-11:35\n5. 11:50-12:30\n6. 12:40-13:20\n7. 13:30-14:10\n8. 14:15-14:55', reply_markup=keyboard9, parse_mode='Markdown')
    elif callback.data == 'Vtorn1':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Расписание на Вторник:\n---------------------------------\n1. 08:30-9:10\n2. 09:20-10:00\n3. 10:15-10:55\n4. 11:10-11:50\n5. 12:05-12:45\n6. 12:55-13:35\n7. 13:45-14:25\n8. 14:30-15:10', reply_markup=keyboard9, parse_mode='Markdown')
    elif callback.data == 'Sreda1':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Расписание на Среду:\n---------------------------------\n1. 08:30-9:10\n2. 09:20-10:00\n3. 10:15-10:55\n4. 11:10-11:50\n5. 12:05-12:45\n6. 12:55-13:35\n7. 13:45-14:25\n8. 14:30-15:10', reply_markup=keyboard9, parse_mode='Markdown')
    elif callback.data == 'Chetverg1':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Расписание на Четверг:\n---------------------------------\n1. 08:30-9:10\n2. 09:20-10:00\n3. 10:15-10:55\n4. 11:10-11:50\n5. 12:05-12:45\n6. 12:55-13:35\n7. 13:45-14:25\n8. 14:30-15:10', reply_markup=keyboard9, parse_mode='Markdown')
    elif callback.data == 'Pyatnica1':
        bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f'Расписание на Пятницу:\n---------------------------------\n1. 08:30-9:10\n2. 09:20-10:00\n3. 10:15-10:55\n4. 11:10-11:50\n5. 12:05-12:45\n6. 12:55-13:35\n7. 13:45-14:25\n8. 14:30-15:10', reply_markup=keyboard9, parse_mode='Markdown')
bot.polling(none_stop=False, interval=0)