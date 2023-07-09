import random
import telebot
import webbrowser
from telebot import types

# достаем api ключ из файла
file = open('./apitoken.txt')
mytoken = file.read()

# подключаем api ключ
bot = telebot.TeleBot(mytoken)

# ответы на непредвиденные ситуации
answers = ['Sorry, I don\'t understand', 'I don\'t know this command.', 'Please, try again', 'Use buttons']


@bot.message_handler(commands=['start'])
def Greeting(message):
    # кнопки
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('🛍 Products')
    button2 = types.KeyboardButton('🛒  Shopping cart')
    button3 = types.KeyboardButton('⚙️ Settings')
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
    if message.text == '🛍 Products':
        productsChapter(message)

    elif message.text == '🛒  Shopping cart':
        cartChapter(message)

    elif message.text == '⚙️ Settings':
        settingsChapter(message)

    elif message.text == '📄 FAQ':
        faqChapter(message)

    elif message.text == '🔹 Product #1':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        incart = False

        button1 = types.KeyboardButton('➕ Add to cart')
        button2 = types.KeyboardButton('↩️ Back')

        markup.row(button1, button2)

        img = open('./imgs/items/product1.jpg', 'rb')
        bot.send_photo(message.chat.id, img)

        bot.send_message(message.chat.id, 'Some Camera', reply_markup=markup)

    elif message.text == '🔴 Product #2':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        incart = False

        button1 = types.KeyboardButton('↩️ Back')

        markup.row(button1)

        img = open('./imgs/items/product2.jpeg', 'rb')
        bot.send_photo(message.chat.id, img)

        bot.send_message(message.chat.id, 'Sorry, this product unavailable.\nPlease, come back later', reply_markup=markup)

    elif message.text == '🔴 Product #3':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        incart = False

        button1 = types.KeyboardButton('↩️ Back')

        markup.row(button1)

        img = open('./imgs/items/product3.jpeg', 'rb')
        bot.send_photo(message.chat.id, img)

        bot.send_message(message.chat.id, 'Sorry, this product unavailable.\nPlease, come back later', reply_markup=markup)

    elif message.text == '🔹 Product #4':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        incart = False

        img = open('./imgs/items/product4.jpeg', 'rb')
        bot.send_photo(message.chat.id, img)

        bot.send_message(message.chat.id, 'Some belt', reply_markup=markup)

    elif message.text == '🔹 Product #5':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        incart = False

        img = open('./imgs/items/product5.jpeg', 'rb')
        bot.send_photo(message.chat.id, img)

        bot.send_message(message.chat.id, 'Some stand for sneakers', reply_markup=markup)

    elif message.text == '🔹 Product #6':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        incart = False

        img = open('./imgs/items/product6.jpeg', 'rb')
        bot.send_photo(message.chat.id, img)

        bot.send_message(message.chat.id, 'Some wireless headphones', reply_markup=markup)

    elif message.text == '🔴 Product #7':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        incart = False

        button1 = types.KeyboardButton('↩️ Back')

        markup.row(button1)

        img = open('./imgs/items/product7.jpeg', 'rb')
        bot.send_photo(message.chat.id, img)

        bot.send_message(message.chat.id, 'Sorry, this product unavailable.\nPlease, come back later',reply_markup=markup)

    elif message.text == '🔹 Product #8':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        incart = False

        img = open('./imgs/items/product8.jpeg', 'rb')
        bot.send_photo(message.chat.id, img)

        bot.send_message(message.chat.id, 'Some keyboard', reply_markup=markup)

    elif message.text == '⚙️ Set up cart':
        bot.send_message(message.chat.id, 'Настройки номер 1...')

    elif message.text == '➕ Add to cart':
        #do something
        bot.send_message(message.chat.id, '✅ Added')

        productsChapter(message)

    elif message.text == '📝️ About us':
        bot.send_message(message.chat.id, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\nUt enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\nDuis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.\nExcepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum')

    elif message.text == '✏️ Write to dev':
        webbrowser.open('https://t.me/l_dd_I')

    elif message.text == '↩️ Back':
        productsChapter(message)

    elif message.text == '↩️ Back to main menu':
        Greeting(message)

    else:
        bot.send_message(message.chat.id, answers[random.randint(0, 3)])


# Products
def productsChapter(message):
    # Кнопки для товаров
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button1 = types.KeyboardButton('🔹 Product #1')
    button2 = types.KeyboardButton('🔴 Product #2')
    button3 = types.KeyboardButton('🔴 Product #3')
    button4 = types.KeyboardButton('🔹 Product #4')
    button5 = types.KeyboardButton('🔹 Product #5')
    button6 = types.KeyboardButton('🔹 Product #6')
    button7 = types.KeyboardButton('🔴 Product #7')
    button8 = types.KeyboardButton('🔹 Product #8')
    button9 = types.KeyboardButton('↩️ Back to main menu')

    markup.row(button1, button2, button3)
    markup.row(button4, button5, button6)
    markup.row(button7, button8, button9)

    bot.send_message(message.chat.id, '🔹 - available\n 🔴 - sold out', reply_markup=markup)


# Cart
def cartChapter(message):
    print('some')


# Settings
def settingsChapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button1 = types.KeyboardButton('⚙️ Set up cart')
    button2 = types.KeyboardButton('↩️ Back to main menu')

    markup.row(button1, button2)

    bot.send_message(message.chat.id, 'Here you can set up your cart', reply_markup=markup)


# FAQ
def faqChapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button1 = types.KeyboardButton('📝️ About us')
    button2 = types.KeyboardButton('✏️ Write to dev')
    button3 = types.KeyboardButton('↩️ Back to main menu')

    markup.row(button1, button2, button3)

    bot.send_message(message.chat.id, 'Welcome to faq.\nHere you can know something about us and write to my developer ^_^', reply_markup=markup)


# non stop
bot.polling(none_stop=True)
