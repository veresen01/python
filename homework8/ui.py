from get_push_data import get_data
from add_data import add_data

def operations():
    print('Выберите действие: \n1 - вывести информацию об учениках \n2 - добавить запись \n3 - выход из программы')
    a = input('Введите номер операции: ')

    while True:
        if a == '1':
            print(*get_data())
            operations()
        if a == '2':
            add_data()
            operations()
        if a == '3':
            exit()