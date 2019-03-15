import csv
user_info = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
        ]

with open('users_list.csv', 'w', encoding='utf-8', newline='\n') as new_file:
    fields = ['name', 'age', 'job',]
    writer = csv.DictWriter(new_file, fields, delimiter=';')
    writer.writeheader()
    for user in user_info:
        writer.writerow(user)