# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдоименами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.
import json

def write_json(name):
    with (open(name, "r", encoding="UTF-8") as res,
          open("output.json", "w", encoding="UTF-8") as j):
        dict_res = dict()
        for item in res:
            key, value = item.replace("\n", "").split("|")
            dict_res[key.capitalize()] = value
        json.dump(dict_res, j, ensure_ascii=False, indent=1)



if __name__=='__main__':
    write_json('file_1.txt')