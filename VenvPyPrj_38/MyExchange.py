import redis  # импортируем библиотеку
import requests
from bs4 import BeautifulSoup as bs
# from time import time
# from pprint import pprint

currency_dict = {'RUR': ['российский рубль', 'рубль', 'рубли'],
                 'USD': ['доллары сша', 'доллар', 'доллары', 'баксы', 'баксов', 'us dollar', 'US Dollar'],
                 'EUR': ['евро'],
                 'CNY': ['китайский юань', 'юань', 'доллары', 'баксы', 'баксов'],
                 }

def get_exchange_list_xrates(currency, amount=1):
    # создаем запрос к x-rates.com для получения валют и курсов
    content = requests.get(f'https://www.x-rates.com/table/?from={currency}&amount={amount}').content
    # инициализируем beautifulsoup
    soup = bs(content, 'html.parser')
    # получаем дату-время последнего обновления курса
    # price_datetime = parse(soup.find_all("span", attrs={"class": "ratesTimestamp"})[1].text)
    price_datetime = soup.find_all("span", attrs={"class": "ratesTimestamp"})[1].text
    # получаем таблицу курсов
    exchange_tables = soup.find_all('table')
    exchange_rates = {}
    for exchange_table in exchange_tables:
        for tr in exchange_table.find_all('tr'):
            tds = tr.find_all('td')
            if tds:
                currency = tds[0].text
                # получим курс
                exchange_rate = float(tds[1].text)
                exchange_rates[currency] = exchange_rate
    return price_datetime, exchange_rates

def get_exchange_convert_sum(currency, amount=1):
    # создаем запрос к x-rates.com для получения валют и курсов
    content = requests.get(f'https://www.x-rates.com/table/?from=RUB&amount={amount}').content
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
                for cur in range(len(currency_dict[currency])):
                    if tds[0].text == currency_dict[currency][cur]:
                        exchange_rate1 = round(float(tds[1].text), 2)  # курс продажи
                        exchange_rate2 = round(float(tds[2].text), 2)  # курс покупки
                        exchange_rates[currency] = exchange_rate2
                        # print('tds[0]: ', tds[0])  # <td>US Dollar</td>
                        # print('tds[1]: ', tds[1])  # <td class="rtRates"><a href="https://www.x-rates.com/graph/?from=RUB&amp;to=USD">12.418301</a></td>
                        # print('tds[2]: ', tds[2])  # <td class="rtRates"><a href="https://www.x-rates.com/graph/?from=USD&amp;to=RUB">80.526314</a></td>

                        return price_datetime, exchange_rates

    # return price_datetime, exchange_rates # если показывать все валюты
def start_processing(input_list):
    amount = int(input_list[-1])
    input_list.pop()
    name_currency = ' '.join(input_list)

    for dict_key, dict_values in currency_dict.items():
        for i in range(len(dict_values)):
            if dict_values[i] == name_currency.lower():
                source_currency = dict_key
                break

    price_datetime, exchange_rates = get_exchange_convert_sum(source_currency, amount)
    print('Last updated:', price_datetime)
    print(source_currency, ' ', exchange_rates[source_currency])

def redis():

    red = redis.Redis(
        host='localhost',
        # ваш хост, если вы поставили Редис к себе на локальную машину, то у вас это будет localhost. Если же вы находитесь на Windows, то воспользуйтесь полем host из вашей облачной БД, которую мы создавали в скринкасте.
        port=6379,
        # порт подключения. На локальной машине это должно быть 6379. Для пользователей облачного сервиса порт всегда разный, поэтому его надо копировать оттуда же, что и host.
        password=''
        # для локальной машины пароль не требуется (если вы устанавливали Редис к себе на компьютер и не пользовались облачным сервисом из скринкаста выше). Для пользователей облачного сервиса пароль находится в вашей облачной базе данных в поле password
    )
    red.set('var1', 'value1')  # записываем в кеш строку "value1"
    print(red.get('var1'))  # считываем из кеша данные


if __name__ == '__main__':
    redis()
    # start_processing(['Доллары', 'США', '1000'])
    # import sys
    # print(sys.argv)
    # source_currency = sys.argv[1]
    # amount = float(sys.argv[2])
    # target_currency = 'RUB'  #"GBP"
    # price_datetime, exchange_rates = get_exchange_list_xrates(source_currency, amount)
    # print('Last updated:', price_datetime)
    # pprint(exchange_rates)

# [<td>Chinese Yuan Renminbi</td>,
# <td class="rtRates">
# <a href="https://www.x-rates.com/graph/?from=USD&amp;to=CNY">7013.490458</a></td>,
# <td class="rtRates"><a href="https://www.x-rates.com/graph/?from=CNY&amp;to=USD">0.142582</a></td>]
