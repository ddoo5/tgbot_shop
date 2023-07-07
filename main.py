import telebot

file = open('./apitoken.txt')
mytoken = file.read()
bot = telebot.TeleBot(mytoken)