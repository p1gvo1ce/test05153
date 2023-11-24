coins = [10, 5, 2, 1, 0.5]    # список доступных номиналов

while True: # добиваемся ввода числового значения кратного 0,5
    try:
        price = float(input('Введите числовое значение с плавающей точкой кратное 0,5\n').replace(',','.'))
        if price % 0.5 == 0:
            break
        else:
            print('Ошибка ввода')
    except:
        print('Ошибка ввода')

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

for i in my_coin: # выводим результат
    print(f'{i}: {my_coin[i]}')
