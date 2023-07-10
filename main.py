import random
import telebot
from telebot import types

import main

# достаем api ключ из файла
file = open('./apitoken.txt')
mytoken = file.read()

# подключаем api ключ
bot = telebot.TeleBot(mytoken)

# переменные
balance = 0
numberOfProduct = 0
# есть идея реализации через сущность, но я полистал, почитал и пришел к выводу, что там куча библиотек и быстрее напишу так, нежели буду пробовать через них
products = [['Some Camera', './imgs/items/product1.jpg', 'available'],
            ['', './imgs/items/product2.jpeg', 'sold out'],
            ['', './imgs/items/product3.jpeg', 'sold out'],
            ['Some belt', './imgs/items/product4.jpeg', 'available'],
            ['Some stand for sneakers', './imgs/items/product5.jpeg', 'available'],
            ['Some wireless headphones', './imgs/items/product6.jpeg', 'available'],
            ['', './imgs/items/product7.jpeg', 'sold out'],
            ['Some keyboard', './imgs/items/product8.jpeg','available' ]]
cart = []


@bot.message_handler(commands=['start'])
def Greeting(message):
    # кнопки
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('🛍 Products')
    button2 = types.KeyboardButton('🛒  Shopping cart')
    button3 = types.KeyboardButton('💰️ Balance')
    button4 = types.KeyboardButton('📄 FAQ')

    # разделение кнопок по строкам
    markup.row(button1, button2)
    markup.row(button3, button4)

    # приветственный текст
    if message.text == '/start':
        bot.send_message(message.chat.id, f'Welcome, {message.from_user.first_name}!\nHere you can buy some items.\nPlease, use buttons', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Welcome back to main menu!', reply_markup=markup)


# обработка фото
@bot.message_handler(content_types='photo')
def get_photo(message):
    bot.send_message(message.chat.id, 'Sorry, I can\'t watch photos.')


# обработка обычных комманд из кнопок
@bot.message_handler()
def info(message):
    num = 1

    if message.text == '🛍 Products':
        productsChapter(message)

    elif message.text == '🛒  Shopping cart':
        cartChapter(message)

    elif message.text == '💰️ Balance':
        balanceChapter(message)

    elif message.text == '📄 FAQ':
        faqChapter(message)

    for a in main.products:
        if a[2] == 'available':
            if message.text == f'🔹 Product #{num}':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

                main.numberOfProduct = num

                button1 = types.KeyboardButton('➕ Add to cart')
                button2 = types.KeyboardButton('↩️ Back')

                markup.row(button1, button2)

                # открытие изображения
                img = open(f'{a[1]}', 'rb')
                bot.send_photo(message.chat.id, img)

                bot.send_message(message.chat.id, f'{a[0]}', reply_markup=markup)

        elif a[2] == 'sold out':
            if message.text == f'🔴 Product #{num}':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

                button1 = types.KeyboardButton('↩️ Back')

                markup.row(button1)

                img = open(f'{a[1]}', 'rb')
                bot.send_photo(message.chat.id, img)

                bot.send_message(message.chat.id, 'Sorry, this product unavailable.\nPlease, come back later', reply_markup=markup)

        else:
            print('Error in main')

        num += 1

    if message.text == '➕ Add to cart':
        checker = addToCart(main.numberOfProduct)

        if checker == True:
            bot.send_message(message.chat.id, '✅ Added')
        else:
            bot.send_message(message.chat.id, '❌ Some exceptions happened\n Please, try again later or write to dev')

        productsChapter(message)

    elif message.text == '📝️ About us':
        bot.send_message(message.chat.id, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\nUt enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\nDuis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.\nExcepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum')

    elif message.text == '✏️ Write to dev':
        bot.send_message(message.chat.id, 'https://t.me/l_dd_I')

    elif message.text == '💳 Deposit':
        bot.send_message(message.chat.id, 'This function is unavailable.\nSorry for that >_<, we will add it later')

    elif message.text == '💳 Check out':
        bot.send_message(message.chat.id, 'This function is unavailable.\nSorry for that >_<, we will add it later')

    elif message.text == '🗂️ Display cart items':
        items = dispCart(message)

        for a in items:
            if len(items) > 1:
                num = items.count(a)
                print(a + f' ({num})')
            else:
                print(a)

    elif message.text == '↩️ Back':
        productsChapter(message)

    elif message.text == '↩️ Back to main menu':
        Greeting(message)




# Products
def productsChapter(message):
    # Кнопки для товаров
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    num = 1

    # был вариант с массивом, но куда остаток девать - хз. вопрос 'а если добавят 1 товар?' не получил ответа
    for a in main.products:
        if a[2] == 'available':
            markup.add(f'🔹 Product #{num}')
        elif a[2] == 'sold out':
            markup.add(f'🔴 Product #{num}')
        else:
            print('Error in method productsChapter')

        num += 1

    buttonBack = types.KeyboardButton('↩️ Back to main menu')
    markup.add(buttonBack)

    bot.send_message(message.chat.id, '🔹 - available\n 🔴 - sold out', reply_markup=markup)


# Cart
# Кстати про корзину глянул, бд хостить надо или такая пойдет(ранее ботов просто не писал, думал можно как-то легко дописать user id и все, а тут классика - через бд)?
def cartChapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button1 = types.KeyboardButton('💳 Check out')
    button2 = types.KeyboardButton('🗂️ Display cart items')
    button3 = types.KeyboardButton('↩️ Back to main menu')

    markup.row(button1, button2, button3)

    if len(main.cart) > 0:
        bot.send_message(message.chat.id, f'{message.from_user.first_name}, Welcome to your cart!', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, f'{message.from_user.first_name}, Welcome to your cart!\nHere is nothing', reply_markup=markup)


# Balance
def balanceChapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button1 = types.KeyboardButton('💳 Deposit')
    button2 = types.KeyboardButton('↩️ Back to main menu')

    markup.row(button1, button2)

    bot.send_message(message.chat.id, f'{message.from_user.first_name}, your balance is {balance}', reply_markup=markup)


# FAQ
def faqChapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button1 = types.KeyboardButton('📝️ About us')
    button2 = types.KeyboardButton('✏️ Write to dev')
    button3 = types.KeyboardButton('↩️ Back to main menu')

    markup.row(button1, button2, button3)

    bot.send_message(message.chat.id, 'Welcome to faq.\nHere you can know something about us and write to my developer ^_^', reply_markup=markup)


# Добавление в корзину
def addToCart(num):
    num -= 1
    main.cart.append([main.products[num][0], main.products[num][1]])
    return True


# Отображение корзины
def dispCart(message):
    text = []

    for i in main.cart:
        text.append(i[0] + '\n')
    return text


# non stop
bot.polling(none_stop=True)
