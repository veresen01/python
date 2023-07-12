# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.
import os
import random
import string

def create_files_with_extension(extension, min_name_lenght=6, max_name_lenght=30, min_file_size=256, max_file_size=4096, num_files=1):
    for _ in range(num_files):
        name_lenght = random.randint(min_name_lenght, max_name_lenght)
        file_name = ''.join(random.choices(string.ascii_letters + string.digits, k=name_lenght)) + '.' + extension

        file_size = random.randint(min_file_size, max_file_size)
        random_bytes = os.urandom(file_size)
        # random_bytes = ''.join(random.choices(string.ascii_letters + string.digits, k=file_size)).encode('UTF-8')

        with open(file_name, 'wb') as file:
            file.write(random_bytes)


def create_dif_files (**kwargs):
    for ext, num in kwargs.items():
        create_files_with_extension(ext, num_files=num)

if __name__=='__main__':
    create_dif_files(txt=2, bin=4, png=8)
