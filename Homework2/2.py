# Список: определить, какой из семей принадлежит фраза 'Winter is Coming')
my_list = [
    ['Stark', 'Winter is Coming'],
    ['Lannister', 'A Lannister always pays his debts'],
    ['Greyjoy', 'What Is Dead May Never Die']
]

for i in my_list:
    if i[1] == 'Winter is Coming':
        print(i[0])

# можно обратиться к нужному элементу по индексу
# можно добавлять и удалять элементы
# может содержать дубликаты
# поддерживает вложенность (списки можно хранить внутри других списков)

# Словарь: определить, какая фраза принадлежит семье Stark
my_dict = {
    'Stark': 'Winter is Coming',
    'Lannister': 'A Lannister always pays his debts',
    'Greyjoy': 'What Is Dead May Never Die'
}

print(my_dict['Stark'])

# у каждого значения словаря есть уникальный ключ, который выступает идентификатором элемента
# можно добавлять и удалять элементы
# нельзя вывести ключ с помощью значения
# поддерживает вложенность

# Множество: определить, какой из семей принадлежит фраза 'Winter is Coming')
my_set_Stark = {'Winter is Coming'}
my_set_Lannister = {'A Lannister always pays his debts'}
my_set_Greyjoy = {'What Is Dead May Never Die'}

if 'Winter is Coming' in my_set_Stark:
    print('Stark')
if 'Winter is Coming' in my_set_Lannister:
    print('Lannister')
if 'Winter is Coming' in my_set_Greyjoy:
    print('Greyjoy')

# элементы множества не являются индексированными, нельзя обратиться к нужному элементу по индексу
# можно добавлять и удалять элементы
# не может содержать дубликаты
# не поддерживает вложенность

# наиболее удобным способом хранения считаю словарь, так как в нем есть уникальный идентификатор (ключ)
