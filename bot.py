import telebot
import random
from telebot.types import Message
coin = ['Орел', 'Решка']
numbers = '123456789'
symbols = '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM@#$%&'

bot = telebot.TeleBot('{TOKEN}', parse_mode='HTML')
@bot.message_handler(commands=['start', 'privet'])
def start(message: Message):
    bot.reply_to(message, 'Привет!')
@bot.message_handler(commands=['coin', 'autor', 'number', 'password', 'commands', 'photo'])
def main(message):
    text = message.text.lower()
    if text == '/autor':
        bot.reply_to(message, 'Автор этого бота - Самойлов Дмитрий')
    if text == '/coin':
        bot.reply_to(message, random.choice(coin))
    if text == '/number':
        bot.reply_to(message, 'Рандомное число: ' + random.choice(numbers))
    if text == '/password':
        lenght = 12
        password = ''
        for i in range(lenght):
            password += random.choice(symbols)
        print(password)
        bot.reply_to(message, 'Ваш пароль: ' + password)
    if text == '/commands':
        bot.reply_to(message, 'Команды: /autor, /coin, /number, /password')

    
bot.infinity_polling()
