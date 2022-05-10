import os_tools.tools as f
import bank.bank as b
import victory.victory as v
"""
Консольный файловый менеджер
"""
while True:
    print('1. создать папку')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('61. сохранить содержимое рабочей директории в файл')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории')
    print('12. выход')

    choice = input('Выберите пункт меню : ')
    if choice == '1':
        dir_name = input('   Введите имя папки: ')
        f.create_dir(dir_name)
    elif choice == '2':
        dir_name = input('   Введите имя папки или файла : ')
        f.del_dir(dir_name)
    elif choice == '3':
        dir_name = input('   Введите имя папки или файла: ')
        dir_new = input('   Введите новое имя папки или файла: ')
        f.copy_dir(dir_name, dir_new)
    elif choice == '4':
        for item in f.info_dir('all'):
            print('      ', item)
    elif choice == '5':
        for item in f.info_dir('dirs'):
            print('      ', item)
    elif choice == '6':
        for item in f.info_dir('files'):
            print('      ', item)
    elif choice == '61':
        f.save_info_dir()
        print('      Данные успешно сохранены')
    elif choice == '7':
        print('      ', f.info_os())
    elif choice == '8':
        print('      ', f.about())
    elif choice == '9':
        v.run()
    elif choice == '10':
        b.run()
    elif choice == '11':
        f.chenge_dir()
    elif choice == '12':
        break
    else:
        print('Неверный пункт меню')
