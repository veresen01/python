# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
import os

DCT = {'Видео': ('mkv', 'avi', 'mp4'),
       'Изображение' : ('png', 'jpg', 'jpeg'),
       'Текст': ('txt', 'bin')}

def group(dir_):
    files = [file for file in os.listdir() if os.path.isfile(file)]
    for fold, exts in DCT.items():
        if fold not in os.listdir():
            os.mkdir(fold)
        for file in files:
            if file.split('.')[1] in exts:
               # os.replace(file, fold + '\\' + file)
                os.replace(file, os.path.join(os.getcwd(), fold, file))

if __name__ == '__main__':
    group(os.getcwd())