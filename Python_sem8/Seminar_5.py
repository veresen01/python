# Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.

import os
import json
import pickle

def my_func (dir_):
    json_files = [i for i in os.listdir(dir_) if i.endswith('.json')]
    for json_file in json_files:
        with (open(os.path.join(dir_, json_file), "r", encoding="UTF-8") as f,
              open(os.path.join(dir_, json_file.rstrip('.json') + '.pickle'), "wb") as f_c):
            pickle.dump(json.load(f),f_c)

if __name__=='__main__':
    my_func(os.getcwd())
    with open('name.pickle', "rb") as f:
        print(pickle.load(f))