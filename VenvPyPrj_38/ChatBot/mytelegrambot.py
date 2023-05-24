# Задание
# Напишите Telegram-бота, в котором будет реализован следующий функционал:
#  +  1. Бот возвращает цену на определённое количество валюты (евро, доллар или рубль).
#  +  2. При написании бота необходимо использовать библиотеку pytelegrambotapi.
#  +  3. Человек должен отправить сообщение боту в виде <имя валюты, цену которой он хочет узнать> <имя валюты, в которой
#        надо узнать цену первой валюты> <количество первой валюты>.
#  +  4. При вводе команды /start или /help пользователю выводятся инструкции по применению бота.
#  +  5. При вводе команды /values должна выводиться информация о всех доступных валютах в читаемом виде.
#  +  6. Для получения курса валют необходимо использовать любое удобное API и отправлять к нему запросы с помощью
#        библиотеки Requests.
#  ?  7. Для парсинга полученных ответов использовать библиотеку JSON.
#  +  8. При ошибке пользователя (например, введена неправильная или несуществующая валюта или неправильно введено число)
#        вызывать собственно написанное исключение APIException с текстом пояснения ошибки.
#  +  9. Текст любой ошибки с указанием типа ошибки должен отправляться пользователю в сообщения.
#  + 10. Для отправки запросов к API описать класс со статическим методом get_price(), который принимает три аргумента и
#        возвращает нужную сумму в валюте:
#      - имя валюты, цену на которую надо узнать, — base;
#      - имя валюты, цену в которой надо узнать, — quote;
#      - количество переводимой валюты — amount.
# + 11. Токен Telegram-бота хранить в специальном конфиге (можно использовать .py файл).
# + 12. Все классы спрятать в файле extensions.py.

import extensions
import telebot
import cfgtelegrambot

bot = telebot.TeleBot(cfgtelegrambot.TOKEN)

command_list = ['/start',     # старт
                '/help',      # помощь
                '/exchange',  # запуск конвертера валют
                '/values'     # список доступных валют
                ]

# Обрабатываются все сообщения, содержащие команду '/start'.
@bot.message_handler(commands=['start',])
def handle_start(message):
    bot.send_message(message.chat.id, f'{message.from_user.first_name}, привет')  # message.chat.username -
    bot.send_message(message.chat.id, 'Бот возвращает цену на определённое количество валюты (список можно посмотреть набрав команду /valutes).\n'
                                      'Напишите какую валюту в какую пересчитать и сумму '
                                      '(например: EUR RUB 10 или евро рубль 10)')

# Обрабатываются все сообщения, содержащие команду '/help'.
@bot.message_handler(commands=['help',])
def handle_help(message):
    bot.send_message(message.chat.id, 'Бот возвращает цену на определённое количество валюты (список можно посмотреть набрав команду /valutes).\n'
                                      'Напишите какую валюту в какую пересчитать и сумму '
                                      '(например: EUR RUB 10 или евро рубль 10)')
    bot.send_message(message.chat.id, 'Команды бота:\n'
                                      '/start - приветствие =)\n'
                                      '/help - помощь\n'
                                      '/valutes - список доступных валют')

# Обрабатываются все сообщения, содержащие команду '/valutes'.
@bot.message_handler(commands=['valutes', ])
def handle_valutes(message):
    val_dict = []
    for val_k, val_v in cfgtelegrambot.currency_dict.items():
        val_dict.append(val_k + ' - ' + val_v[0])
    bot.send_message(message.chat.id, 'Доступные валюты:\n' + '\n'.join(val_dict))

@bot.message_handler(content_types=['text',])
def handle_text(message):
    try:
        if message.text not in command_list:
            base = message.text.split()[0]    # валюта которую пересчитываем
            quote = message.text.split()[1]   # валюта в которую пересчитываем
            amount = message.text.split()[2]  # необходимая сумма

            ex = extensions.Exchange([], base, quote, amount)
            date_rate, rate_value, rp_list = ex.get_currency_rates()  # получение курсов
            for r_code, r_value in rate_value.items():
                # выводим данные пользователю
                # bot.send_message(message.chat.id, f'{r_value} {rp_list[1]} за {amount} {rp_list[0]}\nДата обновления курса: {date_rate}')
                bot.reply_to(message, f'{r_value} {rp_list[1]} за {amount} {rp_list[0]}\nДата обновления курса: {date_rate}')
    except extensions.AmountIncorrect as err:
        bot.send_message(message.chat.id, err)
    except extensions.CurrentEqual as err:
        bot.send_message(message.chat.id, err)
    except extensions.CurrentNotFound as err:
        bot.send_message(message.chat.id, err)
    except extensions.JsonDecodIncorrect as err:
        bot.send_message(message.chat.id, err)
    else:
        pass  # bot.send_message(message.chat.id, 'Все ок!')
    finally:
        bot.send_message(message.chat.id, 'Спасибо Вам за использование нашего бота!')

bot.polling(none_stop=True)

