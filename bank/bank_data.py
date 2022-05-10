import json
import os

def data_save(all_data):
    # print(f'all_data={all_data}')
    # Сохранение в файл
    with open('bank_data.json', 'w', encoding='utf8') as f:
        json.dump(all_data, f)

def data_read():
    if os.path.exists('bank_data.json'):
        with open('bank_data.json', 'r', encoding = 'utf8') as f:
            loaded_all_data = json.load(f)
        return loaded_all_data
    else:
        all_data = {}
        return all_data