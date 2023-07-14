# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строкаcsv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы функции.

import json
import csv

def func(csv_file, file_json):
    with (open(csv_file, "r", encoding="UTF-8") as csv_f,
          open(file_json, "w", encoding="UTF-8",newline='') as json_f):
        file = [*csv.reader(csv_f)]
        headers_id, headers_name, headers_access = file[0]
        lst = []
        for id, name, access in file[1:]:
            lst.append({headers_id: id, headers_name: name, headers_access: access, 'hash': hash(name + id)})

        json.dump(lst, json_f, ensure_ascii=False, indent=2)

if __name__=='__main__':
    func('names.csv','names2.json')