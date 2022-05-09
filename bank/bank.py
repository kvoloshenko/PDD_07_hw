"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""
account = 0
purchases = []

def purchase_get():
    global purchases
    if len(purchases) == 0:
        print('Список покупок пуст')
    else:
        print ('Список совершенных покупок:')
        for purchase in purchases:
            print('  ', purchase['purchase'], ' :',purchase['sum'])

def purchase_add():
    while True:
        answer = input('Введите сумму покупки: ')
        if answer.isdigit(): break
    sum = int(answer)
    global account
    if sum <= account:
        account -= sum
        purchase = input('Введите описание покупки: ')
        global purchases
        purchases.append({'purchase': purchase, 'sum': sum})
        #print(purchases)
    else: print ('Недостаточно средств на счету')

def account_add():
    while True:
        answer = input('Введите сумму пополнения счета: ')
        if answer.isdigit(): break

    sum = int(answer)
    global account
    account += sum


def account_get():
    print('Сейчас на счету: ', account)

def run():
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню : ')
        if choice == '1':
            account_add()
            account_get()
        elif choice == '2':
            purchase_add()
            account_get()
        elif choice == '3':
            purchase_get()
            account_get()
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')
