# Задание
# Напишите Telegram-бота, в котором будет реализован следующий функционал:
# 1. Бот возвращает цену на определённое количество валюты (евро, доллар или рубль).
# 2. При написании бота необходимо использовать библиотеку pytelegrambotapi.
# 3. Человек должен отправить сообщение боту в виде <имя валюты, цену которой он хочет узнать> <имя валюты, в которой надо узнать цену первой валюты> <количество первой валюты>.
# 4. При вводе команды /start или /help пользователю выводятся инструкции по применению бота.
# 5. При вводе команды /values должна выводиться информация о всех доступных валютах в читаемом виде.
# 6. Для получения курса валют необходимо использовать любое удобное API и отправлять к нему запросы с помощью библиотеки Requests.
# 7. Для парсинга полученных ответов использовать библиотеку JSON.
# 8. При ошибке пользователя (например, введена неправильная или несуществующая валюта или неправильно введено число) вызывать собственно написанное исключение APIException с текстом пояснения ошибки.
# 9. Текст любой ошибки с указанием типа ошибки должен отправляться пользователю в сообщения.
# 10. Для отправки запросов к API описать класс со статическим методом get_price(), который принимает три аргумента и возвращает нужную сумму в валюте:
#     - имя валюты, цену на которую надо узнать, — base;
#     - имя валюты, цену в которой надо узнать, — quote;
#     - количество переводимой валюты — amount.
# 11. Токен Telegram-бота хранить в специальном конфиге (можно использовать .py файл).
# 12. Все классы спрятать в файле extensions.py.

# import requests  # импортируем наш знакомый модуль
# import lxml.html
# from lxml import etree
from myexchange import start_processing

# import pytelegrambotapi
import telebot
# import config
import cfgtelegrambot

# TOKEN = "5957782602:AAEq8reL8N957GbRfGsqYgv-Kk6p5Ys1UC0"

bot = telebot.TeleBot(cfgtelegrambot.TOKEN)

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
    bot.send_message(message.chat.id, 'Бот возвращает цену на определённое количество валюты (евро, доллар или рубль)')
    bot.send_message(message.chat.id, 'Напишите какую валюту в какую пересчитать и сумму')
    bot.send_message(message.chat.id, '(например: EUR RUB 10 или евро рубль 10)')
    # < имя валюты, цену которой он хочет узнать >
    # < имя валюты, в которой надо узнать цену первой валюты >
    # < количество первой валюты >

# Обрабатывается все документы и аудиозаписи
@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    pass

@bot.message_handler(content_types=['text',])
def handle_text(message):
    if message.text not in command_list:
        # bot.send_message(message.chat.id, f'Text: {message.text.split()}')  # ['Доллары', 'США', '1000']
        bot.send_message(message.chat.id, message.text.split())
        start_processing(message.text.split())

@bot.message_handler(content_types=['photo',])
def handle_photo(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')

@bot.message_handler(commands=['exchange', ])
def handle_exchange(message):
    bot.send_message(message.chat.id, 'Какую валюту нужно пересчитать, в какую и сумму')
    bot.send_message(message.chat.id, '(например: EUR RUB 10 или евро рубль 10)')
    # < имя валюты, цену которой он хочет узнать >
    # < имя валюты, в которой надо узнать цену первой валюты >
    # < количество первой валюты >

    # if message.text not in command_list:
    #     bot.send_message(message.chat.id, f'Вы написали: {message.text}')   # Доллары США 1000
    #     start_processing(list(message.text.split))
    # bot.send_message(message.chat.id, f'Вы написали: {message.text}')

bot.polling(none_stop=True)

