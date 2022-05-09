import json

all_data = {}
account = 21
purchases = []
purchase_1 = 'aaa 1'
sum_1 = 10
purchases.append({'purchase': purchase_1, 'sum': sum_1})
purchase_2 = 'bbb 2'
sum_2 = 20
purchases.append({'purchase': purchase_2, 'sum': sum_2})
print(f'purchases={purchases}')
all_data['account'] = account
all_data['purchases'] = purchases
print(f'all_data={all_data}')

"""
jsonStr = json.dumps(all_data)
print(f'jsonStr={jsonStr}')

loaded_all_data = json.loads(jsonStr)

print(type(loaded_all_data),f' loaded_all_data={loaded_all_data}')
loaded_account = loaded_all_data ['account']
print(type(loaded_account), f' loaded_account={loaded_account}')
loaded_purchases = loaded_all_data ['purchases']
print(type(loaded_purchases), f' loaded_purchases={loaded_purchases}')
"""

# Сохранение в файл
with open('bank_data.json', 'w') as f:
    json.dump(all_data, f)


with open('bank_data.json', 'r') as f:
    loaded_all_data = json.load(f)
    print(type(loaded_all_data), f' loaded_all_data={loaded_all_data}')
    loaded_account = loaded_all_data['account']
    print(type(loaded_account), f' loaded_account={loaded_account}')
    loaded_purchases = loaded_all_data['purchases']
    print(type(loaded_purchases), f' loaded_purchases={loaded_purchases}')
