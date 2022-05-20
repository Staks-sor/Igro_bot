from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# hi
button1 = KeyboardButton('Создать персонажа')  # +
button2 = KeyboardButton('Начать игру')  # +
markup0 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    button1).add(button2)

# tutorial
button1 = KeyboardButton('Отправь мне ссылку на созданного персонажа')  # +

markup1 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    button1)

# begin

button1 = KeyboardButton('Подойти к окну')  # +
button2 = KeyboardButton('Подойти к двери')  # +
button3 = KeyboardButton('Подойти к люку')
markup2 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    button1).add(button2).add(button3)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# window story

button1 = KeyboardButton('Разобраться с мыслями')  # +
button2 = KeyboardButton('Осмотреть экран')  # +
button3 = KeyboardButton('Идти к "ВОТ"')  # +
markup3 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    button1).add(button2).add(button3)
# mind
button1 = KeyboardButton('Да, разобраться')  # +
button2 = KeyboardButton('Нет, к экрану')  # +
button3 = KeyboardButton('Нет, идти к "ВОТ"')  # +
markup4 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    button1).add(button2).add(button3)


button1 = KeyboardButton('Сердце')  # +
button2 = KeyboardButton('Орган')  # +
button3 = KeyboardButton('Рисунок')  # +
markup5 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    button2).add(button3).add(button1)

button1 = KeyboardButton('Ждать')  # +
button2 = KeyboardButton('Бежать')  # +
markup6 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    button1).add(button2)

button1 = KeyboardButton('1')  # +wait
button2 = KeyboardButton('2')  # +
button3 = KeyboardButton('3')  # +
markup7 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    button1).add(button2).add(button3)

button1 = KeyboardButton('Рассказать правду')  # +
button2 = KeyboardButton('Солгать')  # +
markup8 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    button1).add(button2)

button1 = KeyboardButton('Д')  # +wait
button2 = KeyboardButton('Ж')  # +
button3 = KeyboardButton('Р')  # +
markup9 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    button2).add(button1).add(button3)

button1 = KeyboardButton('100')  # +
button2 = KeyboardButton('50')  # +
button3 = KeyboardButton('200')  # +
markup10 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    button1).add(button2).add(button3)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# door


button1 = KeyboardButton('Букварь')  # +
button2 = KeyboardButton('Блокнот')  # +
button3 = KeyboardButton('Бумажка')  # +
markup11 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    button1).add(button2).add(button3)

button1 = KeyboardButton('К кабанам')  # +
button2 = KeyboardButton('К Гере')  # +
button3 = KeyboardButton('Сойти с ума')  # +
markup12 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    button1).add(button2).add(button3)

button1 = KeyboardButton('Груша')  # +
button2 = KeyboardButton('Лампочка')  # +
button3 = KeyboardButton('Яблоко')  # +
markup13 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    button3).add(button2).add(button1)

button1 = KeyboardButton('Да')  # +
button2 = KeyboardButton('Нет')  # +
markup14 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    button1).add(button2)

button1 = KeyboardButton('Лампочка')  # +
button2 = KeyboardButton('Груша')  # +
markup002 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    button1).add(button2)

button4 = KeyboardButton('Конечно!')  # +
button2 = KeyboardButton('Нет, спасибо.')  # +
markup000 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    button4).add(button2)

button4 = KeyboardButton('Прекратить читать')  # +
button2 = KeyboardButton('Продолжить')  # +
markup001 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    button4).add(button2)


button1 = KeyboardButton('Все рассказать')  # +
button3 = KeyboardButton('Игнорировать')  # +
markup15 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    button1).add(button3)

button5 = KeyboardButton('2.')  # +
button2 = KeyboardButton('94.')  # +
button3 = KeyboardButton('0.')  # +
markup16 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    button2).add(button5).add(button3)

button1 = KeyboardButton('Войти')  # +
button2 = KeyboardButton('Разрушить')  # +
markup17 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    button1).add(button2)

button1 = KeyboardButton('Да, разрушить')  # +
button2 = KeyboardButton('Передумать')  # +
markup18 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    button1).add(button2)

button1 = KeyboardButton('Моргнуть')  # +
markup003 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    button1)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# luke

button1 = KeyboardButton('Сейчас')  # +
button2 = KeyboardButton('После истории')  # +
markup19 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    button1).add(button2)

button1 = KeyboardButton('Дальше')  # +
markup01 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    button1)

button1 = KeyboardButton('Слушать')  # +
markup02 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    button1)

button1 = KeyboardButton('Внимать')  # +
markup03 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    button1)

button1 = KeyboardButton('Еще')  # +
markup04 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    button1)

button1 = KeyboardButton('Хорошим')  # +
button2 = KeyboardButton('Плохим')  # +
markup05 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    button1).add(button2)

button1 = KeyboardButton('Слушать дальше')  # +
markup06 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    button1)

button1 = KeyboardButton('Слушать еще')  # +
markup07 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    button1)

button1 = KeyboardButton('Слушать больше')  # +
markup08 = ReplyKeyboardMarkup(resize_keyboard=True).add(
    button1)
