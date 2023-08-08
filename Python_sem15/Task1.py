# 1. Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.


import logging

logging.basicConfig(filename="error.log", encoding="utf-8", level=logging.WARNING)
logger = logging.getLogger(__name__)


def div(a: int, b: int) -> float:
    res = None
    try:
        res = a / b
    except ZeroDivisionError as e:
        logger.error(e)
    return res


if __name__ == '__main__':
    # print(div(4, 0))
    print(div(4, 2))