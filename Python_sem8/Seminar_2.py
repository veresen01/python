# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны в пределах одного уровня доступа.
# При перезапуске функции уже записанные в файл данные должны сохраняться.

import json
import os

def func(file_json):
    if os.path.isfile(file_json):
        with open(file_json, "r", encoding="UTF-8") as f:
            dict_res = json.load(f)
    else:
        dict_res = {str(i):{} for i in range(1, 8)}

    while True:
        data = input('Введите через пробел имя, ID, уровень доступа:')
        if not data:
            break
        user_input, id, access = data.split()
        if id not in dict_res[access]:
            dict_res.setdefault(access, {id:user_input})[id] = user_input

    with open(file_json, 'w', encoding='utf-8') as f:
        json.dump(dict_res, f, ensure_ascii=False)





if __name__=='__main__':
    func('names.json')