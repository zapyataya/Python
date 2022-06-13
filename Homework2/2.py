#Список
my_list = [
    ['Stark', 'Winter is Coming'],
    ['Lannister', 'A Lannister always pays his debts'],
    ['Greyjoy', 'What Is Dead May Never Die']
]

#Словарь
my_dict = {
    'Stark': 'Winter is Coming',
    'Lannister': 'A Lannister always pays his debts',
    'Greyjoy': 'What Is Dead May Never Die'
}

#Множество
my_set = {'Winter is Coming', 'A Lannister always pays his debts', 'What Is Dead May Never Die'}

#Задача - найти и вывести значение фразы семьи Старк

#Решение задачи для списка
for i in my_list:
    if i[0] == 'Stark':
        print(i[1])

#Решение задачи для словаря
print(my_dict['Stark'])

#Для множества не нашла способ решить указанную задачу, так как элементы множества не упорядочены

#Для решения поставленной задачи лучше всего подходит словарь, так как для каждого значения можно указать ключ, с помощью которого легко можно найти нужное значение
