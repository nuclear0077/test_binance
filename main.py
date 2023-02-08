import requests
import time

# В этом примере функция get_max_price_xrp_usdt_last_hour 
# получает исторически максимальную цену за последний час, далее
# функция get_price использует библиотеку
# запросов для получения последней цены XRP/USDT
# от Binance. Код устанавливает переменную start_time в текущее время и входит
# в бесконечный цикл, который извлекает цену и проверяет, упала ли она на 1%
# от максимальной цены за последний час. Если время,
# прошедшее с момента start_time,
# больше или равно 1 часу, код сбрасывает max_price на 0,
# а start_time на текущее время.
# Если цена упала на 1%, код выводит сообщение в консоль.
# Цикл продолжается бесконечно, постоянно получая последнюю цену.


def get_max_price_xrp_usdt_last_hour():
    endpoint = "https://api.binance.com/api/v3/klines?symbol=XRPUSDT&interval=1h&limit=1"
    response = requests.get(endpoint)
    data = response.json()
    return float(data[0][2])


def get_price():
    response = requests.get(
        "https://api.binance.com/api/v3/ticker/price?symbol=XRPUSDT")
    return float(response.json()["price"])


max_price = get_max_price_xrp_usdt_last_hour()
print("Максимальная цена XRP/USDT за последний час:", max_price)
start_time = time.time()


while True:
    price = get_price()
    if price > max_price:
        max_price = price
    if (time.time() - start_time) / 3600 >= 1:
        max_price = price
        start_time = time.time()
    if max_price * 0.99 > price:
        print("Цена упала на 1%")
