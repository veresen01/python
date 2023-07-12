# Дорабатываем функции из предыдущих задач.
#Генерируйте файлы в указанную директорию — отдельный параметр функции.
# Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

from Seminar_5 import create_dif_files
from pathlib import Path
import os


def create_dir(name_dir: str):
    name = Path(Path.cwd() / name_dir)
    if not name.exists():       #проверка на наличие директория
        name.mkdir()            #создает директорий с именем name_dir в текущем директории
    os.chdir(name)          #переходим в созданный каталог сделав его текущим


if __name__ == '__main__':
    create_dif_files(txt=2, bin=4, png=8)
    create_dir('new')