import os_tools.tools as f
import os
import shutil
import bank.bank_data as bd
import json


# тесты для "чистых" функций
def test_about():
    assert f.about() == '(c) Konstantin Voloshenko'


# тесты для "грязных" функций
def test_create_dir():
    dir_name = 'test_dir_1'
    if os.path.exists(dir_name):
        os.rmdir(dir_name)
    f.create_dir(dir_name)
    assert os.path.exists(dir_name)
    os.rmdir(dir_name)


def test_del_dir():
    dir_name = 'test_dir_2'
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    f.del_dir(dir_name)
    assert not os.path.exists(dir_name)


def test_copy_dir():
    dir_name = 'test_copy_dir1'
    dir_new = 'test_copy_dir2'
    os.mkdir(dir_name)
    f.copy_dir(dir_name, dir_new)
    assert os.path.exists(dir_new)
    os.rmdir(dir_name)
    os.rmdir(dir_new)


def test_info_dir():
    cur_dir = os.getcwd()
    dir_name = 'test_info_dir'
    os.mkdir(dir_name)
    os.chdir(dir_name)
    os.mkdir('test_dir_1')
    os.mkdir('test_dir_2')
    open('test_file_1', mode='a').close()
    open('test_file_2', mode='a').close()
    assert f.info_dir('dirs') == ['test_dir_1', 'test_dir_2']
    assert f.info_dir('files') == ['test_file_1', 'test_file_2']
    assert f.info_dir('all') == ['test_dir_1', 'test_dir_2', 'test_file_1', 'test_file_2']
    os.chdir(cur_dir)
    # os.rmdir(dir_name)
    shutil.rmtree(dir_name, ignore_errors=True)


def test_info_os():
    assert len(f.info_os()) > 1


def test_data_save():
    file_name = 'bank_data.json'
    all_data = {}
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
    bd.data_save(all_data)
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
    assert bd.data_read() == {}
    file_name = 'bank_data.json'
    all_data = {}
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
    assert bd.data_read() == all_data
    os.remove(file_name)

