coins = [10, 5, 2, 1, 0.5]    # список доступных номиналов

def input_price():        # добиваемся ввода числового значения кратного 0,5
    while True:
        try:
            price = float(input('Введите числовое значение с плавающей точкой кратное 0,5\n').replace(',','.'))
            if price % 0.5 == 0:
                return price
            else:
                print('Ошибка ввода')
        except:
            print('Ошибка ввода')

def calculation(price):        # вычисление минимального количества монет
    my_coin = {        # определяем состояние кошелька
        'монет 10': 0,
        'монет 5': 0,
        'монет 2': 0,
        'монет 1': 0,
        'монет 0.5': 0
    }
    my_money = 0 # текущий баланс

    while my_money != price:
        for coin in coins: # последовательно перебираем номиналы монет
            while my_money + coin <= price: # добавляем по одной пока не превысим целевое значение
                my_money += coin # добавляем монету на баланс и в кошелек
                my_coin.update({f'монет {coin}': my_coin[f'монет {coin}']+1})
    return my_coin

while True:        # цикл для проверки множества вариантов
    price = input_price()            # ввод целевой суммы
    my_coin = calculation(price)     # вычисление

    for i in my_coin: # выводим результат
        print(f'{i}: {my_coin[i]}')
                                            # проверка намерения повторить с новой суммой
    if input('Введите "Y" чтобы повторить или иное чтобы завершить:\n').lower() != 'y':
        break
