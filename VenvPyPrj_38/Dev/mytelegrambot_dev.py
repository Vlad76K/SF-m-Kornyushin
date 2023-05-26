import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from extensions_dev import Exchange
from Dev import config


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.TOKEN)  # "12345678:AaBbCcDdEeFfGgHh")
# Диспетчер
dp = Dispatcher()

command_list = ['/start',     # старт
                '/help',      # помощь
                '/exchange',  # запуск конвертера валют
                '/values'     # список доступных валют
                ]

# Хэндлер на команду /start
@dp.message(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer('Бот возвращает цену на определённое количество валюты (евро, доллар или рубль).\n'
                         'Напишите какую валюту в какую пересчитать и сумму '
                         '(например: EUR RUB 10 или евро рубль 10)')

# Хэндлер на команду /help
@dp.message(commands=['help'])
async def cmd_help(message: types.Message):
    await message.answer('Бот возвращает цену на определённое количество валюты (евро, доллар или рубль).\n'
                         'Напишите какую валюту в какую пересчитать и сумму '
                         '(например: EUR RUB 10 или евро рубль 10)\n'
                         'Команды бота:\n'
                         '/start - приветствие =)\n'
                         '/help - помощь\n'
                         '/convert - запуск конвертера\n'
                         '/valutes - список доступных валют')

@dp.message(commands=['valutes'])
async def cmd_valutes(message: types.Message):
    val_dict = []
    for val_k, val_v in config.currency_dict.items():
        val_dict.append(val_k + ' - ' + val_v[0])
    await message.answer('Доступные валюты:\n' + '\n'.join(val_dict)

@dp.message(commands=['convert'])
async def cmd_convert(message: types.Message):
    if message.text not in command_list:
        base = message.text.split()[0]  # валюта которую пересчитываем
        quote = message.text.split()[1]  # валюта в которую пересчитываем
        amount = message.text.split()[2]  # необходимая сумма

        ex = Exchange([])
        date_rate, rate_value, rp_list = ex.get_price(base, quote, amount)
        for r_code, r_value in rate_value.items():
            await message.answer(f'{r_value} {rp_list[1]} за {amount} {rp_list[0]}\nДата обновления курса: {date_rate}')


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())








#
# from ChatBot import extensions as start_processing, config
# import telebot
#
#
# bot = telebot.TeleBot(cfgtelegrambot.TOKEN)
#
# command_list = ['/start',     # старт
#                 '/help',      # помощь
#                 '/exchange',  # запуск конвертера валют
#                 '/values'     # список доступных валют
#                 ]
# currency_list = ['RUB - Российский рубль',
#                  'USD - Доллар США',
#                  'EUR - Евро']
#
# # Обрабатываются все сообщения, содержащие команду '/start'.
# @bot.message_handler(commands=['start',])
# def handle_start(message):
#     bot.send_message(message.chat.id, f'{message.from_user.first_name}, привет')  # message.chat.username -
#     bot.send_message(message.chat.id, 'Бот возвращает цену на определённое количество валюты (евро, доллар или рубль).\n'
#                                       'Напишите какую валюту в какую пересчитать и сумму '
#                                       '(например: EUR RUB 10 или евро рубль 10)')
#
# # Обрабатываются все сообщения, содержащие команду '/help'.
# @bot.message_handler(commands=['help',])
# def handle_help(message):
#     bot.send_message(message.chat.id, 'Бот возвращает цену на определённое количество валюты (евро, доллар или рубль).\n'
#                                       'Напишите какую валюту в какую пересчитать и сумму '
#                                       '(например: EUR RUB 10 или евро рубль 10)')
#     bot.send_message(message.chat.id, 'Команды бота:\n'
#                                       '/start - приветствие =)\n'
#                                       '/help - помощь\n'
#                                       '/valutes - список доступных валют')
#     # < имя валюты, цену которой он хочет узнать >
#     # < имя валюты, в которой надо узнать цену первой валюты >
#     # < количество первой валюты >
#
# # Обрабатываются все сообщения, содержащие команду '/valutes'.
# @bot.message_handler(commands=['valutes', ])
# def handle_valutes(message):
#     bot.send_message(message.chat.id, 'Доступные валюты:\n' + '\n'.join(currency_list))
#
# # Обрабатывается все документы и аудиозаписи
# # @bot.message_handler(content_types=['document', 'audio'])
# # def handle_docs_audio(message):
# #     pass
# #
# # @bot.message_handler(content_types=['photo',])
# # def handle_photo(message: telebot.types.Message):
# #     bot.reply_to(message, 'Nice meme XDD')
#
# @bot.message_handler(content_types=['text',])
# def handle_text(message):
#     try:
#         if message.text not in command_list:
#             base = message.text.split()[0]    # валюта которую пересчитываем
#             quote = message.text.split()[1]   # валюта в которую пересчитываем
#             amount = message.text.split()[2]  # необходимая сумма
#
#             ex = start_processing.Exchange([])
#             date_rate, rate_value, rp_list = ex.get_price(base, quote, amount)
#             for r_code, r_value in rate_value.items():
#                 bot.send_message(message.chat.id, f'{r_value} {rp_list[1]} за {amount} {rp_list[0]}\nДата обновления курса: {date_rate}')
#     except start_processing.AmountIncorrect as err:
#         bot.send_message(message.chat.id, err)
#     except start_processing.CurrentEqual as err:
#         bot.send_message(message.chat.id, err)
#     except start_processing.CurrentNotFound as err:
#         bot.send_message(message.chat.id, err)
#     except start_processing.JsonDecodIncorrect as err:
#         bot.send_message(message.chat.id, err)
#     else:
#         pass  # bot.send_message(message.chat.id, 'Все ок!')
#     finally:
#         bot.send_message(message.chat.id, 'Спасибо Вам за использование нашего бота!')
#
# bot.polling(none_stop=True)
#
