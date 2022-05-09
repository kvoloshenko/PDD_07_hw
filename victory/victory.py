import numpy as np

"""
7. (МОДУЛЬ 4) В проекте создать новый модуль victory.py. Задание
Написать или улучшить программу Викторина из предыдущего дз (Для тренировки предлагаю не пользоваться никакими библиотеками кроме random)
Есть 10 известных людей и их даты рождения в формате '02.01.1988' ('dd.mm.yyyy') - предлагаю для тренировки пока использовать строку
Программа выбирает из этих 10-и 5 случайных людей, это можно реализовать с помощью модуля random и функции sample
Пример использования sample:
import random
numbers = [1, 2, 3, 4, 5]
# 2 - количество случайных элементов
result = random.sample(numbers, 2)
print(result) # [5, 1]
После того как выбраны 5 случайных людей, предлагаем пользователю ввести их дату рождения
пользователь вводит дату в формате 'dd.mm.yyyy'
Например 03.01.2009, если пользователь ответил неверно, то выводим правильный ответ, но уже в следующем виде: третье января 2009 года, склонением можно пренебречь
В конце считаем количество правильных и неправильных ответов и предлагаем начать снова
"""

"""
03.01.1956 Мел Гибсон
06.01.1938 Адриано Челентано
07.01.1964 Николас Кейдж
08.01.1935 Элвис Прэсли
17.01.1962 Джим Кэрри
18.01.1955 Кевин Костнер
24.01.1961 Настасья Кински
27.01.1964 Бриджит Фонда
23.02.1944 Олег Янковский
05.03.1955 Орнелла Мути
"""
def run():
    persons = [{'birthday': '03.01.1956', 'name': 'Мел Гибсон'},
               {'birthday': '06.01.1938', 'name': 'Адриано Челентано'},
               {'birthday': '07.01.1964', 'name': 'Николас Кейдж'},
               {'birthday': '08.01.1935', 'name': 'Элвис Прэсли'},
               {'birthday': '17.01.1962', 'name': 'Джим Кэрри'},
               {'birthday': '18.01.1955', 'name': 'Кевин Костнер'},
               {'birthday': '24.01.1961', 'name': 'Настасья Кински'},
               {'birthday': '27.01.1964', 'name': 'Бриджит Фонда'},
               {'birthday': '23.02.1944', 'name': 'Олег Янковский'},
               {'birthday': '05.03.1955', 'name': 'Орнелла Мути'}]

    # print(type(persons),persons)

    number_of_unique_attempts = 0
    while (number_of_unique_attempts != 5): # пока не получим 5 разных случайных чисел
        random_integer_array = np.random.randint(0, 10, 5)
        # print(random_integer_array)
        s_digits = set(random_integer_array)
        number_of_unique_attempts = len(s_digits)
        # print ('number_of_unique_attempts=',number_of_unique_attempts)

    number_of_correct_answers = 0
    n = 1
    for i in random_integer_array:
        # print(i)
        # print(persons[i]['birthday'])
        # print(persons[i]['name'])
        s = 'Попытка №' + str(n) + ': Введите дату рождения ' + persons[i]['name'] + 'в формате dd.mm.yyyy: '
        n += 1
        answer = input(s)
        if persons[i]['birthday'] == answer:
            number_of_correct_answers += 1
        else:
            print('правильный ответ:', persons[i]['birthday'])

    print('Количество правильных ответов=', number_of_correct_answers)

if __name__ == '__main__':
    run()