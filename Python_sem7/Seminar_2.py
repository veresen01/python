# ✔ Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

import random as rnd

def my_func(num, name):
    literals = 'ёйцукенгшщзхъэждлорпавыфячсмитьбю'
    vowels = 'аеиоуэюя'
    min_ = 4
    max_ = 7
    with open (name, 'w', encoding='utf-8') as f:
        for _ in range(num):
            name = rnd.sample(literals, rnd.randint(min_, max_))
            if not set(name) & set(vowels):
                half = len(name) // 2
                name = name[:half] + rnd.sample(vowels,half)
                rnd.shuffle(name)
            name = ''.join(name).capitalize()
            f.write(f'{name}\n')


if __name__=='__main__':
    my_func(10, 'file_2.txt')