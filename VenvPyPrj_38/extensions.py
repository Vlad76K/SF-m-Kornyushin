# Задание
# Напишите Telegram-бота, в котором будет реализован следующий функционал:
#  1. Бот возвращает цену на определённое количество валюты (евро, доллар или рубль).
#  2. При написании бота необходимо использовать библиотеку pytelegrambotapi.
#  3. Человек должен отправить сообщение боту в виде <имя валюты, цену которой он хочет узнать> <имя валюты, в которой
#     надо узнать цену первой валюты> <количество первой валюты>.
#  4. При вводе команды /start или /help пользователю выводятся инструкции по применению бота.
#  5. При вводе команды /values должна выводиться информация о всех доступных валютах в читаемом виде.
#  6. Для получения курса валют необходимо использовать любое удобное API и отправлять к нему запросы с помощью
#     библиотеки Requests.
#  7. Для парсинга полученных ответов использовать библиотеку JSON.
#  8. При ошибке пользователя (например, введена неправильная или несуществующая валюта или неправильно введено число)
#     вызывать собственно написанное исключение APIException с текстом пояснения ошибки.
#  9. Текст любой ошибки с указанием типа ошибки должен отправляться пользователю в сообщения.
# 10. Для отправки запросов к API описать класс со статическим методом get_price(), который принимает три аргумента и
#     возвращает нужную сумму в валюте:
#      - имя валюты, цену на которую надо узнать, — base;
#      - имя валюты, цену в которой надо узнать, — quote;
#      - количество переводимой валюты — amount.
# 11. Токен Telegram-бота хранить в специальном конфиге (можно использовать .py файл).
# 12. Все классы спрятать в файле extensions.py.

import json
import requests
from bs4 import BeautifulSoup as bs

currency_dict = {'RUB': ['Российский рубль', 'рубль', 'рублей', 'Russian Ruble'],
                 'USD': ['Доллары сша', 'доллары', 'долларов', 'доллар', 'баксы', 'баксов', 'us dollar', 'US Dollar'],
                 'EUR': ['Евро', 'евро', 'евро', 'Euro'],
                 'CNY': ['Китайский юань', 'юань', 'юаней', 'Chinese Yuan Renminbi'],
                 }

class ExchangeBotException(Exception):
    pass

class BaseCurrentNotFound(ExchangeBotException):
    def __init__(self, base):
        self.base = base
        super().__init__(f'Валюта {base} не найдена')

class QuoteCurrentNotFound(ExchangeBotException):
    def __init__(self, quote):
        self.quote = quote
        super().__init__(f'Валюта {quote} не найдена')

class AmountIncorrect(ExchangeBotException):
    def __init__(self, amount):
        self.amount = amount
        super().__init__(f"Не корректно задана сумма: {amount}")

class Exchange:
    def __init__(self, input_list): #, base, quote, amount):
        self.input_list = input_list
        # self.base = base
        # self.quote = quote
        # self.amount = amount

    def test_json(self):  #, base, quote, amount=1):
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        req_get = requests.get(f'https://www.x-rates.com/table/?from={base}&amount={amount}')
        js = json.loads(req_get.text)
        print(js)

    @staticmethod
    def get_exchange_convert_sum(base, quote, amount=1):
        # создаем запрос к x-rates.com для получения валют и курсов
        # content = requests.get(f'https://www.x-rates.com/graph/?from={base}&to={quote}&amount={amount}').content
        content = requests.get(f'https://www.x-rates.com/table/?from={base}&amount={amount}').content

        # инициализируем beautifulsoup
        soup = bs(content, 'html.parser')
        # получаем дату-время последнего обновления курса
        price_datetime = soup.find_all("span", attrs={"class": "ratesTimestamp"})[1].text
        # получаем таблицу курсов
        exchange_tables = soup.find_all('table')
        exchange_rates = {}
        for exchange_table in exchange_tables:
            for tr in exchange_table.find_all('tr'):
                tds = tr.find_all('td')
                if tds:
                    print(quote)
                    print('currency_dict[quote] : ', currency_dict[quote])
                    for cur in range(len(currency_dict[quote])):
                        if tds[0].text == currency_dict[quote][cur]:
                            base_rp = currency_dict[base][2]
                            quote_rp = currency_dict[quote][2]
                            # print(base_rp, ' --- ', quote_rp)
                            exchange_rate1 = round(float(tds[1].text), 2)  # base/quote
                            exchange_rate2 = round(float(tds[2].text), 2)  # quote/base
                            exchange_rates[quote] = exchange_rate1
                            # print('tds[0]: ', tds[0])  # <td>US Dollar</td>
                            # print('tds[1]: ', tds[1])  # <td class="rtRates"><a href="https://www.x-rates.com/graph/?from=RUB&amp;to=USD">12.418301</a></td>
                            # print('tds[2]: ', tds[2])  # <td class="rtRates"><a href="https://www.x-rates.com/graph/?from=USD&amp;to=RUB">80.526314</a></td>

                            return price_datetime, exchange_rates, [base_rp, quote_rp]

        # return price_datetime, exchange_rates # если показывать все валюты

    @staticmethod
    def get_price(base, quote, amount):
        print(base, ' --- ', quote, ' --- ', amount)
        try:
            amount = round(float(amount), 2)

            base_code = ''
            quote_code = ''
            for dict_key, dict_values in currency_dict.items():
                if dict_key == base:
                    base_code = base
                else:
                    for i in range(len(dict_values)):
                        if dict_values[i] == base.lower():
                            base_code = dict_key
                            break
                    else:
                        pass
                if dict_key == quote:
                    quote_code = quote
                else:
                    for i in range(len(dict_values)):
                        if dict_values[i] == quote.lower():
                            quote_code = dict_key
                            break
                        else:
                            pass
                if base == '':
                    # raise ValueError('Не корректное значение валюты которую нужно пересчитать!')
                    raise BaseCurrentNotFound(base)
                if quote == '':
                    # raise ValueError('Не корректное значение валюты в которую нужно пересчитать!')
                    raise QuoteCurrentNotFound(quote)

        except BaseCurrentNotFound:
            raise
        except QuoteCurrentNotFound:
            raise
        except AmountIncorrect:
            raise
        else:
            # ex = Exchange
            # ex.base = base_code
            # ex.quote = quote_code
            # ex.amount = amount
            # price_datetime, exchange_rates, curr_rp_list = ex.get_exchange_convert_sum() #Exchange.get_exchange_convert_sum()
            price_datetime, exchange_rates, curr_rp_list = Exchange.get_exchange_convert_sum(base_code, quote_code, amount)

            return price_datetime, exchange_rates, curr_rp_list
        finally:
            print('Спасибо, что выбрали нашу компанию! =)')

if __name__ == '__main__':
    input_list = ['евро', 'доллары', '10']
    # input_list = ['EUR', 'RUB', '10']
    base = input_list[0]
    quote = input_list[1]
    amount = input_list[2]

    Exchange.get_price(base, quote, amount)

    ex = Exchange(input_list)
    ex.test_json()

    # get_price(['евро', 'доллары', '10'])
    # Exchange.get_price(['EUR', 'RUB', '10'])

