from get_push_data import get_data, push_data


def add_data():
    result_list = get_data()
    id = int(len(result_list))
    string = ''
    string += str(id)+';'       # list[0] - id ученика
    string += input('Введите фамилию: ') + ';'
    string += input('Введите имя: ') + ';'
    string += input('Введите класс: ') + ';'
    string += input('Введите статус: ') + ';'
    string += input('Введите ряд: ') + ';'
    string += input('Введите номер парты: ') + ';'
    string += input('Введите город: ') + ';'
    string += input('Введите улицу: ') + ';'
    string += input('Введите дом: ') + ';'
    string += input('Введите номер квартиры: ') + ';'
    string += input('Введите примечание: ') + ';'
    print('Добавляем ученика: ', string)
    push_data(string)