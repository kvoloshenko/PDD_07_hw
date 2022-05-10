import os
import json
import bank.bank as bank

def test_account_get():
    file_name = 'bank_data.json'
    if os.path.exists(file_name):
        os.remove(file_name)
    # проверка на ноль, когда нет файла
    assert bank.account_get() == 0
    account = 21
    purchases = []
    purchase_1 = 'покупка 1'
    sum_1 = 10
    purchases.append({'purchase': purchase_1, 'sum': sum_1})
    purchase_2 = 'bbb 2'
    sum_2 = 20
    purchases.append({'purchase': purchase_2, 'sum': sum_2})
    # print(f'purchases={purchases}')
    all_data = {}
    all_data['account'] = account
    all_data['purchases'] = purchases
    # проверка на значение из файла
    with open(file_name, 'w', encoding='utf8') as f:
        json.dump(all_data, f)
    assert bank.account_get() == account
    os.remove(file_name)

def test_account_add():
    file_name = 'bank_data.json'
    if os.path.exists(file_name):
        os.remove(file_name)
    # проверка на ноль, когда нет файла
    account = 21
    purchases = []
    purchase_1 = 'покупка 1'
    sum_1 = 10
    purchases.append({'purchase': purchase_1, 'sum': sum_1})
    purchase_2 = 'bbb 2'
    sum_2 = 20
    purchases.append({'purchase': purchase_2, 'sum': sum_2})
    # print(f'purchases={purchases}')
    all_data = {}
    all_data['account'] = account
    all_data['purchases'] = purchases
    # проверка на значение из файла
    with open(file_name, 'w', encoding='utf8') as f:
        json.dump(all_data, f)
    bank.account_add(9)
    assert bank.account_get() == 30
    os.remove(file_name)


def test_data_save():
    file_name = 'bank_data.json'
    account = 21
    purchases = []
    purchase_1 = 'покупка 1'
    sum_1 = 10
    purchases.append({'purchase': purchase_1, 'sum': sum_1})
    purchase_2 = 'bbb 2'
    sum_2 = 20
    purchases.append({'purchase': purchase_2, 'sum': sum_2})
    # print(f'purchases={purchases}')
    all_data = {}
    all_data['account'] = account
    all_data['purchases'] = purchases
    bank.data_save(all_data)
    assert os.path.exists(file_name)
    assert os.path.isfile(file_name)
    with open(file_name, 'r', encoding='utf8') as f:
        loaded_all_data = json.load(f)
        assert loaded_all_data == all_data
        loaded_account = loaded_all_data['account']
        assert account == loaded_account
        # print(type(loaded_account), f' loaded_account={loaded_account}')
        loaded_purchases = loaded_all_data['purchases']
        # print(type(loaded_purchases), f' loaded_purchases={loaded_purchases}')
        assert purchases == loaded_purchases
    os.remove(file_name)

def test_data_read():
    assert bank.data_read() == {}
    file_name = 'bank_data.json'
    account = 21
    purchases = []
    purchase_1 = 'покупка 1'
    sum_1 = 10
    purchases.append({'purchase': purchase_1, 'sum': sum_1})
    purchase_2 = 'bbb 2'
    sum_2 = 20
    purchases.append({'purchase': purchase_2, 'sum': sum_2})
    all_data = {}
    all_data['account'] = account
    all_data['purchases'] = purchases
    with open(file_name, 'w', encoding='utf8') as f:
        json.dump(all_data, f)
    assert bank.data_read() == all_data
    os.remove(file_name)

