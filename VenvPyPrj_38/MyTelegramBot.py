# import requests  # импортируем наш знакомый модуль
# import lxml.html
# from lxml import etree
from MyExchange import get_exchange_list_xrates

import telebot
# import config

TOKEN = "5957782602:AAEq8reL8N957GbRfGsqYgv-Kk6p5Ys1UC0"

bot = telebot.TeleBot(TOKEN)

command_list = ['/start',     # старт
                '/help',      # помощь
                '/exchange'   # запуск конвертера валют
                ]

# Обрабатываются все сообщения, содержащие команду '/start'.
@bot.message_handler(commands=['start',])
def handle_start(message):
    bot.send_message(message.chat.id, f'{message.from_user.first_name}, привет')  # message.chat.username -

# Обрабатываются все сообщения, содержащие команду '/help'.
@bot.message_handler(commands=['help',])
def handle_help(message):
    pass

# Обрабатывается все документы и аудиозаписи
@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    pass

@bot.message_handler(content_types=['text',])
def handle_text(message):
    if message.text not in command_list:
        bot.send_message(message.chat.id, f'Вы написали: {message.text}')   # Доллары США 1000
        msg_list = message.text.split()
        # msg_list = '\n'.join(message.text.split())

        bot.send_message(message.chat.id, msg_list)
        # get_exchange_list_xrates(msg_list[0])

@bot.message_handler(content_types=['photo',])
def handle_photo(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')

@bot.message_handler(commands=['exchange',])
def handle_exchange(message):
    bot.send_message(message.chat.id, 'Напишите какую сумму и в какой валюте Вам нужно'
                                      ' пересчитать (например: EUR 1000 или евро 1000)')
    if message.text not in command_list:
        bot.send_message(message.chat.id, f'Вы написали: {message.text}')   # Доллары США 1000
    # get_exchange_list_xrates()
    # bot.send_message(message.chat.id, f'Вы написали: {message.text}')

bot.polling(none_stop=True)


# @bot.message_handler(commands=['exchange',])
# def handle_start(message):
#     html = requests.get('https://ya.ru/').content  # получим html главной странички сайта с курсами
#
#     tree = etree.parse('F:\Work\Vlad\Python\Итоговый проект\Яндекс.html', lxml.html.HTMLParser())
#     # попытаемся спарсить наш файл с помощью html-парсера. Сам html - это то,
#     # что мы скачали и поместили в папку из браузера.
#
#     # xpath: '/html/body/main/div[2]/div/div/a[1]/span'
#     ul = tree.findall('/body/main/div[2]/div/div/a')
#     # помещаем в аргумент метода findall скопированный xpath. Здесь мы получим
#     # все элементы списка курсов (код валюты и цена в рублях)
#
#     bot.send_message(message.chat.id, 'Введите сумму')
#     bot.
#
#     # создаём цикл, в котором мы будем выводить название каждого элемента из списка
#     msg = ''
#     rate = []
#     for span in ul:
#         msg += span.find('span').text + '\n'  # в каждом элементе находим, где хранится курс валюты.
#         rate.append(span.find('span').text)
#
#         # print('a: ', a.text)  # из этого тега забираем текст
#     bot.send_message(message.chat.id, f'Курсы на сегодня\n{msg}')  # message.chat.username -
#
# bot.polling(none_stop=True)
