import telebot
from utils import *

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def echo_test(message: telebot.types.Message):
    text = 'Чтобы начать работу введите, команду боту в следующем формате: \
    <имя валюты> <в какоую валюту перевести> <количество переводимой валюты>\n \
    Увидить список доступных валют: /valuse '
    bot.reply_to(message, text)


@bot.message_handler(commands=['valuse'])
def valuse(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def converter(message: telebot.types.Message):
    values = message.text.split()

    if len(values) != 3:
        raise ConvertionExeption('Слишком много параметров')

    base, sym, amount = values
    res = Converter.convert(sym, base, amount)
    text = f'Цена {amount} {base} в {sym} - {res}'
    bot.send_message(message.chat.id, text)


bot.polling()
