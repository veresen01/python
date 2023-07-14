# Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.


import json
import csv

def func(file_json):
    file_csv = 'names.csv'
    with (open(file_json, "r", encoding="UTF-8") as f,
          open(file_csv, "w", encoding="UTF-8",newline='') as f_с):
        json_dict = json.load(f)
        print(json_dict)
        rows = []
        for level, in_dict in json_dict.items():
            for id, name in in_dict.items():
                rows.append({'id': id, 'level': int(level), 'name': name})
        print(rows)

        csv_write = csv.DictWriter(f_с, fieldnames=['id', 'level', 'name'])
        csv_write.writeheader()
        csv_write.writerows(rows)

if __name__=='__main__':
    func('names.json')


