# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.


from datetime import datetime


def date_check(user_date: str):
    try:
        val = datetime.strptime(user_date, "%d.%m.%Y").date()
        return True
    except:
        return False


if __name__ == '__main__':
    print("Проверка")
    print(date_check(input('Введите дату (dd.mm.YYYY) - ')))