# ✔ Напишите функцию, которая заполняет файл  (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

from random import randint, uniform

MIN_V = -1000
MAX_V = 1000
def my_func(count_row, filename):
    with open (filename, 'a', encoding='utf-8') as f:
        for _ in range(count_row):
            f.write(f'{randint(MIN_V, MAX_V)}|{round(uniform(MIN_V, MAX_V),2)}\n')


if __name__=='__main__':
    my_func(10, 'file_1.txt')